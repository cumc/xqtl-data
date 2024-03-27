import math
import time
import io
import boto3
from ftplib import FTP_TLS


S3_BUCKET_NAME = "statfungen"

FTP_HOST = "54.83.44.49"
FTP_PORT = 21
FTP_USERNAME = "xxx"
FTP_PASSWORD = "xxx"

CHUNK_SIZE = 6291456  # 6 MB

def open_ftps_connection(ftp_host, ftp_port, ftp_username, ftp_password):
    """
    Opens ftps connection and returns connection object.
    """
    ftps = FTP_TLS()
    try:
        ftps.connect(ftp_host, ftp_port)
        ftps.login(ftp_username, ftp_password)
        ftps.prot_p()  # Switch to secure data connection
    except Exception as e:
        print("Connection error:", e)
        return None
    return ftps

def transfer_chunk_from_ftp_to_s3(
    s3_connection,
    multipart_upload,
    bucket_name,
    s3_file_path,
    part_number,
    chunk
):
    start_time = time.time()
    part = s3_connection.upload_part(
        Bucket=bucket_name,
        Key=s3_file_path,
        PartNumber=part_number,
        UploadId=multipart_upload["UploadId"],
        Body=chunk,
    )
    end_time = time.time()
    total_seconds = end_time - start_time
    print(
        "Uploaded chunk {} at {} kb/s, taking {} seconds".format(
            part_number, math.ceil((len(chunk) / 1024) / total_seconds), total_seconds
        )
    )
    part_output = {"PartNumber": part_number, "ETag": part["ETag"]}
    return part_output

def transfer_file_from_ftps_to_s3(
    bucket_name, ftp_file_path, s3_file_path, ftp_username, ftp_password, chunk_size
):
    # Initialize the S3 client
    s3_connection = boto3.client('s3')

    ftps_connection = open_ftps_connection(
        FTP_HOST, FTP_PORT, ftp_username, ftp_password
    )
    if ftps_connection is None:
        print("Failed to connect to FTP Server!")
        return

    try:
        ftps_connection.cwd("/")  # Change to the directory if necessary
        ftp_file_size = ftps_connection.size(ftp_file_path)
    except Exception as e:
        print("File does not exist on FTPS Server or other error:", e)
        return

    if ftp_file_size <= chunk_size:
        # Buffer to hold the file data
        file_data_buffer = io.BytesIO()

        # Retrieve the file in binary mode
        ftps_connection.retrbinary('RETR ' + ftp_file_path, file_data_buffer.write)

        # Upload to S3
        file_data_buffer.seek(0)  # Reset buffer pointer to the beginning
        s3_connection.upload_fileobj(file_data_buffer, bucket_name, s3_file_path)
        print("Successfully Transferred file from FTP to S3!")

    else:
        print("Transferring File from FTP to S3 in chunks...")
        # Upload file in chunks
        chunk_count = int(math.ceil(ftp_file_size / float(chunk_size)))
        multipart_upload = s3_connection.create_multipart_upload(
            Bucket=bucket_name, Key=s3_file_path
        )
        parts = []

        for i in range(chunk_count):
            print("Transferring chunk {}...".format(i + 1))
            file_data_buffer = io.BytesIO()
            ftps_connection.retrbinary(
                'RETR ' + ftp_file_path, 
                file_data_buffer.write, 
                blocksize=chunk_size, 
                rest=i*chunk_size
            )
            file_data_buffer.seek(0)
            chunk = file_data_buffer.read(chunk_size)
            part = transfer_chunk_from_ftp_to_s3(
                s3_connection,
                multipart_upload,
                bucket_name,
                s3_file_path,
                i + 1,
                chunk
            )
            parts.append(part)
            print("Chunk {} Transferred Successfully!".format(i + 1))

        part_info = {"Parts": parts}
        s3_connection.complete_multipart_upload(
            Bucket=bucket_name,
            Key=s3_file_path,
            UploadId=multipart_upload["UploadId"],
            MultipartUpload=part_info,
        )
        print("All chunks Transferred to S3 bucket! File Transfer successful!")
        ftps_connection.quit()

def list_files_in_directory(ftps_connection, directory):
    """
    List all files in a specific directory on the FTPS server.
    """
    try:
        ftps_connection.cwd(directory)
        files = ftps_connection.nlst()
        return files
    except Exception as e:
        print("Error listing files:", e)
        return []
    

if __name__ == "__main__":
    ftp_username = FTP_USERNAME
    ftp_password = FTP_PASSWORD
    
    # Connect to FTPS
    ftps_connection = open_ftps_connection(FTP_HOST, FTP_PORT, ftp_username, ftp_password)
    if ftps_connection is None:
        print("Failed to connect to FTP Server!")
    else:
        # Specify the directory on the FTPS server
        ftp_directory = str(input("Enter directory path located on FTPS server: "))
        
        # Get the list of files in the directory
        files_to_transfer = list_files_in_directory(ftps_connection, ftp_directory)
        s3_file_paths = str(input(f"Enter S3 file path to upload: "))
        # Iterate over files and transfer each one
        for file_name in files_to_transfer:
            print(f"Transferring {file_name} from FTP to S3 ")
            ftp_file_path = f"{ftp_directory}/{file_name}"
            s3_file_path = f"{s3_file_paths}/{file_name}"
            transfer_file_from_ftps_to_s3(
                S3_BUCKET_NAME,
                ftp_file_path,
                s3_file_path,
                ftp_username,
                ftp_password,
                CHUNK_SIZE,
            )

        # Close the FTPS connection
        ftps_connection.quit()

#!/usr/bin/env python
# A program to generate table of contents from markdown files
# 2015, Gao Wang
'''
Usage:
python toc.py data/*.md -o toc-data.md -t "Data Resources"
python toc.py utilities/wiki/*.md -o toc-utils.md -t "Utility Resources"
'''

from collections import OrderedDict
from argparse import ArgumentParser
import re

A_TO_Z = '''
|     |     |     |     |     |     |     |     |     |
|:-:  |:-:  |:-:  |:-:  |:-:  |:-:  |:-:  |:-:  |:-:  |
| [#](#0) 	| [A](#a) 	| [B](#b) 	| [C](#c) 	| [D](#d) 	| [E](#e) 	| [F](#f) 	| [G](#g) 	| [H](#h) 	|
| [I](#i) 	| [J](#j) 	| [K](#k) 	| [L](#l) 	| [M](#m) 	| [N](#n) 	| [O](#o) 	| [P](#p) 	| [Q](#q) 	|
| [R](#r) 	| [S](#s) 	| [T](#t) 	| [U](#u) 	| [V](#v) 	| [W](#w) 	| [X](#x) 	| [Y](#y) 	| [Z](#z)  	|'''

class Environment:
    def __init__(self):
        self.blob = ''
        self.exclude = []
        self.remove_ext = 0

env = Environment()

def get_toc(files):
    '''Input: a list of *.md files
    Procedure: parse and get the title and description line in each file
    Output: a dictionary of data : [filename, description]'''
    res = {}
    for item in files:
        if item in env.exclude:
            continue
        n_sec = 0
        lines = [x.strip() for x in open(item).readlines() if x.strip()]
        name = lines[0].strip('#').strip()
        res[name] = [item]
        for line in lines[1:]:
            if line.startswith('#'):
                n_sec += 1
                continue
            else:
                if n_sec == 0 and len(res[name]) == 1:
                    # Take the 1st sentence as description
                    res[name].append(line.split('. ')[0])
                if n_sec == 1:
                    # Take the 1st sentence of the 2nd section as author
                    res[name].append(line.split('. ')[0])
                if not res[name][-1].strip().endswith('.'):
                    res[name][-1] += '.'
            if len(res[name]) == 3:
                break
    return OrderedDict(sorted(res.items(), key=lambda i: i[0].lower()))

def write_toc(toc, page, title, description, contact, add_link = True):
    categories = []
    with open(page, 'w') as f:
        f.write('# {}\n'.format(title))
        if add_link:
            f.write(A_TO_Z)
        if description:
            f.write('{}\n'.format(description))
        for name in toc.keys():
            category = '0' if re.match(r"[-+]?\d+$", name[0]) is not None else name[0].upper()
            if category not in categories:
                categories.append(category)
                f.write('\n## {}\n'.format(category))
            try:
                desc_text = '. {}\n\t* {}**{}**'.format(toc[name][1], contact, toc[name][2]) 
            except:
                # no description line
                desc_text = '.\n\t* {}**{}**'.format(contact, toc[name][1]) 
            link = '{}{}'.format(env.blob, toc[name][0][:-env.remove_ext] if env.remove_ext > 0 else toc[name][0])
            if add_link:
                f.write('* [{}]({}){}\n'.format(name, link, desc_text))
            else:
                f.write('* {}{}\n'.format(name, desc_text))

def main(args):
    if args.base_url:
        env.blob = args.base_url
    if args.exclude:
        env.exclude = args.exclude
    if not args.output.endswith('.md'):
        args.output = args.output.strip('.') + '.md'
    toc = get_toc(args.files)
    write_toc(toc, args.output, args.title, args.description, args.contact_title, not args.no_link)

if __name__ == '__main__':
    parser = ArgumentParser(description = 'A program to generate table of contents from markdown files',
                            epilog = '''2015 by Gao Wang''' )
    parser.add_argument('files', nargs = '+', help = 'Input files')
    parser.add_argument('-o', '--output', required=True, help = 'Output page name')
    parser.add_argument('-c', '--contact_title', default="", help = 'Title for the contact person, eg "Lead analyst", "PI".')
    parser.add_argument('-t', '--title', required=True, help = 'Output page title')
    parser.add_argument('-d', '--description', help = 'Output page description section')
    parser.add_argument('-b', '--base_url', help = 'Base URL for pages')
    parser.add_argument('-e', '--exclude', nargs = '+', help = 'Exclude pages')
    parser.add_argument('-p', '--no-link', action='store_true', help='Plain text, do not include URL')
    main(parser.parse_args())

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# python docx2txt.py
# kiki 2018/11/25

import sys
sys.path.append(r'W:\work_place\Anaconda\Lib\site-packages')
import docx
from docx import Document
INFILE = 'input.docx'
OUTFILE = 'output.txt'

def main():
    document = Document(INFILE)
    with open(OUTFILE, 'w', encoding='utf-8') as outFile:
        outFile.write('')
    with open(OUTFILE, 'w', encoding='utf-8') as outFile:
        for para in document.paragraphs:
            outFile.write(para.text + '\n\n')

if __name__ == "__main__":
	main()

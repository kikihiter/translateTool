#!user/bin/env python
# -*- coding:UTF-8 -*-
# python read_docx.py
# kiki 2018/10/27

from docx import Document
import docx

if __name__ == "__main__":
    docStr = Document("01_Fine-grained+Opinion+Mining+with+Recurrent+Ne.docx")  
    for paragraph in docStr.paragraphs:
        parStr = paragraph.text
        print parStr



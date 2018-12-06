#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#python unifiedFormat01.py
# kiki 2018/10/20
'''
考虑了首字符为特殊符号的情况(已停用此策略)
采用每行字数来判断是否换行
'''


import sys

minLen = 70     #每行最少多少字（认为每一行最少应该有多少字，少于这个字数的行，认为此行为段末，双列布局的英文pdf一般设置为50，单列70

if __name__=="__main__":
    try:
        fpi = open("data.in", "r",encoding='UTF-8')
    except IOError:
        print >> sys.stderr, "failed to open file."
        sys.exit(1)

    try:
        fpo = open("data.out", "w",encoding='UTF-8')
    except IOError:
        print >> sys.stderr, "failed to open file."
        sys.exit(1)


    lineLen = []
    while True:
        line = fpi.readline()
        if not line:
            break
        
        # if line[0].isalpha() == False:
        #     line = '\n'+ '\n' + line
        
        lineLen.append(len(line))
        

        
        line = line.rstrip('\n')
        if line[-1] == '-':
            line = line.rstrip('-')
        elif line[-1] != '-':
            line = line + " "
        if len(line) < minLen:
            line = line + '\n'+ '\n' 
        fpo.write(line)
    print (lineLen)
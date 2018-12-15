#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#python unifiedFormat.py
import sys

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

    while True:
        line = fpi.readline()
        if not line:
            break
        iline = line.lstrip()
        try:
            a =int(iline[0])
            line = '\n' + line
            #line = line.rstrip('\n')+' '
        except:
            
            if line[0] == ' ':
                line = '\n' + line
                
            line = line.rstrip('\n')
            if line[-1] == '-':
                line = line.rstrip('-')
            elif line[-1] != '-':
                line = line + " "
            
            
        #print (line[-1])
        fpo.write(line)
        #fpo.close()
        #if line[-1] == '-':
            #line
        #fpo.write(line.rstrip('\n')+" ")
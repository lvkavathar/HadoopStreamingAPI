#!/usr/bin/env python

import sys
import re
for linenum,line in enumerate(sys.stdin):
        #removing header from the file
        if linenum != 0 :
                count = 0
                #striping whitespaces in a line
                line = line.strip()
                #replacing the content in "" by none
                line = re.sub(r'".*"', '', line)
                #splitting the line in to words seperated by comma
                words=line.split(',')
                for word in words:
                        count = count + 1
                        if count >= 25 and word != "" :
                                print '%s\t%s' %(word,1)

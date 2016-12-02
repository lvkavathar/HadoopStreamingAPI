#!/usr/bin/env python

import sys
import re
for linenum,line in enumerate(sys.stdin):
        if linenum != 0 :
                count = 0
                line = line.strip()
                line = re.sub(r'".*"', '', line)
                words=line.split(',')
                for word in words:
                        count = count + 1
                        if count >= 25 and word != "" :
                                print '%s\t%s' %(word,1)

#!/usr/bin/python
# -*- coding: utf-8 -*-

## DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
##                    Version 2, December 2004
##
## Copyright (C) 2004 Sam Hocevar
##  14 rue de Plaisance, 75014 Paris, France
## Everyone is permitted to copy and distribute verbatim or modified
## copies of this license document, and changing it is allowed as long
## as the name is changed.
##
##            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
##   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
##
##  0. You just DO WHAT THE FUCK YOU WANT TO.

from datetime import datetime
import re

# there are two date formats, e.g.
# 4:53 PM May 19th, 2008
# Sat Apr 25 09:54:24 +0000 2009

def parsedate(line):
    try:
        return datetime.strptime(re.sub(r"(st|nd|rd|th),", ",", line),"Date: %I:%M %p %b %d, %Y\n")
    except ValueError:# try:
        return datetime.strptime(line,"Date: %a %b %d %H:%M:%S +0000 %Y\n")
    
times = sorted([parsedate(line).time() for line in f if line[:6] == "Date: "])

f.close()

BINWIDTH = 1 #minutes

distr = {}
for d in times: 
    try: distr[(d.minute + d.hour*60)/(BINWIDTH)] += 1
    except KeyError: distr[(d.minute + d.hour*60)/(BINWIDTH)] = 1

distr_sum = sum(distr.values())
for i,n in distr.items():
    distr[i] = float(n)/distr_sum

print distr

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

DEBUG = False
N = 2
BINWIDTH = 1 #minutes

TEST = False

import config
import dissociated_press as diss

import twitter
import random

from time import sleep
from datetime import datetime, time
from sys import argv
import re

if argv[1] == "-t": TEST = True

# make a tweet
def tweet(s):
    if config.twitter.username != "":
        twitsession = twitter.Api(config.twitter.username, config.twitter.password, input_encoding="utf-8")
        twitsession.PostUpdate(s)
    print(str(datetime.today()) + ": " + s)

# parse a date line
# there are 2 possible date line formats:
# Date: 4:53 PM May 19th, 2008
# Date: Sat Apr 25 09:54:24 +0000 2009
def parsedate(line):
    try:
        return datetime.strptime(re.sub(r"(st|nd|rd|th),", ",", line),"Date: %I:%M %p %b %d, %Y\n")
    except ValueError:
        return datetime.strptime(line,"Date: %a %b %d %H:%M:%S +0000 %Y\n")
 


infile = config.local.tweetdata
f = open(infile,"r")

# initialize
distr = {} # the distribution of the time of day of the tweets
distrN = 0 # for probability distribution normalization
d = diss.dictionary(debug=DEBUG) # THE dictionary
input = [] # for comparison to avoid simple reposts

for line in f:
    if line[:6] == "Date: ":
        t = parsedate(line).time()
        try: distr[(t.minute + t.hour*60)/(BINWIDTH)] += 1
        except KeyError: distr[(t.minute + t.hour*60)/(BINWIDTH)] = 1
        distrN += 1
    elif line[:6] == "Text: ":
        d.dissociate(line[6:],N=N)
        input.append(line[6:])
f.close()

# the real main loop
while not TEST:
    try:
        t = datetime.today.time()
        if random.random() < float(distr[(t.minute + t.hour*60)/(BINWIDTH)])/distrN: # FIXME: this is utter bullshit
            faketext = ""
            while len(faketext) < 40 or len(faketext) > 140 or faketext in input: # FIXME: still produces reposts
                faketext = d.associate()
            tweet(faketext)
    except KeyError:
        pass
    sleep(BINWIDTH*60)

# modified main loop for testing
if TEST:
    for t in ( time(h,m,s) for h in range(24) for m in range(60) for s in range(60) ):
        try:
            if random.random() < float(distr[(t.minute + t.hour*60)/(BINWIDTH)])/distrN: # FIXME: this is utter bullshit
                faketext = ""
                while len(faketext) < 40 or len(faketext) > 140 or faketext in input: # FIXME: still produces reposts
                    faketext = d.associate()

                print(str(t) + ": " + faketext)
        except KeyError:
            pass


#!/usr/bin/env python2

from random import choice
from sys import stdin
from time import sleep

dict = {}

def dissociate(sent):
    """Feed a sentence to the Dissociated Press dictionary."""
    words = sent.split(" ")
    words.append(None)
    for i in xrange(len(words) - 1):
        if dict.has_key(words[i]):
            if dict[words[i]].has_key(words[i+1]):
                dict[words[i]][words[i+1]] += 1
            else:
                dict[words[i]][words[i+1]] = 1
        else:
            dict[words[i]] = { words[i+1]: 1 }

def associate():
    """Create a sentence from the Dissociated Press dictionary."""
    w = choice(dict.keys())
    r = ""
    while w:
        r += w + " "
        p = []
        for k in dict[w].keys():
            p += [k] * dict[w][k]
        w = choice(p)
    return r

if __name__ == '__main__':
    while 1:
        s = stdin.readline()
        if s == "": break
        dissociate(s[:-1])
    print "=== Dissociated Press ==="
    try:
        while 1:
            print associate()
            sleep(1)
    except KeyboardInterrupt:
        print "=== Enough! ==="


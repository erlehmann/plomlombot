#!/usr/bin/env python2
# 

from random import choice
from sys import stdin
from time import sleep
import re

dict = {}

split_pattern = re.compile('( \w+[%]*|\.|,)')

# substitutions (re.sub-style) applied to input before dissociation
# URL pattern from http://blog.dieweltistgarnichtso.net/constructing-a-regular-expression-that-matches-uris
preprocess_patterns = { 
    r"((?<=\()[A-Za-z][A-Za-z0-9\+\.\-]*:([A-Za-z0-9\.\-_~:/\?#\[\]@!\$&'\(\)\*\+,;=]|%[A-Fa-f0-9]{2})+(?=\)))|([A-Za-z][A-Za-z0-9\+\.\-]*:([A-Za-z0-9\.\-_~:/\?#\[\]@!\$&'\(\)\*\+,;=]|%[A-Fa-f0-9]{2})+)": '',
    r"[!?:]": ".",

    }

preprocess_patterns_compiled = {}
for k in preprocess_patterns.keys():
  preprocess_patterns_compiled[re.compile(k)] = preprocess_patterns[k]

def _preprocess(sent):
  for k in preprocess_patterns_compiled.keys():
    sent = k.sub(preprocess_patterns_compiled[k],sent)
  return sent

# Algorithm based on http://everything2.com/user/Frater%20219/writeups/dissociated+press
def dissociate(sent):
    """Feed a sentence to the Dissociated Press dictionary."""
    words = split_pattern.findall(". " + _preprocess(sent))
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
    # we want to start with the beginning of a sentence
    # the word "." denotes this, so start with that
    w = "."
    r = ""
    # ignore empty lines (which would have a finite probability with most input otherwise)
    while len(r) <= 2:
      w = "."
      r = ""
      while w:
          r += w
          p = []
          for k in dict[w].keys():
              p += [k] * dict[w][k]
          w = choice(p)
    # cut out the ". " at the beginning
    # the "." is the one we inserted above
    # the " " is from the first word
    return r[2:]

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


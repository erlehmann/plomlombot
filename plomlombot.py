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

import config
import dissociated_press as diss

import twitter, time
import random, sys, os

class MainLoop:
    """
    Plomlombot main loop
    """
    if random.random() < 0.025:
        while len(faketext) < 40 or len(faketext) > 140:
            faketext = diss.associate().encode("utf-8")
            #faketext = faketext.replace("@", "@-")
            #faketext = faketext.replace("#", "#-")
            print("Überlege / Twitter: " + faketext)

        twitsession = twitter.Api(config.twitter.username, config.twitter.password, input_encoding="utf-8")
        twitsession.PostUpdate(faketext)
        connection.privmsg(config.irc.logchannel, "Getwittert: " + faketext)
        print("Getwittert: " + faketext)

class Plomlombot:
    """
    Attempts to resimulate Christian Hellers Twitter stream.
    """
    def __init__(self, twituser, tweets):
        self.twituser = twituser
        self.twitpass = twitpass

        twitsession = twitter.Api(self.twituser, self.twitpass)
        tweets = twitsession.GetUserTimeline("plomlompom", tweets)
        for t in tweets:
            diss.dissociate(t.text)
            print("Gelernt: " + t.text)

def main(args):
    if len(args) > 1:
        print('plomlombot takes no arguments. Just run it. If you wish to configure, edit \'config.py\'.')
        return 2

    plom = Plomlombot(
        twituser = config.twitter.username,
        twitpass = config.twitter.password,
        tweets = config.twitter.tweetcount,
    return 1

if __name__ == '__main__':
    sys.exit(main(sys.argv))
else:
    print("plomlombot is a standalone program for now.")

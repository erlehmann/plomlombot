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

import irclib, twitter, time
import random, sys, os

class PlomIRClistener(irclib.SimpleIRCClient):
    """
    Listen to and save Christian Hellers IRC ramblings.
    """
    def on_pubmsg(self, connection, event):
        faketext = ""
        
        if (len(faketext) > 0 and
            event.arguments()[0].rfind(config.irc.username) + 1 and
            event.arguments()[0].rfind("lob") + 1 or
            event.arguments()[0].rfind("bravo") + 1):
            diss.dissociate(faketext)
            connection.privmsg(config.irc.channel, "Danke, danke. Ich werde es mir merken.")
            print("Gelobt: " + faketext)

        if event.arguments()[0].rfind(config.irc.username) + 1:
            while len(faketext) < 20 or len(faketext) > 80:
                faketext = diss.associate().encode("utf-8")
                print("Überlege / IRC: " + faketext)
            connection.privmsg(config.irc.channel, faketext)

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

        if event.source().split('!')[0].startswith("plom"):
            plomtext = event.arguments()[0]
            diss.dissociate(plomtext)
            print("Gelernt: " + plomtext)

class Plomlombot:
    """
    Attempts to resimulate Christian Hellers Twitter stream.
    """
    def __init__(self, twituser, tweets, twitpass, ircuser, ircserver, ircchannel, irclogchannel):
        self.twituser = twituser
        self.twitpass = twitpass

        twitsession = twitter.Api(self.twituser, self.twitpass)
        tweets = twitsession.GetUserTimeline("plomlompom", tweets)
        for t in tweets:
            diss.dissociate(t.text)
            print("Gelernt: " + t.text)

        ircsession = PlomIRClistener()
        ircsession.connect(ircserver, 6667, ircuser, "plomlombot.py")
        ircsession.connection.join (irclogchannel)
        ircsession.connection.join (ircchannel)
        ircsession.connection.privmsg("erlehmann", "De-bug init!")
        ircsession.start()

        print("Starting plomlombot IRC component...")

def main(args):
    if len(args) > 1:
        print('plomlombot takes no arguments. Just run it. If you wish to configure, edit \'config.py\'.')
        return 2

    plom = Plomlombot(
        twituser = config.twitter.username,
        twitpass = config.twitter.password,
        tweets = config.twitter.tweetcount,
        ircuser = config.irc.username,
        ircserver = config.irc.server,
        ircchannel = config.irc.channel,
        irclogchannel = config.irc.logchannel)
    return 1

if __name__ == '__main__':
    sys.exit(main(sys.argv))
else:
    print("plomlombot is a standalone program for now.")

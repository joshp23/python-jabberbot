#!/usr/bin/python3
#
# This is an example JabberBot that serves a Magic 8-ball
# Just Send it a msg as "Magic 8-ball... <Question>"
#
from jabberbot import *
import random
    @botcmd
    def magic(self, mess, args):
        """This is the Magic 8 Ball!"""
        answers = ("It is certain", "It is decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it", "As I see it", "yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy", "try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful")
        return random.choice(answers)

bot = MultiBot("user@example.com", "password")
bot.serve_forever()

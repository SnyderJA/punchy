from slackbot.bot import respond_to
import re

@respond_to('hi', re.IGNORECASE)
def hi(msg):
    msg.reply("what's up my coder")
    msg.react("+1")

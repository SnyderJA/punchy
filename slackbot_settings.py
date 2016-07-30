import os

API_TOKEN = os.environ.get('SLACK_API_TOKEN', '')

DEFAULT_REPLY = "Sorry but I didn't understand you"

PLUGINS = [
    'slackbot.plugins',
    'punchy.plugins',
]

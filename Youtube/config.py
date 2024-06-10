import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7247451117:AAFhxMguFJSrGxt3z7DePTBPxxj3nwQ4Uzs")
    API_ID = int(os.environ.get("API_ID", "27940595")
    API_HASH = os.environ.get("API_HASH", "89a1fa73f8cc1e1002044e1e4e2b7b65")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1001625446236")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''

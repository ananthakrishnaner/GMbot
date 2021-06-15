import telegram
import os
from dotenv import load_dotenv

load_dotenv()
#token that can be generated talking with @BotFather on telegram
my_token = os.getenv('my_token')
chat_id = os.getenv('chat_id')
def sendMessage(msg, chat_id=chat_id, token=my_token):
    """
    Send a message to a telegram user or group specified on chatId
    chat_id must be a number!
    """
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)

sendMessage
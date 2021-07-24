# GMbot
## _Automate your google meet sessions_




GMbot help you to automate your online class.


- Join the meet by puting meet url (with the help of your friend via 
telegram bot)
- Send message via telegram bot
- Stop meet via telegram bot


> Classes are important so I will never promote anyone to use this for 
attending online classes



## Dependencies

#### [packages]
- selenium = "*"
- requests = "*"
- pause = "*"
- colorama = "*"
- termcolor = "*"
- DateTime = "*"
- python-telegram-bot = "*"
- python-dotenv = "*"
- pyrogram = "*"
- schedule = "*"

#### [dev-packages]
- python_version = "3.8"


## Installation

```sh
git clone https://github.com/ananthakrishnaner/GMbot.git
cd GMbot
```

Create a .env file

```sh
nano .env
api_id = ""
api_hash=""
bot_token="bot_token_from_telegram"
USERNAME="myemail@gmail.com"
PASSWORD = "my_password"
my_token = 'same_token_of-bot_token'
chat_id = ''

```



```sh
pipenv shell
```

Add your chromdrive location in 
[gmbot.py](https://github.com/ananthakrishnaner/GMbot/blob/main/gmbot.py#L35)
> Note: `choose chromedrive for your version of browser` 
[chromedrive](https://chromedriver.chromium.org/)

```sh
python gmbot.py
```
[![IMAGE ALT 
TEXT](https://github.com/ananthakrishnaner/GMbot/blob/main/img/gmbotimage.JPG?raw=true)](http://www.youtube.com/watch?v=u1Xhm12Ga2M 
"Video Poc")



[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=3cca959b930b&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)

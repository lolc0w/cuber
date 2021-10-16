from pymem import *
from pymem.process import *
import time
import os
from colorama import Fore, Back, Style

pm = pymem.Pymem("ac_client.exe")
baseStaticAddress = 0x00509B74
base = pm.read_int(baseStaticAddress)
#################
#Variables/Bases#
#################
health = 0xf8
primaryAmmo = 0x150
secondaryAmmo = 0x13C
rifleSpeed = 0x178
secondarySpeed = 0x160
recoil = 0xEE444

while True:
    print('''
       ______      __             
      / ____/_  __/ /_  ___  _____
     / /   / / / / __ \/ _ \/ ___/
    / /___/ /_/ / /_/ /  __/ /    
    \____/\__,_/_.___/\___/_/     
                               ''')
    print("[1] Health")
    print("[2] Primary Ammo")
    print("[3] Secondary Ammo")
    print("[4] Rifle Speed")
    print("[5] Secondary Speed")
    print("[6] Recoil")
    userInput = input("Choose A Number: ")

    if int(userInput) == 1:
        value = int(input("Health Value: "))
        pm.write_int(base+health, value)
        print(Fore.GREEN + "SUCCESS! Your Health has been set to %s"%value)
        time.sleep(1)
        print(Fore.WHITE + "Going Back to Menu...")

    elif int(userInput) == 2:
        value = int(input("Ammo Value: "))
        pm.write_int(base+primaryAmmo, value)
        print(Fore.GREEN + "SUCCESS! Your Primary Ammo has been set to %s"%value)
        time.sleep(1)
        print(Fore.WHITE + "Going Back to Menu...")

    elif int(userInput) == 3:
        value = int(input("Ammo Value: "))
        pm.write_int(base+secondaryAmmo, value)
        print(Fore.GREEN + "SUCCESS! Your Secondary Ammo has been set to %s"%value)
        time.sleep(1)
        print(Fore.WHITE + "Going Back to Menu...")

    elif int(userInput) == 4:
        value = int(input("Choose Your Rifle Speed: "))
        pm.write_int(base+rifleSpeed, value)
        print(Fore.GREEN + "SUCCESS! Your Rifle Speed has been set to %s"%value)
        time.sleep(1)
        print(Fore.WHITE + "Going Back to Menu...")

    elif int(userInput) == 5:
        value = int(input("Choose Your Secondary Speed: "))
        pm.write_int(base+secondarySpeed, value)
        print(Fore.GREEN + "SUCCESS! Your Secondary Speed has been set to %s"%value)
        time.sleep(1)
        print(Fore.WHITE + "Going Back to Menu...")

    elif int(userInput) == 6:
        value = int(input("Recoil: "))
        pm.write_int(base+recoil, value)
        print(Fore.GREEN + "SUCCESS! Your Recoil has been set to %s"%value)
        time.sleep(1)
        print(Fore.WHITE + "Going Back to Menu...")
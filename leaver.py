import os
import requests
from tkinter import *
from tkinter.filedialog import *

print ("Open Token .txt file...")
Tk().withdraw()
token = askopenfilename()
with open(token) as handle:
    txtf = handle.read()

f = open("tokens.txt","w+")
f.write(txtf)
f.close()

ID = input('Discord Server ID to leave: ')

apilink = "https://discordapp.com/api/v6/users/@me/guilds/" + str(ID)

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            requests.delete(apilink, headers=headers)
        print ("All valid tokens have left that server.")
os.remove("tokens.txt")
input()

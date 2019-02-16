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

link = input('Discord Invite Link: ')
if len(link) > 6:
    link = link[19:]
apilink = "https://discordapp.com/api/v6/invite/" + str(link)

print (link)

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            requests.post(apilink, headers=headers)
        print ("All valid tokens have joined!")
os.remove("tokens.txt")
input()

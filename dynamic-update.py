#!/usr/bin/python3
import requests as r
import socket as s
import time
import sys


print("started")
#add username/password from domains.google.com after setting up under DNS>Dynamic DNS
username=""
password=""
#get hostname and concat fqdn if not
hostname=s.gethostname()
hostname=hostname + ".15kmr.com"

def update():
    #this will allow us to manually set our ip4 address from ident.me
    #external_ip = urllib.request.urlopen('https://v4.ident.me/').read().decode('utf8')
    #post=r.post(f"https://{username}:{password}@domains.google.com/nic/update?hostname={hostname}&myip={external_ip}")
    post=r.post(f"https://{username}:{password}@domains.google.com/nic/update?hostname={hostname}")
    date=time.localtime()
    print(f"{post.text}, {date.tm_hour}:{date.tm_min}.{date.tm_sec}, sleeping for one minute")
    sys.stdout.flush()
    time.sleep(60)
    
while (1):
    update()

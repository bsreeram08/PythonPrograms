import time
from datetime import datetime as dt
hosttemp="hosts"
hostpath="C:\Windows\System32\drivers\etc\hosts"
redirect='127.0.0.1'
website_list=["www.uglytub.com","uglytub.com"]
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,18) <= dt.now() and dt(dt.now().year,dt.now().month,dt.now().day,19) >=dt.now():
        print(1)
        with open(hostpath,"r+") as file:
            contents=file.read()
            for websites in website_list:
                if websites in contents:
                    pass
                else:
                    file.write(redirect+" "+websites+"\n")
    else:
        print (0)
        with open(hostpath,"r+") as file:
            contents=file.readlines()
            file.seek(0)
            for line in contents:
                if not any(websites in line for websites in website_list):
                    file.write(line)
            file.truncate()

    time.sleep(5)

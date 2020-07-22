import time
from datetime import datetime as dt
hosts_name = 'hosts'
hosts_dup = 'hosts_dup'
ban_website = ["www.youtube.com","www.facebook.com"]
redirect = '127.0.0.1'
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,12) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,15):
        with open(hosts_name,'r+') as file:
            content=file.read()
            for website in ban_website:
                if website in content:
                    pass
                else:
                    file.write(redirect+"       "+website+"\n")
    else:
        with open(hosts_name,'r+') as file:
            file.truncate(1050)
    time.sleep(5)

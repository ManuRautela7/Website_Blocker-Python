import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,10) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,19):
         # print("working hours")
          with open(hosts_path,'r+') as file:
              content=file.read()
              for website in website_list:
                  if website in content:
                      pass
                  else:
                       file.write(redirect+"  "+website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):# cheeck every word in the the list to be blocked if it is not present write it else pass
                    file.write(line)
            file.truncate()
        #print("fun hours")
    time.sleep(5)

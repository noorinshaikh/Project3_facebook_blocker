from datetime import datetime as dt
from time import sleep

websites=["www.facebook.com","facebook.com"]
loopback="127.0.0.1"

while True:
  if dt(dt.now().year,dt.now().month,dt.now().day,9) <= dt.now() <= dt(dt.now().year,dt.now().month,dt.now().day,20):
    print("work_hour")
    with open('hosts_copy',"r+") as file:
      hostfile = file.read()
      for site in websites:
        if site not in hostfile:
          file.write(loopback+" "+site+"\n")
        else:
          pass
  else:
    print("outside_working_hour")
    with open('hosts_copy',"r+") as file:
      hostlines = file.readlines()
      file.seek(0)
      for line in hostlines:
        if not any(site in line for site in websites):
          file.write(line)
      file.truncate() 
  sleep(5)

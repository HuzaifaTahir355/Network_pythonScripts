import pandas as pd
# import datetime
from datetime import datetime
from netmiko import ConnectHandler
from telnetlib import Telnet
import os

#getting data from excel file
ip_data = pd.read_excel("device_access_info.xlsx")

# getting current date
date_now = datetime.now().date()

#create new directory
os.mkdir(f"{date_now}")

# change directory to new, where we save our backup files
os.chdir(f'{date_now}')

# getting records form .xlsx file
for i in ip_data.index:
    print(i)
    # get record one by one
    data = ip_data.iloc[i]
    ip = data["IP_Addresses"]
    if data["accessing_protocols"] == "SSH":
        try:
            # pass info of devices
            cisco_router = {
                'device_type': 'cisco_ios',
                'host': data["IP_Addresses"],
                'username': data["username"],
                'password': str(data["password"]),
                'secret': str(data["enable_pass"]),
                'port': 22
            }

            ssh = ConnectHandler(**cisco_router)
            ssh.enable()
            print(ssh.find_prompt())
            device_name = ssh.find_prompt()
            ssh.send_command("terminal length 0\n")
            result = ssh.send_command("show running-config")
            # creating a file and store information in it
            with open(f"{device_name}({ip})_{datetime.now().date()}_backup.txt", "w") as f:
                f.write(result)

        except Exception as e:
            print(e)






    #under development for telnet also
    elif data["accessing_protocols"] == "telnet":
        try:
            telnet = Telnet(ip, timeout=5)
            # telnet.open(ip)

            telnet.read_until(b'sername')
            # print(telnet.read_until(b'sername').decode())
            telnet.write(data["username"].encode('ascii') + b'\n')

            telnet.read_until(b'assword')
            telnet.write(data["password"].encode('ascii') + b'\n')

            telnet.read_until(b'>', timeout=5)
            telnet.write(b'enable\n')
            telnet.write(b'data["enable_pass"]\n')

            telnet.read_until(b'#', timeout=5)
            telnet.write(b'terminal length 0\n')


        except Exception as e:
            # mgbx.showinfo("Access Denied", f"{e}")
            pass
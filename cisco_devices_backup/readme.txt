This script is to get backups of cisco network devices such as L3, L2 and MLS. The main thing is that SSH must be configured on the target devices.
please fill out the excel file with correct information. such as ip_add, SSH, username, password and enable password.
There is no limitation of number of device in it. U can get a large no of backup of devices as u want just by adding correct records in .xlsx file.  
This script will create a folder in current working directory and store all devices's backup in it.
Name of created directory is the date of that day.
Name of Files in this directory will be "devicename#(ip_add)_currentdate_backup".


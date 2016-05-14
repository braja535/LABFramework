import paramiko
import ConfigParser
import re
"""
Program to Grab Host WWNS ans well as alter them as in switches
these all details use the file where i kept my host/switch details with me
"""

#class get_host_login :
#    def __init__:
def hosts():
       config = ConfigParser.RawConfigParser()
       host_list = "wwns" #raw_input("Enter File Name where you have host list :")
       config.read(host_list)
       print config.sections()
       print config.sections()[0]
       print config.sections()[1]
       print config.sections()[2]
       print config.sections()[3]
       print config.sections().__len__()
       #while (config.section()):
       host_ip = config.get('Linux','host_ip')
       uname = config.get('Linux','username')
       passwd =config.get('Linux','Password')
       zonename = "".join(host_ip.split("."))
       #print host_ip,uname,passwd
       ssh_login = paramiko.SSHClient()
       ssh_login.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       ssh_login.connect(host_ip,username=uname,password=passwd)
       ssh_stdin,ssh_stdout,ssh_stderr = ssh_login.exec_command("cat /sys/class/fc_host/host*/port_name")
       ssh_login.close()
       host_wwns = []
       #with ssh_stdout.xreadlines() as f :
       for str in ssh_stdout.xreadlines():
              host_wwns.append(":".join(re.findall('..',str.lstrip("0x"))))
       return host_wwns
       print zonename
       #print ":".join(re.findall('..',host_wwns[0].lstrip("0x")))
       #print ":".join(re.findall('..',host_wwns[1].lstrip("0x")))
"""
Rough Work to get the WWNS in Switch output format this can be applicable to VPDIDs
*****************************************************************************************
# ":".join([str.lstrip("0x")[i:i+2] for i in range(0,len(str.lstrip("0x")),2)])         *
# print ":".join([str.lstrip("0x")[i:i+2] for i in range(0,len(str.lstrip("0x"))-1,2)]) *
# (":".join(re.findall('..',str.lstrip("0x"))))                                         *
*****************************************************************************************
"""



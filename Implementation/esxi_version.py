import os
import sys
import subprocess
#try :
#    from paramiko import paramiko,SSHClient,MissingHostKeyPolicy
#except:
#    print "Paramiko not installed please install"
#    sys.exit()

InputFile = raw_input("Enterfile name where you have your host list : ")
InFile = open(InputFile,'r')
OutFile = open(InputFile+"_output.txt",'w+')

for line in InFile.readlines():
    line = line.strip()
    #ssh = paramiko.SSHClient()
    #ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
    #ssh.connect(line,username='root',password='dangerous')
    #ssh_stdin,ssh_stdout,ssh_stderr = ssh.exec_command('vmware -v')
    #ssh -oStrictHostKeyChecking=no root@lqam4237  "vmware -v"
    #vmware_version = os.popen("ssh root@"+line+"")
    vmware_version_cmd = "sshpass -p \"dangerous\" ssh -o StrictHostKeyChecking=no root@"+line+"vmware -v"
    vmware_version = subprocess.call([vmware_version_cmd])
    powrpath_version = os.popen("rpowermt version host="+line+" username=root password=dangerous").read()
    #for vmware_version in ssh_stdout:
    OutFile.write(line+"\n"+vmware_version+"\n"+powrpath_version+"\n"+30*'*'+"\n\n\n")
    #ssh.close()
InFile.close()
OutFile.close()






'''

This Module intentionally created to perform the Tasks related to Switches

This will include the tasks  below.

    ** While initiating the script it will asks for minimum details of switches connected **
     *  store in classes a
     *
    1. Loging to the switch
#   2. search for recent logs forbidden in switches -- you can implement in Hosts
    3. generate the Logs
    4. Push it to the server

'''
import paramiko
import cPickle
import re
import string
import requests
import get_host_logins

#client = requests.Session()
#client.auth('admin','fabricx01')
#client.verify = False

class Switch :
    def __init__(self,ip="0.0.0.0",uname="admin",password="fabricx01"):
        self.IP = ip # raw_input("Enter Ip address of switch \t : ")
        self.uname = uname #raw_input("Enter Username of the switch \t :")
        self.password = password #raw_input("Enter Password for the switch for user  \t :")
    """
    Prints the details of switch Object
    """
    def switchdetails(self):
            print self.IP,self.uname,self.password
    """
    To get Switch Logins
    """
    def switch_login(self):
        sw_login = paramiko.SSHClient()
        sw_login.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sw_login.connect(hostname=str(self.IP),username=str(self.uname),password=str(self.password))
        return sw_login
    """
    This Function creates zone in switch
    """

    def zonecreation(self,wwns_list,zonename):
        wwns_string =""
        for i in range(0,wwns_list.__len__()):
            wwns_string += ":".join(re.findall('..',wwns_list[i].lstrip("0x")))+";"

        SwitchCommand = "zonecreate "+'\"'+zonename+'\"' + "," + '\"' + wwns_string.rstrip(";") + '\"'
        print SwitchCommand
        execution_command = self.switch_login()
        ssh_in,ssh_out,ssh_error = execution_command.exec_command("cfgtransshow")
        with ssh_out.xreadlines() as f:
            for line in f:
                print line,
                if "There is no outstanding zoning transactions" in line:
                    ssh_in,ssh_out,ssh_error = execution_command.exec_command(SwitchCommand)
                    print ssh_out
                    with ssh_out.xreadlines() as f , ssh_error as e :
                        for line in f:
                            print line,
                            print "This is error \n " , "---> " ,e
                    print "executing cfgadd Raja,anil command"
                    cfgadd_command = "cfgadd \"Raja\","+'\"'+zonename+'\"'
                    print cfgadd_command
                    ssh_in,ssh_out,ssh_error = execution_command.exec_command(cfgadd_command)
                    print "executed"
                    for line in ssh_out.xreadlines():
                        print line,"--> print normal output"

                    ssh_in,ssh_out,ssh_error = execution_command.exec_command("cfgsave")
                    ssh_in.write('yes\n')
                    ssh_in.flush()
                    print ssh_out.read()

                    execution_command.close()
                else :
                    print "there is a trasaction "

def main():
    obj1 = Switch("10.31.25.200")
    lst = get_host_logins.hosts()
    z_name = "anil"
    obj1.switchdetails()
    obj1.zonecreation(lst,z_name)
if __name__ == '__main__':
    main()


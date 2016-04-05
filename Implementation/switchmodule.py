'''

This Module intentionally created to perform the Tasks related to Switches

This will include the tasks  below.

    ** While initiating the script it will asks for minimum details of switches connected **
     *  store in classes a
     *
    1. Loging to the switch
#    2.search for recent logs forbidden in switches -- you can implement in Hosts
    3.generate the Logs
    4.Push it to the server

'''

import cPickle

class switchmodule() :
    def __init__(self):
        self.IP = raw_input("Enter Ip address of switch \t : ")
        self.uname = raw_input("Enter Username of the switch \t :")
        self.password = raw_input("Enter Password for the switch for user  \t :")
        self.switch_details = {'IP':self.IP, 'Uname':self.uname, 'passwd' :self.password}
    def __switchdetails(self):
        for key,value in self.switch_details.iteritems() :
            print key,value

def main() :
     obj1 = switchmodule()
     infobj = open("switchinfo","wb")
     cPickle.dump(obj1,infobj,2)
     infobj.close()
     obj1.__switchdetails()


if __name__ == '__main__':
    main()



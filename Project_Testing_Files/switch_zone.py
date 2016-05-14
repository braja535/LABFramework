import paramiko

class Brocade_Zone :
    def __init__(self,ip,uname,password):
        self.switch_uname = uname
        self.switch_passwd = password
        self.switch_ip = ip


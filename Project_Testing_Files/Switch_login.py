import paramiko
import sys


def main():
    SshCalling(sys.argv)
def FtpServerlogin(ServerName):
    Ftp = paramiko.SSHClient()
    FtpServer = raw_input("Enter FTP server")
    FtpUser = raw_input("Enter FTP user")
    FtpPassword = raw_input("Enter Password for FTP user ")
                                 #FtpDirectory  = raw_input("Enter the Directory Name :")
    Ftp.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    Ftp.connect(FtpServer,username = FtpUser,password = FtpPassword)
    FtpDirectory_Abs = "/tmp/"+ServerName
    Ftp.exec_command(str('mkadr '+ FtpDirectory_Abs))
    return FtpDirectory_Abs,FtpServer,FtpUser,FtpPassword

def SshCalling (server_params):
    Script,Server,Username,Password = server_params
    ssh = paramiko.SSHClient()
                                #ssh1 = paramiko.SSHClient()
                                #ssh1.connect(FtpServer,username= FtpUser,password = FtpPassword)
                                #FtpDirectory ="/tmp/"+str(Server)
                                #ssh1.exec_command(str('mkdir '+FtpDirectory))
    FtpDir,FtpServer,FtpUser,FtpPassword = FtpServerlogin(Server)
    paramiko_logfile = str(FtpDir) + "paramiko_logfile"
    paramiko.util.log_to_file(paramiko_logfile)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                                #in case server key is unknown
                                # we will be adding it automatically ti the list of known hosts
    ssh.connect(Server,username=Username,password=Password)
                                #ssh.exec_command('cd /tmp')
    SwitchCommand = str("bash --login -c 'supportsave'"+"-n "+"-u "+FtpUser+" -p "+FtpPassword+" -d "+FtpDir+" -l scp")
    ssh_stdin,ssh_stdout,ssh_stderr = ssh.exec_command(SwitchCommand)
    print "output",
    with ssh_stdout.xreadlines() as f:
    	for line in f:
    		print line,
                                # Reading output of the executed command
    error = ssh_stderr.read()
    print error
    ssh.close()
main()

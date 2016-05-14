import pexpect

class vplex():
  def __init__(self,ip):
          ip = self.ip
          uname ='service'
          passwd ='Mi@Dim7T'

  def vplex_sms_login(ip,uname,passwd):
      child = pexpect.spawn('ssh ' + uname + '@' + ip)
#          try:
#                  child.expect('Password*:')
#          except:
#                   child.expect('.*WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED.*.')
      i = child.expect(['.*WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED.*','Password*:','.*(yes/no)', pexpect4.EOF])
      if i == 0:
              print "Pleease remove host key in /home/user/.ssh/known_hosts:"
              pass
      elif i==1:
              child.expect('Password*:')
              child.sendline('Mi@Dim7T')
      else :
          child.sendline('yes')
      child.expect('service.*>')
      child.sendline('vplexcli')
      child.expect('Enter User Name:')
      child.sendline('service')
      child.expect('Password:')
      child.sendline('Mi@Dim7T')
      child.expect('VPlexcli.*>')
      child.sendline('ll /engines/**/ports')
      child.expect('VPlexcli.*>')
      print child.before()

def main() :
    v1_ip = raw_input("Please enter the VPLEX IP : ")
    v1 = vplex(v1_ip)
    v1.vplex_sms_login()

if __name__ == '__main__':
    main()

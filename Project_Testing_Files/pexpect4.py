import pexpect4

class vplex():
  def vplex_login(self,ip,uname,passwd):
          ip = self.ip
          uname ='service'
          passwd = 'Mi@Dim7T'
  def vplex_sms_login(self,ip,uname,paswd):
      child = pexpect4.spawn('ssh ' + uname + '@' + ip)
      i = child.expect(['.*WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED.*','Password*:','.*(yes/no)', pexpect4.EOF])
      if i == 0 :
              print "Pleease remove host key in /home/user/.ssh/known_hosts:"
              pass
      elif i == 1 :
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
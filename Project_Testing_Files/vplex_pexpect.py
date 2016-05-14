import pexpect
import subprocess

subprocess.pywintypes()


child = pexpect.spawn('p service@10.31.53.39')
child.expect('Password*:')
child.sendline('Mi@Dim8T')
child.sendline('vplexcli')
child.expect('Enter User Name:')
child.sendline('service')
child.expect('Password:')
child.sendline('Mi@DiT')
child.expect('VPlexcli.*>')
child.sendline('ll /engines/**/ports')
child.expect('VPlexcli.*>')
print child.before()

import wmi



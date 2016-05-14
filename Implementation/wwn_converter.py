#switch_128:admin> nodefind 50:06:01:65:3c:e0:20:1b
#Local:
# Type Pid    COS     PortName                NodeName                 SCR
# N    61e780;      3;50:06:01:65:3c:e0:20:1b;50:06:01:60:bc:e0:20:1b; 3
#    FC4s: FCP [DGC     LUNZ            0430]
#    Fabric Port Name: 2e:6f:00:05:1e:d1:b1:00
#    Permanent Port Name: 50:06:01:65:3c:e0:20:1b
#    Device type: Physical Unknown(initiator/target)
#    Port Index: 367
#    Share Area: Yes
#    Device Shared in Other AD: No
#    Redirect: No
#    Aliases: Security_Symm3185_CX84 Security_VplexCL2


#wwn_fname = raw_input("Enter where WWNs are reside : ")
#file = open(wwn_fname,"RW+")
#file.read().splitlines()#

import gzip
import tarfile
with tarfile.open("C:\Users\badan\Downloads\Pt-sms-install.tar",'rt') as f:
    text = f.read()

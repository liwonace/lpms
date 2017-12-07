#!/usr/bin/env python
from packages.cSSHManager import cSSHManager
''' Connect To Device info '''
user="lwa"
host="192.168.7.223"
passwd="lwa012"
port="22"
cSSH = cSSHManager(host, passwd, user, port)
result_bool, result_str = cSSH.mSSHConnect()
if result_bool == False:
    raise Exception('SSH Connection Failed')

#cSSH.mSendFile( SrcPath, DstPath )
RemoteCmd="ansible 192.168.7.223 -u lwa -k -m setup | grep ansible_distribution"		
so = cSSH.mRemoteCmd(RemoteCmd)

sostr = so.readlines()
print (sostr)
	
#with open(Path + FileName, "w") as f:                                                     
#    for line in sostr:                                                                    
#        f.write(line) 

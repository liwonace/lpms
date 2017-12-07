# -*- coding: utf-8 -*-

import paramiko
from scp import SCPClient

'''
     원격 ssh로 접속하는 접속하여 처리하는 클래스  
     원격ssh로 연결하여 파일 전송 및 명령어 실행의 기능을 수행한다. 
'''
class cSSHManager(object):
    c_ip = None
    c_password = None
    c_user = None
    c_ssh = None

    def __init__(self, ip, password, User, port=22, Timeout=1):
        self.c_ip = ip
        self.c_password = password
        self.c_user = User
        self.c_port = port 
        self.c_timeout = Timeout
    
    def __del__(self):
        if self.c_ssh:
            self.c_ssh.close()

    def mSSHConnect(self):
        try:
            self.c_ssh = paramiko.SSHClient()
            ''' connect ssh server '''
            self.c_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            #print self.c_port; print self.c_user; print self.c_password; print self.c_ip


            self.c_ssh.connect(self.c_ip, port=int(self.c_port), username=self.c_user, password=self.c_password, timeout=self.c_timeout)

            chan = self.c_ssh.invoke_shell(term='xt100')
            return True, "SSH connect success"
    
        except Exception as e:
            return False, e
    
    def mSetIPnPassword(self, ip, password):
        self.c_ip = ip
        self.c_password = password
    
    '''Send file to remote server '''
    def mSendFile(self, SrcFile, DstFile):
        if SrcFile is None:
            return False
        if DstFile is None:
            return False
        
        ''' get ssh session '''
        scp = SCPClient(self.c_ssh.get_transport())
        
        ''' send file '''
        scp.put(SrcFile, DstFile)
        return True
    
    def mRemoteCmd(self, cmd):
        ''' excute command at remoted device'''
        si, so, se = self.c_ssh.exec_command(cmd,  get_pty=True)
        return so

if __name__ == '__main__':
    try:
        cSSH = cSSHManager('IP', 'PW', 'root')
        ret, connect_result =  cSSH.mSSHConnect() 
        print(ret, end=' '); print(connect_result) 
        cmd = cSSH.mRemoteCmd('ls -al')
        print(cmd.readlines())
    except Exception as e:
        pass		
    finally:
        pass

    



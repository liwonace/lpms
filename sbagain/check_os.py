import subprocess
import time

# test code. 
# send command
# parse return value
# find os word

ip='192.168.7.223'
cmd='ansible ' + ip + ' -i /root/sbagain/ansible-dyninv-mysql/mysql.py -u root -m setup | grep ansible_distribution'
#result = subprocess.check_output ('ansible --help' , shell=True)
result = subprocess.check_output (cmd , shell=True, stderr=subprocess.STDOUT)

strresult = result.decode('utf-8')
#print(strresult)
lines = strresult.strip('\n').strip().split(',')
#print(lines)
osflag = 0

if -1 != lines[0].find("CentOS"):
    osflag = 1
   
elif -1 != lines[0].find("Ubuntu"):
    osflag = 2

elif -1 != lines[0].find("Fedora"):
    osflag = 3

elif -1 != lines[0].find("SUSE"):
    osflag = 4

else:
    print("Not supported OS")

print(lines[0])
print(osflag)	


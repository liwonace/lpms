import os
os.system('ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/ansible-python/yml/check-update.yml --limit 192.168.7.221')

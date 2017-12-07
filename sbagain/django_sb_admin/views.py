from django.shortcuts import render
from django_sb_admin.models import *
from django.db.models import Count
from django.db import connection
import socket
import os
import subprocess
import logging
import time 

def start(request):
    """Start page with a documentation.
    """
    return render(request, "django_sb_admin/start.html",
                  {"nav_active":"start"})

def dashboard(request):
    """Dashboard page.
    """
    return render(request, "django_sb_admin/sb_admin_dashboard.html",
                  {"nav_active":"dashboard"})

def charts(request):
    """Charts page.
    """
    return render(request, "django_sb_admin/sb_admin_charts.html",
                  {"nav_active":"charts"})
def tables(request):
    """Tables page.
    """
    return render(request, "django_sb_admin/sb_admin_tables.html",
                  {"nav_active":"tables"})
def forms(request):
    """Forms page.
    """
    return render(request, "django_sb_admin/sb_admin_forms.html",
                  {"nav_active":"forms"})
def bootstrap_elements(request):
    """Bootstrap elements page.
    """
    return render(request, "django_sb_admin/sb_admin_bootstrap_elements.html",
                  {"nav_active":"bootstrap_elements"})
def bootstrap_grid(request):
    """Bootstrap grid page.
    """
    return render(request, "django_sb_admin/sb_admin_bootstrap_grid.html",
                  {"nav_active":"bootstrap_grid"})
def dropdown(request):
    """Dropdown  page.
    """
    return render(request, "django_sb_admin/sb_admin_dropdown.html",
                  {"nav_active":"dropdown"})
def rtl_dashboard(request):
    """RTL Dashboard page.
    """
    return render(request, "django_sb_admin/sb_admin_rtl_dashboard.html",
                  {"nav_active":"rtl_dashboard"})

def blank(request):
    """Blank page.
    """
    return render(request, "django_sb_admin/sb_admin_blank.html",
                  {"nav_active":"blank"})

def check_os(ip):
    print("test check_os")
    # send command
    # parse return value
    # find os word

    ip=ip
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

    return osflag

def deviceinfo(request):
    logger = logging.getLogger(__name__)
    # count os type	
    centos_cnt = 0	
    ubuntu_cnt = 0	
    fedora_cnt = 0	
    suse_cnt = 0	
    cursor = connection.cursor()
    sql_str1 = 'SELECT COUNT( host ) FROM hostinfo WHERE distribution=\'CentOS\';'
    sql_str2 = 'SELECT COUNT( host ) FROM hostinfo WHERE distribution=\'Ubuntu\';'
    sql_str3 = 'SELECT COUNT( host ) FROM hostinfo WHERE distribution=\'Fedora\';'
    sql_str4 = 'SELECT COUNT( host ) FROM hostinfo WHERE distribution=\'openSUSE\';'
    #for p in Inventory.objects.raw('SELECT * FROM inventory;'):
    #    print(p)
    cursor.execute(sql_str1)
    centos_cnt_tuple = cursor.fetchall()
    #print(type(centos_cnt_tuple))
    #print(centos_cnt_tuple)
    for cnt in centos_cnt_tuple:
        centos_cnt = cnt[0]	
    print(centos_cnt)

    cursor.execute(sql_str2)
    ubuntu_cnt_tuple = cursor.fetchall()
    for cnt in ubuntu_cnt_tuple:
        ubuntu_cnt = cnt[0]	
    print(ubuntu_cnt)

    cursor.execute(sql_str3)
    fedora_cnt_tuple = cursor.fetchall()
    for cnt in fedora_cnt_tuple:
        fedora_cnt = cnt[0]	
    print(fedora_cnt)

    cursor.execute(sql_str4)
    suse_cnt_tuple = cursor.fetchall()
    for cnt in suse_cnt_tuple:
        suse_cnt = cnt[0]	
    print(suse_cnt)


    ##print(hostinfo_list)
    #group select   
    centos_host=""
    distribution=""
    host_list=[]
    if(request.POST.get('centos_details')):
        print("post centos")
        logger.info("centos_details")
        distribution="CentOS"

    if(request.POST.get('ubuntu_details')):
        print("post ubuntu")
        logger.info("ubuntu_details")
        distribution="Ubuntu"

    if(request.POST.get('fedora_details')):
        print("post fedora")
        logger.info("fedora_details")
        distribution="Fedora"

    if(request.POST.get('suse_details')):
        print("post suse")
        logger.info("suse_details")
        distribution="openSUSE"

    cursor = connection.cursor()
    sql_str1 = 'SELECT * FROM hostinfo WHERE distribution=\'' + distribution+ '\';'
    cursor.execute(sql_str1)
    host_tuple = cursor.fetchall()
    #print(host_tuple)
    host_list=list(host_tuple)
    print(host_list)

    #print(centos_host)
    #print(centos_distribution)
    #print(centos_list)

    if(request.POST.get('ubuntu_details')):
        print("post ubuntu")

    if(request.POST.get('fedora_details')):
        print("post fedora")

    if(request.POST.get('suse_details')):
        print("post suse")

    """Dashboard page.
    """
    return render(request, "django_sb_admin/sb_admin_deviceinfo.html",
                  {"nav_active":"deviceinfo", "centos_cnt": centos_cnt,
				  "ubuntu_cnt": ubuntu_cnt, "fedora_cnt": fedora_cnt,
				  "suse_cnt": suse_cnt, "host_list": host_tuple})

def inventory(request):
    logger = logging.getLogger(__name__)
    logger.info("test log")
    """Blank page.
    """
    import sys
    from packages.sshcopyid import SshCopy
    group_list = Group.objects.all()
    host_list = Host.objects.all()	
    #inventory_list = Inventory.objects.all()
    #print(inventory_list)
    cursor = connection.cursor()
    sql_str = 'SELECT * FROM inventory'	
    #sql_str = 'SELECT `group`, `host`, `hostname` FROM `inventory`;'

    #for p in Inventory.objects.raw('SELECT * FROM inventory;'):
    #    print(p)
    cursor.execute(sql_str)
    inventory_list = cursor.fetchall()
    print(host_list)
    print(type(host_list))
    print(inventory_list)
    print(type(inventory))
    for val in inventory_list:
        print(val[0], val[1], val[2]) 	
    #inventory_list = Inventory.objects.all()	
		
    #if(request.GET.get('mybtn')):
    #    print("mybtn!!")
        #cSSH = SshCopy(user, host,passwd, port)
        #cSSH = SshCopy(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    #    cSSH.send()
        		
    if(request.GET.get('selecthost')):
        selid=request.GET.get('selecthost')
        print(selid)
        #selectedhostid=Host.objects.filter(host=selid).values('variables')[0]	
        selectedhostid=Host.objects.filter(host=selid)
        #print(selectedhostid)
        for info in selectedhostid:
            print(info.variables)
            selectedport=info.variables

        #os.system("python")			
        ## 이런 식으로플레이ㅂ북을 정의 해서 			
        cmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/check-update.yml --limit '
        #cmd=cmd + '192.168.7.221'
        cmd=cmd + selid
        print(cmd)
        #os.system(cmd)	
        #os.system('ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/check-update.yml --limit 192.168.7.221')			
        
    if(request.GET.get('groupdevice')):
        print("groupdevice")
        groupp=request.GET.get('groupp')
        print(groupp)
	
    #group select	
    if(request.POST.get('groupselect')):
        logger.info("group select")

    if(request.POST.get('groupbtn')):
        print("groupbtn!!")
        #groupret = 0
        groupname=request.POST.get('groupname', False)
        print(groupname)
        jsonport='{}'
        sp=""
        try:
            Group.objects.create(name=groupname, variables=jsonport, enabled=1)
        except:
            print("except insert db")

        return render(request, 'django_sb_admin/sb_admin_inventory.html',
            {"group_list": group_list, "host_list": host_list,
			"inventory_list": inventory_list})

    ## change process with post button submit
    #if request.method == 'POST':
    if(request.POST.get('submitbtn')):
        # check vaild IP or not	  
        ip=request.POST.get('ip', False)
        session=request.POST.get('session', False)
        sshuser=request.POST.get('sshuser', False)
        try:
            if(ip == False):
                return render(request, 'django_sb_admin/sb_admin_inventory.html',
                {"group_list": group_list, "host_list": host_list})
            socket.inet_aton(ip)
        except socket.error:
            print("invalid IP") 		
            #return render(request, "django_sb_admin/sb_admin_inventory.html",
            #      {"nav_active":"blank"})
            return render(request, 'django_sb_admin/sb_admin_inventory.html',
                {"group_list": group_list, "host_list":host_list, "inventory_list": inventory_list})
        		
        port=request.POST.get('port', False)
        print(port)	    
        if port == False:
            print(port) 		
            print("1") 		
            jsonport= '{X}'
        elif port != "" and port != False:
            jsonport= '{"ansible_ssh_port": "' + port  +'"}'    	   
            print(jsonport) 		
            print("2") 		
        else: 
            jsonport= '{}'
            print("3") 		
			
        print(sshuser)
        sshpw=request.POST.get('sshpw', False)
        # print(sshpw)
        # Input ssh key
        #cSSH = SshCopy(user, host,passwd, port)
        print("start ssh copy")	
        print(sshuser, ip, sshpw, port) 		
        cSSH = SshCopy(sshuser, ip, sshpw, port)
        try:
            cSSH.send()
        except:
            print("except ssh key send")	
        #print(returncopy)	
        try:
            Host.objects.create(host=ip, hostname=session, variables=jsonport,
				enabled=1)
            print("4") 		
            oneofhostid=Host.objects.filter(host=ip).values('id')[0]	
            print("5") 		
            groupname=request.POST.get('group', False)	
            print("6") 		
            oneofgroupid=Group.objects.filter(name=groupname).values('id')[0]
            print("7") 		
            Hostgroups.objects.create(host_id=oneofhostid['id'],
				group_id=oneofgroupid['id'])
            print("8") 		
        except:
            print("except insert db")
        
        try:			
            #cmd='ansible ' + ip + ' -i /root/sbagain/ansible-dyninv-mysql/mysql.py -u root -m setup | grep ansible_distribution'
            print("OS Code: ")
            #os_code = check_os(ip)
    
            # send command
            # parse return value
            # find os word

            #ip='192.168.7.223'
            cmd='ansible ' + ip + ' -i /root/sbagain/ansible-dyninv-mysql/mysql.py -u root -m setup | grep ansible_distribution'
            #result = subprocess.check_output ('ansible --help' , shell=True)
            result = subprocess.check_output (cmd , shell=True, stderr=subprocess.STDOUT)
            print("check_os")
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

            elif -1 != lines[0].find("openSUSE"):
                osflag = 4

            else:
                print("Not supported OS")
            
            print(lines[0])
            print(osflag)
        except:
            print("check os except")

            # print(os_code)			
            # os.system(cmd)	
            # result = subprocess.check_output(cmd, shell=True)	
            # result = subprocess.check_output (cmd , shell=True)
            # print(result)
        # DB에서 각host id와 groupid를 가져와서 입력하여야 한다.	
        #oneofgroupid=Group.objects.filter(name=groupname).values('id').annotate(num=Count('id'))
        #oneofgroupid=Group.objects.annotate(num=Count('id'))
        #oneofhostid=Host.objects.filter(host=ip).values('id')	
        #oneofhostid=Host.objects.annotate(numhost=Count('id'))
        #return render(request, "django_sb_admin/sb_admin_inventory.html",
        #         {"nav_active":"blank"})
        return render(request, 'django_sb_admin/sb_admin_inventory.html',
            {"group_list": group_list, "host_list": host_list, "some_flag":
			True, "inventory_list": inventory_list})
	
    """ 
    elif request.method == 'GET':
        group_list = Group.objects.all()
        host_list = Host.objects.all()	

        return render(request, 'django_sb_admin/sb_admin_inventory.html',
            {"group_list": group_list, "host_list": host_list})
    """
    #return render(request, "django_sb_admin/sb_admin_inventory.html",                         
    #              {"nav_active":"blank"})
    return render(request, 'django_sb_admin/sb_admin_inventory.html',
            {"group_list": group_list, "host_list": host_list, "inventory_list": inventory_list})
    #return render(request, 'django_sb_admin/sb_admin_inventory.html',
    #        {"group_list": group_list, "host_list": host_list })

	
def jquery(request):

    return render(request, "django_sb_admin/sb_jquery.html",
                  {"nav_active":"blank"})
def playbook(request):
    """playbook page.
    """
    import sys
    from packages.sshcopyid import SshCopy
    group_list = Group.objects.all()
    host_list = Host.objects.all()	
    logger = logging.getLogger(__name__)
    	
    #inventory_list = inventory.objects.all() 

    if(request.GET.get('selecthost')):
        print("select host")
    if(request.GET.get('osbtn')):
        #request.GET.get('selecthost')
        logger.info("os button!")
        selid=request.GET.get('selecthost')
        
        #selectedhostid=Host.objects.filter(host=selid)

        cmd='ansible ' + selid + ' -i /root/sbagain/ansible-dyninv-mysql/mysql.py -u root -m setup | grep ansible_distribution'
        osflag = 0
        osstr="Not supported"
        lines= [0,0,0,0,0]
        try:
            result = subprocess.check_output (cmd , shell=True, stderr=subprocess.STDOUT)
            print("check_os")
            strresult = result.decode('utf-8')
            #print(strresult)
            lines = strresult.strip('\n').strip().split(',')
            #print(lines)

            if -1 != lines[0].find("CentOS"):
                osflag = 1
                osstr="CentOS"

            elif -1 != lines[0].find("Ubuntu"):
                osflag = 2
                osstr="Ubuntu"

            elif -1 != lines[0].find("Fedora"):
                osflag = 3
                osstr="Fedora"

            elif -1 != lines[0].find("openSUSE"):
                osflag = 4
                osstr="openSUSE"

            else:
                print("Not supported OS")

            print(lines[0])
	   
            # print(osflag)
        except:
            print("check os except")
        
        print(cmd)
        # print(type(osflag))

        # make str for ui return value
        retosstr = ""	    
        if osflag == 0:
            retosstr = str(lines[0]) + ", Not supported OS"	  
        elif osflag != 0:
            retosstr = str(lines[0]) + ", Open source OS"	  
        else: 
            resosstr = "Check OS error"	
			
        # insert to db
        try:
            Hostinfo.objects.create(host=selid, distribution=osstr)

        except:
            Hostinfo.objects.filter(host=selid).update(distribution=osstr)
            print("update hostinfo")
        
        # disable ip when not support os
        if osflag == 0: 
            Host.objects.filter(host=selid).update(enabled=0)
          

        return render(request, 'django_sb_admin/sb_admin_playbook.html',
				{"host_list": host_list, "distribution": retosstr, })          				

    if(request.GET.get('reservationbtn')):
        stdmsg=""
        pkgcmd=""
        strresult=""
        selid=""
        #runhost=request.POST.get('selecthost', False)
        print("reservebtn!!")
        
        selid=request.GET.get('selecthost')
        print(selid)
        if selid== None:
            strresult="didn't select host"
            return render(request, 'django_sb_admin/sb_admin_playbook.html', {"group_list": group_list, "host_list": host_list, "stdmsg": stdmsg, "strresult": strresult})

        try:
            os=Hostinfo.objects.filter(host=selid).values('distribution')[0]
            #print(os)
            #print(type(os))
            if os['distribution'] == "CentOS":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/patch/yum_patch.yml --limit '
            elif os['distribution'] == "Ubuntu":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/patch/apt_patch.yml --limit '
		
            elif os['distribution'] == "Fedora":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/patch/yum_patch.yml --limit '

            elif os['distribution'] == "openSUSE":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/patch/zypper_patch.yml --limit '

            else: 
               print("Not support os")

        except:
            print("except value")		
        #print(selectedhostid)

        #cmd=cmd + '192.168.7.221'
        pkgcmd=pkgcmd + selid
        try:
            pkgresult = subprocess.check_output (pkgcmd , shell=True, stderr=subprocess.STDOUT)
            print("after reservation")		
            strresult = pkgresult.decode('utf-8')
            print("reservation result")		
            print(strresult)
            stdmsg="Reservation Success"
             	        
        #cSSH = SshCopy(user, host,passwd, port)
        #cSSH = SshCopy(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        #cSSH.send()
        except:
            stdmsg="Reservation Patch Exception"
            print("reservation patch fail")	

        return render(request, 'django_sb_admin/sb_admin_playbook.html', {"group_list": group_list, "host_list": host_list, "stdmsg": stdmsg, "strresult": strresult})


    # Refresh package		
    if(request.GET.get('pkgbtn')):
        pkgcmd=""

        print("package button")
        selid=request.GET.get('selecthost')
        print(selid)
        if selid== None:
            strresult="didn't select host"
            return render(request, 'django_sb_admin/sb_admin_playbook.html', {"group_list": group_list, "host_list": host_list, "stdmsg": stdmsg, "strresult": strresult})
        #selectedhostid=Host.objects.filter(host=selid).values('variables')[0]	
        selectedhostid=Host.objects.filter(host=selid)
        try:
            os=Hostinfo.objects.filter(host=selid).values('distribution')[0]
            print(os)
            print(type(os))
            if os['distribution'] == "CentOS":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/repo/centos_repo.yml --limit '
            elif os['distribution'] == "Ubuntu":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/repo/ubuntu_repo.yml --limit '
		
            elif os['distribution'] == "Fedora":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/repo/fedora_repo.yml --limit '

            elif os['distribution'] == "openSUSE":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/repo/suse_repo.yml --limit '

            else: 
               print("Not support os")
        except:
            print("except value")		
        #print(selectedhostid)
        for info in selectedhostid:
            print(info.variables)
            selectedport=info.variables

        #cmd=cmd + '192.168.7.221'
        pkgcmd=pkgcmd + selid
        try:
            print("add repo")		
            pkgresult = subprocess.check_output (pkgcmd , shell=True, stderr=subprocess.STDOUT)
            print("after add repo")		
            strresult = pkgresult.decode('utf-8')
            print("pkgresult")		
            print(strresult)		
        #cSSH = SshCopy(user, host,passwd, port)
        #cSSH = SshCopy(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        #cSSH.send()
        except:
            print("refresh package fail")		


    # Check update test
    if(request.GET.get('checkupdatebtn')):
        stdmsg = ""
        strresult = ""
        #selectedhostid=Host.objects.filter(host=selid)
        pkgcmd=""
        print("check update")
        selid=request.GET.get('selecthost')
        #pkgname=request.GET.get('pkgname')

        print(selid)
        if selid== None:
            strresult="didn't select host"
            return render(request, 'django_sb_admin/sb_admin_playbook.html', {"group_list": group_list, "host_list": host_list, "stdmsg": stdmsg, "strresult": strresult})
        print("pkgname")
        #print(pkgname)
        #selectedhostid=Host.objects.filter(host=selid).values('variables')[0]	
        #selectedhostid=Host.objects.filter(host=selid)
        try:
            os=Hostinfo.objects.filter(host=selid).values('distribution')[0]
            print(os)
            print(type(os))
            if os['distribution'] == "CentOS":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/list_compare/centos_check-update.yml --limit '
            elif os['distribution'] == "Ubuntu":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/repo/ubuntu_repo.yml --limit '
		
            elif os['distribution'] == "Fedora":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/repo/fedora_repo.yml --limit '

            elif os['distribution'] == "openSUSE":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/repo/suse_repo.yml --limit '

            else: 
               print("Not support os")
        except:
            print("except value")		

        pkgcmd=pkgcmd + selid
        try:
            print("check-update pkg")		
            pkgresult = subprocess.check_output (pkgcmd , shell=True, stderr=subprocess.STDOUT)
            print("after check-update pkg")		
            strresult = pkgresult.decode('utf-8')
            print("pkgresult")		
            print(strresult)		
            stdmsg = "Success check update"
        #cSSH = SshCopy(user, host,passwd, port)
        #cSSH = SshCopy(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        #cSSH.send()
        except:
            stdmsg = "check update fail"
            print("download package fail")		

        return render(request, 'django_sb_admin/sb_admin_playbook.html',
				{"host_list": host_list, "stdmsg": stdmsg, "strresult": strresult})          				

    if(request.GET.get('comparepkgverbtn')):
        stdmsg = ""
        strresult= ""
        pkgcmd=""
        print("compare package version button")
        #selid=request.GET.get('optionsRadiosInline')
        selid=request.GET.get('selecthost')
        if selid== None:
            strresult="didn't select host"
            return render(request, 'django_sb_admin/sb_admin_playbook.html', {"group_list": group_list, "host_list": host_list, "stdmsg": stdmsg, "strresult": strresult})
        pkgname=request.GET.get('pkgname')
        #selectedhostid=Host.objects.filter(host=selid)
        print(selid)
        print(pkgname)
        #selectedhostid=Host.objects.filter(host=selid)
        try:
            os=Hostinfo.objects.filter(host=selid).values('distribution')[0]
            if os['distribution'] == "CentOS":
                pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/list_compare/centos_compare_pkg.yml --limit '
                # pkgcmd='rpm -qa | grep ' + pkgname + ';yum check-update | grep '+ pkgname
                print(pkgcmd)

            elif os['distribution'] == "Ubuntu":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/repo/ubuntu_repo.yml --limit '
		
            elif os['distribution'] == "Fedora":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/repo/fedora_repo.yml --limit '

            elif os['distribution'] == "openSUSE":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/repo/suse_repo.yml --limit '

            else: 
               print("Not support os")
        except:
            print("except value")		

        pkgcmd=pkgcmd + selid
        try:
            print("compare package version")		
            pkgresult = subprocess.check_output (pkgcmd , shell=True, stderr=subprocess.STDOUT)
            print("after compare pkg")		
            strresult = pkgresult.decode('utf-8')
            print("pkgresult")		
            print(strresult)		
            stdmsg = "Compare package success"
        #cSSH = SshCopy(user, host,passwd, port)
        #cSSH = SshCopy(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        #cSSH.send()
        except:
            print("Compare package fail")		
            stdmsg = "Compare package fail"

        return render(request, 'django_sb_admin/sb_admin_playbook.html',
				{"host_list": host_list, "stdmsg": stdmsg, "strresult": strresult})          				

    # Download package		
    if(request.GET.get('downpkgbtn')):
        pkgcmd=""

        print("download package button")
        selid=request.GET.get('selecthost')
        print(selid)
        #selectedhostid=Host.objects.filter(host=selid).values('variables')[0]	
        selectedhostid=Host.objects.filter(host=selid)
        try:
            os=Hostinfo.objects.filter(host=selid).values('distribution')[0]
            ##print(os)
            if os['distribution'] == "CentOS":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/pkg/yum_downloadonly.yml --limit '

            elif os['distribution'] == "Ubuntu":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/pkg/apt_downloadonly.yml --limit '
		
            elif os['distribution'] == "Fedora":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/pkg/yum_downloadonly.yml --limit '

            elif os['distribution'] == "openSUSE":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/pkg/zypper_downloadonly.yml --limit '

            else: 
               print("Not support os")
        except:
            print("except value")		

        #cmd=cmd + '192.168.7.221'
        pkgcmd=pkgcmd + selid
        try:
            print("download pkg")		
            pkgresult = subprocess.check_output (pkgcmd , shell=True, stderr=subprocess.STDOUT)
            print("after download pkg")		
            strresult = pkgresult.decode('utf-8')
            print("pkgresult")		
            print(strresult)		
        #cSSH = SshCopy(user, host,passwd, port)
        #cSSH = SshCopy(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        #cSSH.send()
        except:
            print("download package fail")		
    
    if(request.GET.get('patchbtn')):
        start_time=time.time()		
        print("patch start time", start_time)		
        stdmsg=""
        strresult=""
        pkgcmd=""
        #runhost=request.POST.get('selecthost', False)
        print("patchbtn!!")
        #print(runhost)
        selid=request.GET.get('selecthost')
        print(selid)
        if selid== None:
            strresult="didn't select host"
            return render(request, 'django_sb_admin/sb_admin_playbook.html', {"group_list": group_list, "host_list": host_list, "stdmsg": stdmsg, "strresult": strresult})
        #selectedhostid=Host.objects.filter(host=selid).values('variables')[0]	
        #selectedhostid=Host.objects.filter(host=selid)
        try:
            os=Hostinfo.objects.filter(host=selid).values('distribution')[0]
            #print(os)
            #print(type(os))
            if os['distribution'] == "CentOS":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/patch/yum_patch.yml --limit '
            elif os['distribution'] == "Ubuntu":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/patch/apt_patch.yml --limit '
		
            elif os['distribution'] == "Fedora":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/patch/yum_patch.yml --limit '

            elif os['distribution'] == "openSUSE":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/patch/zypper_patch.yml --limit '

            else: 
               print("Not support os")

        except:
            print("except value")		
        #print(selectedhostid)

        #cmd=cmd + '192.168.7.221'
        pkgcmd=pkgcmd + selid
        try:
            pkgresult = subprocess.check_output (pkgcmd , shell=True, stderr=subprocess.STDOUT)
            print("after patch")		
            strresult = pkgresult.decode('utf-8')
            print("patch result")		
            print(strresult)
            stdmsg="Patch Success"
             	        
        #cSSH = SshCopy(user, host,passwd, port)
        #cSSH = SshCopy(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        #cSSH.send()
        except:
            stdmsg="Patch Excepttion"
            print("refresh package fail")		
        running_time = time.time() - start_time
        #print(running_time)	    
        print("--- patch time: %s seconds ---" %(time.time() - start_time))			
        return render(request, 'django_sb_admin/sb_admin_playbook.html', {"group_list": group_list, "host_list": host_list, "stdmsg": stdmsg, "strresult": strresult})


		

    if(request.GET.get('restorebtn')):
        start_time=time.time()		
        print("restore start time", start_time)		
        pkgcmd=""
        #runhost=request.POST.get('selecthost', False)
        print("restorebtn!!")
        #print(runhost)
        selid=request.GET.get('selecthost')
        print(selid)
        try:
            os=Hostinfo.objects.filter(host=selid).values('distribution')[0]
            print(os)
            #print(type(os))
            if os['distribution'] == "CentOS":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/restore/yum_restore.yml --limit '
            elif os['distribution'] == "Ubuntu":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/restore/apt_restore.yml --limit '
		
            elif os['distribution'] == "Fedora":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/restore/yum_restore.yml --limit '

            elif os['distribution'] == "openSUSE":
               pkgcmd='ansible-playbook -i /root/sbagain/ansible-dyninv-mysql/mysql.py ~/sbagain/yml/patch/zypper_restore.yml --limit '

            else: 
               print("Not support os")

        except:
            print("except value")		
        #print(selectedhostid)

        #cmd=cmd + '192.168.7.221'
        pkgcmd=pkgcmd + selid
        try:
            pkgresult = subprocess.check_output (pkgcmd , shell=True, stderr=subprocess.STDOUT)
            print("after restore")		
            strresult = pkgresult.decode('utf-8')
            print("restore result")		
            print(strresult)		
        #cSSH = SshCopy(user, host,passwd, port)
        #cSSH = SshCopy(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        #cSSH.send()
        except:
            print("restore fail")		
        running_time = time.time() - start_time
        print("--- restore time: %s seconds ---" %(time.time() -start_time))
        return render(request, 'django_sb_admin/sb_admin_playbook.html',
            {"group_list": group_list, "host_list": host_list})

        		
    return render(request, 'django_sb_admin/sb_admin_playbook.html',
            {"group_list": group_list, "host_list": host_list})

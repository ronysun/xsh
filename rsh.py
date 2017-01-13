#coding:utf-8

import sys
import os
import paramiko
import csv
import interactive

listFile = 'hostListFile'


def addHostToList():
    hostName = raw_input("input the hostname:")
    hostIp = raw_input("host ip:")
    hostLoginUser = raw_input("login user:")
    hostLoginPWD = raw_input("login password:")
    fieldnames = ['name',  'ip', 'loginUser', 'loginPWD']
    if os.path.exists(listFile):
        File = file(listFile,'a')
        hostListFile = csv.DictWriter(File, fieldnames=fieldnames)
        hostListFile.writerow({'name':hostName,'ip':hostIp, 'loginUser':hostLoginUser, 'loginPWD':hostLoginPWD })
    
    else :
        File = file(listFile,'w')
        hostListFile = csv.DictWriter(File, fieldnames=fieldnames)
        hostListFile.writeheader()
        hostListFile.writerow({'name':hostName,'ip':hostIp, 'loginUser':hostLoginUser, 'loginPWD':hostLoginPWD })
        File.close
    return 

def deletHost():
    pass

def connectHost(hostInfo):
    print host
    ssh = paramiko.client.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostInfo['ip'], username=hostInfo['loginUser'], password=hostInfo['loginPWD'])
    channel = ssh.invoke_shell()
    interactive.interactive_shell(channel)
    channel.close
    ssh.close  
    return 



if __name__ == '__main__':
    if len(sys.argv) == 1:
        print "input pramise!\r"
    else:
        parame = sys.argv[1]
        if parame == "list":
            hostListFile = open(listFile, 'rd')
            for host in csv.DictReader(hostListFile):
                print (host['name']+",ip address:"+host['ip'])
            hostListFile.close

        elif parame == "add":
            addHostToList()

        elif parame == "del":
            deletHost()

        else:
            hostListFile = open(listFile, 'rd')
            for host in csv.DictReader(hostListFile):
                if parame == host['name'] :
                   connectHost(host)

                else:
                    print "there is no this host!\r"
                    print "host list:\r"
                    print (host['name']+",ip address:"+host['ip'])


            # connectHost(parame)





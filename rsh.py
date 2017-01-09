#coding:utf-8

import sys
import paramiko
import pickle


def hostList():
    pass

def saveList():
    hostDict = {}
    hostDict['name'] = raw_input("please input the hostname:")
    hostDict['ip'] = raw_input("host ip:")
    hostDict['loginUser'] = raw_input("login user:")
    hostDict['loginPWD'] = raw_input("login password:")
    hostListFile = open('hostListFile', 'a')
    pickle.dump(hostDict, hostListFile)
    hostListFile.close
    return

def connectHost(hostDict):
    ssh = paramiko.SSHClient()
    ssh.connect(hostDict['ip'], 22, hostDict['loginUser'], hostDict['loginPWD'])

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print "input pramise!\r"
    else:
        parame = sys.argv[1]
        if parame == "list":
            hostList_file = open('hostListFile', 'rd')
            for host in pickle.Unpickler.load_dict(hostList_file):
                print host

        elif parame == "save":
            saveList()

        else:
            pass
            # connectHost(parame)





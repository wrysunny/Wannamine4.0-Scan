#!-*- coding:utf-8 -*-
import os.path
from pywinservicemanager.WindowsServiceConfigurationManager import ServiceExists
_author_ = "wrysunny"
# u"\u5764\u6cf0\uff08\u006b\u0075\u006e\u0074\u0079\u0065\u002e\u0063\u006f\u006d\uff09\u0049\u0054\u4e0d\u914d\u5408\u0020\u0066\u0075\u0063\u006b"


def verify():
    print u"\u68c0\u6d4b\u662f\u5426\u5df2\u4e2d\u6bd2\n"
    flag = False
    if os.path.exists("C:/Windows/NetworkDistribution/"):
        flag = True
    elif os.path.exists("C:/Windows/System32/rdpkax.xsl"):
        flag = True
    elif os.path.exists("C:/Windows/System32/dllhostex.exe"):
        flag = True
    elif os.path.exists("C:/Windows/SysWOW64/dllhostex.exe"):
        flag = True
    print flag,"\n"
    if flag:
        print u"\u5df2\u4e2d\u6bd2\n"
        print u"\u8bf7\u68c0\u67e5\u4ee5\u4e0b\u6587\u4ef6\uff1a\n"
        print "C:/Windows/NetworkDistribution/\n"
        print "C:/Windows/System32/rdpkax.xsl\n"
        print "C:/Windows/System32/dllhostex.exe\n"
        print "C:/Windows/SysWOW64/dllhostex.exe\n"
    else:
        print u"\u672a\u53d1\u73b0\n"

def servicename():
    string1 = ["Windows","Microsoft","Network","Remote","Function","Secure","Application"]
    string2 = ["Update","Time","NetBIOS","RPC","Protocol","SSDP","UPnP"]
    string3 = ["Service","Host","Client","Event","Manager","Helper","System"]
    s_d_name = []
    for x in string1:
        for y in string2:
            for z in string3:
                s_d_name.append(x+y+z)
    #print len(s_d_name) 
    return s_d_name

def scanservice(s_d_name):
    flag = False
    for i in s_d_name:
        if ServiceExists(i):
            flag = True
        if flag:
            print u"\u53d1\u73b0\u670d\u52a1\u540d\uff1a",i

def scandll(s_d_name):
    # print u"\u68c0\u6d4b\u662f\u5426\u5b58\u5728\u75c5\u6bd2\u0044\u004c\u004c\n"
    for i in s_d_name:
        if os.path.exists("C:/Windows/System32/"+i+".dll"):
            print u"\u53d1\u73b0\uff1a","C:/Windows/System32/"+i+".dll"
        if os.path.exists("C:/Windows/SysWOW64/"+i+".dll"):
            print u"\u53d1\u73b0\uff1a","C:/Windows/SysWOW64/"+i+".dll"

if __name__ == "__main__":
    # scan 
    verify()
    # scan service
    scanservice(servicename())
    # scan dll
    scandll(servicename())

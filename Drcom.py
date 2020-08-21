import sys
from urllib import urlencode
from urllib2 import urlopen

'''
=================Drcom.py======================
NOTION: When you don't use it, LOGOUT on time!

Usage:
	Login:   python2 Drcom.py login
	Logout:  Python2 Drcom.py logout
=============================================== 
'''

username = ""
upass = ""
LOGIN = "https://drcom.szu.edu.cn/a70.htm"
LOGOUT = "https://drcom.szu.edu.cn/F.htm"
 
def post(url, data=None):
    if data:
        data = urlencode(data)
    response = urlopen(url, data)
    return response.read()
 
def login():
    data={}
    data["DDDDD"] = username
    data["upass"] = upass
    data["R1"] = 0
    data["R2"] = ''
    data["R6"] = 0
    data["para"] = 00
    data["0MKKey"] = 123456
    post(LOGIN, data)
    pass
 
def logout():
    post(LOGOUT)
 
def main(argv):
    if argv[0] in ('login','in','i'):
        login()
    elif argv[0] in ('logout','out','o'):
        logout()
    pass
 
if __name__ == '__main__':
    main(sys.argv[1:]);


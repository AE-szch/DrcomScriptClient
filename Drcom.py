'''
=================Drcom.py======================
NOTION: When you don't use it, LOGOUT on time!
Version 2.0:
 - Add python 3.x support
Usage:
	Login:   python Drcom.py login
	Logout:  python Drcom.py logout
=============================================== 
'''
import os
import sys
PY2 = True if sys.version_info.major == 2 else False
if PY2:
    from urllib import urlencode
    from urllib2 import urlopen
else:
    from urllib.parse import urlencode
    from urllib.request import urlopen

username = ""
upass = ""
LOGIN = "https://drcom.szu.edu.cn/a70.htm"
LOGOUT = "https://drcom.szu.edu.cn/F.htm"

def post(url, data=None):
    if data:
        data = urlencode(data) if PY2 else urlencode(data).encode('utf-8')
    return urlopen(url, data)

def login():
    data = {}
    data["DDDDD"] = username
    data["upass"] = upass
    data["R1"] = 0
    data["R2"] = ''
    data["R6"] = 0
    data["para"] = 80
    data["0MKKey"] = 123456
    return( post( LOGIN, data ) )

def logout():
    return( post( LOGOUT ) )

def checkPing(time=4):
    os.system( 'timeout %d ping www.baidu.com' % time )

def drcom_main(argv, response=None):
    if argv[0] in ('--help', '-h'):
        print( "\nUsage:" )
        print( "\tLogin:\t\tpython Drcom.py login" )
        print( "\tLogout:\t\tpython Drcom.py logout" )
        print( "\nArguments:" )
        print( "\tlogin/in/i:\tLogin Drcom" )
        print( "\tlogout/out/o:\tLogout Drcom" )
        print( "\t--help/-h:\tDrcom Usage Helper\n" )
    elif argv[0] in ('login', 'in', 'i'):
        operation = 'login'
        response = login()
        print( "Python Version : %s\nOperation : %s\n" % ( sys.version, operation ) )
        if response.getcode() == 200:
            print( "Status : \033[1;32;40m%s\033[0m" % response.getcode() )
        else:
            print( "Status : \033[1;31;40m%s\033[0m" % response.getcode() )
        print( response.info() )
        checkPing(5)
    elif argv[0] in ('logout', 'out', 'o'):
        operation = 'logout'
        response = logout()
        print( "Python Version : %s\nOperation : %s\n" % ( sys.version, operation ) )
        if response.getcode() == 200:
            print( "Status : \033[1;32;40m%s\033[0m" % response.getcode() )
        else:
            print( "Status : \033[1;31;40m%s\033[0m" % response.getcode() )
        print( response.info() )
        checkPing(1)
    else:
        print( "Drcom Error: The Operate does not exist.\nSpecift --help or -h for usage." )

if __name__ == '__main__':
    if len(sys.argv) > 1:
        drcom_main( sys.argv[1:] )
    else:
        print( "Drcom Option Problem.\nSpecift --help or -h for usage." )
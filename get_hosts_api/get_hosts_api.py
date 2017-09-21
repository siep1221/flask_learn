#!/usr/bin/env python3
# __author__ : peng.xu

import urllib
import requests
import json
from bs4 import BeautifulSoup
from flask import Flask
app = Flask(__name__)

@app.route('/')
def GetHosts():
    s = requests.Session()
    data={
            'os_username':"peng.xu",
            'os_password':"#xxxx#",
        }

    s.post("http://wiki.xxx.com/login.action",data=data)

    r = s.get("http://wiki.xxx.com/pages/viewpage.action?pageId=286206")
    soup = BeautifulSoup(r.content,'html.parser')

    AllTr = soup.find_all('td')

    name = []
    status = []
    ip = []
    a,b,c = 1,2,3
    while 1:
        for index,ii in enumerate(AllTr):
            if (index+1) == a:
                name.append(ii.string)
                a += 7
            elif (index+1) == b:
                status.append(ii.string)
                b += 7
            elif (index)+1 == c:
                ip.append(ii.string)
                c+=7
        else:
            break

    # host_list = dict(map(lambda x,y,z:[x,y,z],name,status,ip))
    host_list = dict(zip(name,zip(ip,status)))
    res = json.dumps(host_list)
    return res.encode('utf-8')

if __name__=='__main__':
    app.run(host='0.0.0.0',port='9851')

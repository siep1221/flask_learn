#!/usr/bin/env python3
# __author__ : peng.xu

import requests
import json


res = requests.get('http://110.109.98.51:9851')
res_data = json.loads(a1.text)

host_file = open('ops_host_list','w')
ip_file = open('ops_ip_list','w')
hosts_all = open('ops_all_host','w')
for k,v in res_data.items():
    hosts_all.write(k.encode('utf-8')+"\t"+v[1].encode('utf-8')+"\n")
    if v[1] == "ok":
        host_file.write(k.encode('utf-8')+"\n")
        ip_file.write(v[0].encode('utf-8')+"\n")
host_file.close()
ip_file.close()
hosts_all.close()

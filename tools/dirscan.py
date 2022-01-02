#!/usr/bin/env python

import requests
import concurrent.futures
import urllib3
import collections
from .check import check_site


class Enum:
    def __init__(self, ip, ext, retries, login, headers, cookies):
        self.ip = ip
        self.ext = ext
        self.res = check_site()
        self.retries = retries
        self.login = login
        self.headers = headers
        self.cookies = cookies
        self.row_format = '{:<30}{:<100}{:<20}'

    def dirScan(self, Dir):
        site = f"{self.ip}/{Dir}"
        response = self.res.check_site(site, self.retries, self.login, self.headers, self.cookies)
        if response[1] != 404:
            if response[0]==None:
                print("{:<50}{:>40}".format("[+] "+site+"    [Status code:"+str(response[1])+f"]     [Size:{response[3]}]"))
            else:
                a="[+] " + site
                b="[Status code:" + str(response[2])+"]  ----->  " + response[0]
                c="    [Status code:" + str(response[1]) + f"]     [Size:{response[3]}]"
                if len(b)>100:
                    b=b[:100]+'\n'+' '*30+f"{b[100:]:<100}"
                print(self.row_format.format(a, b, c))
        if self.ext != None:
            for ext in self.ext.split(','):
                site = f"http://{self.ip}/{Dir}.{ext.strip()}"
                response = self.res.check_site(site, login, headers, cookies)
                if response[0]==None:
                    print("{:<50}{:>40}".format("[+] "+site+"    [Status code:"+str(response[1])+f"]     [Size:{response[3]}]"))
                else:
                    a="[+] " + site
                    b="[Status code:" + str(response[2])+"]  ----->  " + response[0]
                    c="    [Status code:" + str(response[1]) + f"]     [Size:{response[3]}]"
                    d=[[a, b, c]]
                    print(tabulate(d).strip('- \n'))

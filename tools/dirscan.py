#!/usr/bin/env python

import requests
import concurrent.futures
import urllib3
import collections
from .check import check_site


class Scan:
    def __init__(self, ip, ext):
        self.ip = ip
        self.ext = ext
        self.res = check_site()

    def dirScan(self, Dir):
        site = f"{self.ip}/{Dir}"
        response = self.res.check_site(site)
        if response[1] != None and response[1] != 404:
            if response[0]==None:
                print("{:<75}                    {:>18}".format("[+] "+site, "[Status code:"+str(response[1])+"]"))
            else:
                print("{:<75}                    {:>18}".format("[+] "+site+" --> "+response[0], "[Status code:"+str(response[2])+"]"))
            if self.ext != None:
                for ext in self.ext.split(','):
                    site = f"http://{self.ip}/{Dir}.{ext.strip()}"
                    response = self.res.check_site(site)
                    if response != None and response[1] != 404:
                        if response[0]==None:
                            print("{:<75}                    {:>18}".format("[+] "+site, "[Status code:"+str(response[1])+"]"))
                        else:
                            print("{:<75}                    {:>18}".format("[+] "+site+" --> "+response[0], "[Status code:"+str(response[2])+"]"))

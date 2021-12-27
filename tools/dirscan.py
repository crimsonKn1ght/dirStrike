#!/usr/bin/env python

import requests
import sys
import concurrent.futures
import urllib3
import collections
from .check import check_site


class Scan:
    def __init__(self, ip, ext, code):
        self.ip = ip
        self.ext = ext
        self.res = check_site()
        self.code = code

    def dirscan(self, Dir):
        site = f"{self.ip}/{Dir}"
        response_code = self.res.check_site(site)
        if response_code != None and response_code != self.code[0] and response_code != self.code[1]:
        	print("{:<50}                    {:>18}".format("[+] "+site, "[Status code:"+str(response_code)+"]"))
        	if self.ext != None:
        		for ext in self.ext.split(','):
        			site = f"http://{self.ip}/{Dir}.{ext.strip()}"
        			response_code = self.res.check_site(site)
        			if response_code != None and response_code != self.code[0] and response_code != self.code[1]:
        				print("{:<50}                    {:>18}".format("[+] "+site, "[Status code:"+str(response_code)+"]"))

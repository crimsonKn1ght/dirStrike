#!/usr/bin/env python

import requests
import sys
import concurrent.futures
import urllib3
import collections
from .check import check_site


class Scan:
    def __init__(self, ip, ext):
        self.ip = ip
        self.ext = ext
        self.res = check_site()

    def dirscan(self, Dir):
        site = f"http://{self.ip}/{Dir}"
        response_code = self.res.check_site(site)
        if response_code != None and response_code != 404:
        	print("{:<50}                    {:>18}".format("[+] "+site, "[Status code:"+str(response_code)+"]"))
        	if self.ext != None:
        		for ext in self.ext.split(','):
        			site = f"http://{self.ip}/{Dir}.{ext.strip()}"
        			response_code = self.res.check_site(site)
        			if response_code != None and response_code != 404:
        				print("{:<50}                    {:>18}".format("[+] "+site, "[Status code:"+str(response_code)+"]"))

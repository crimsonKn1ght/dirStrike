#!/usr/bin/env python

import requests
import sys
import concurrent.futures
import urllib3
import collections
from .check import check_site

class Fuzz:
	def __init__(self, ip, retries, login, headers, cookies):
		self.ip = ip.strip('https://www.').strip('http://www.')
		self.res = check_site()
		self.login = login
		self.retries = retries
		self.headers = headers
		self.cookies = cookies

	def fuzzer(self, sub):
		sub_domain = f"https://{sub}.{self.ip}"
		response = self.res.check_site(sub_domain, self.retries, self.login, self.headers, self.cookies)
		if response[1] != None and response[1] != 404:
			if response[0]==None:
				print("{:<50}{:>40}".format("[+] "+site+"    [Status code:"+str(response[1])+f"]     [Size:{response[3]}]"))
			else:
				a="[+] " + site
				b="[Status code:" + str(response[2])+"]  ----->  " + response[0]
				c="    [Status code:" + str(response[1]) + f"]     [Size:{response[3]}]"
				if len(b)>100:
					b=b[:100]+'\n'+' '*30+f"{b[100:]:<100}"

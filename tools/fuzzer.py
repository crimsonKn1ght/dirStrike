#!/usr/bin/env python

import requests
import sys
import concurrent.futures
import urllib3
import collections
from .check import check_site

class Fuzz:
	def __init__(self, ip, code):
		self.ip = ip.strip('https://www.').strip('http://www.')
		self.res = check_site()
		self.code = code

	def fuzzer(self, sub):
		sub_domain = f"https://{sub}.{self.ip}"
		response_code = self.res.check_site(sub_domain)
		if response_code != None and response_code != self.code[0] and response_code != self.code[1]:
			print("{:<50}                    {:>18}".format("[+] "+sub_domain, "[Status code:"+str(response_code)+"]"))

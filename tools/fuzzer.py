#!/usr/bin/env python

import requests
import sys
import concurrent.futures
import urllib3
import collections
from .check import check_site

class Fuzz:
	def __init__(self, ip):
		self.ip = ip.strip('https://www.').strip('http://www.')
		self.res = check_site()

	def fuzzer(self, sub):
		sub_domain = f"https://{sub}.{self.ip}"
		response = self.res.check_site(sub_domain)
		if response[1] != None and response[1] != 404:
			if response[0]==None:
				print("{:<100}                    {:>18}".format("[+] "+sub_domain, "[Status code:"+str(response[1])+"]"))
			else:
				print("{:<100}                    {:>18}".format("[+] "+sub_domain+" --> "+response[0], "[Status code:"+str(response[2])+"]"))

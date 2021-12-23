#!/usr/bin/env python

import requests
import sys
import concurrent.futures
import urllib3
import collections
from .check import check_site

class Fuzz:
	def __init__(self, ip):
		self.ip = ip
		self.res = check_site()

	def fuzzer(self, sub):
		sub_domain = f"http://{sub}.{self.ip}"
		response_code = self.res.check_site(sub_domain)
		if response_code != None and response_code != 404:
			print("{:<50}                    {:>18}".format("[+] "+sub_domain, "[Status code:"+str(response_code)+"]"))


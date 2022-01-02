#!/usr/bin/env python

import requests
from requests.auth import HTTPBasicAuth

class check_site:
	def __init__(self):
		self.count = 0

	def check_site(self, site, retries, login, headers, cookies):
		try:
			res1 = requests.get(site, headers=headers, auth=HTTPBasicAuth(login[0],login[1]), cookies=cookies)
			if len(res1.history)>0:
				if str(res1.history[0].status_code).startswith('3'):
					url=res1.url
				else:
					url=None
				if res1.history[0].status_code:
					first_code=res1.history[0].status_code
				else:
					first_code=None

		except Exception as e:
			if self.count < retries:
				self.count+=1
				check_site(site)
			else:
				print('Connection error:', e)

		else:
			return [url, res1.status_code, first_code, len(res1.content)]

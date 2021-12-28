#!/usr/bin/env python

import requests

class check_site:
	def __init__(self):
		self.headers={'User-Agent':'dirstrike/1.1'}

	def check_site(self, site):
		try:
			res1 = requests.get(site, headers=self.headers)
			if len(res1.history)>0:
				if str(res1.history[0].status_code).startswith('3'):
					url=res1.url
			if res1.history[0].status_code:
				first_code=res1.history[0].status_code
			else:
				first_code=None

		except Exception as e:
			print(e)
		else:
			return [url, res1.status_code, first_code]

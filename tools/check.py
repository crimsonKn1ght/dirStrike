#!/usr/bin/env python

import requests

class check_site:
	def __init__(self):
		self.headers={'User-Agent':'dirHunter/1.0'}

	def check_site(self, site):
		try:
			response = requests.get(site, headers=self.headers)
		except requests.ConnectionError:
			pass
		else:
			return response.status_code

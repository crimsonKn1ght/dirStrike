#!/usr/bin/env python

import requests

class check_site:
	def __init__(self):
		pass

	def check_site(self, site):
		try: 
			response = requests.get(site, verify=False)
		except requests.ConnectionError:
			pass
		else:
			return response.status_code

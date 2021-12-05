#!/usr/bin/env python

import requests
import sys
import threading
from args.arguments import argcheck
from checker.check import check_site
from banner.banner import Banner
import urllib3
from queue import Queue


class dirEnum:
	def __init__(self, ip, wordlist, mode, threads, ext):
		self.ip = ip
		self.wordlist = wordlist
		self.ext = ext
		self.threads = threads
		self.q = Queue()
		self.directories = []
		self.mode = mode
		self.res = check_site()


	def fuzzer(self):
		while not self.q.empty():
			sub = self.q.get()
			sub_domain = f"http://{sub}.{self.ip}"
			response_code = self.res.check_site(sub_domain)
			if response_code != None:
				print("{:<50}                    {:>18}".format("[+] "+sub_domain, "[Status code:"+str(response_code)+"]"))

	def dirScan(self):
		while not self.q.empty():
			dir = self.q.get()
			site = f"http://{self.ip}/{dir}"
			response_code = self.res.check_site(site)
			if response_code != None:
				print("{:<50}                    {:>18}".format("[+] "+site, "[Status code:"+str(response_code)+"]"))
			if self.ext != None:
				for ext in self.ext.split(','):
					site = f"http://{self.ip}/{dir}.{ext.strip()}"
					response_code = self.res.check_site(site)
					if response_code != None:
						print("{:<50}                    {:>18}".format("[+] "+site, "[Status code:"+str(response_code)+"]"))

	def dirEnum(self):
		file = open(self.wordlist, 'r')
		for dir in file.read().split('\n'):
			if not dir.startswith('#') and dir != '':
				self.q.put(dir)
		
		thread_list = []

		if self.mode == 'dir':
			for _ in range(int(self.threads)):
				thread = threading.Thread(target=self.dirScan)
				thread_list.append(thread)
				thread.start()

		elif self.mode == 'fuzz':
			for _ in range(int(self.threads)):
				thread = threading.Thread(target=self.fuzzer)
				thread_list.append(thread)
				thread.start()	

		for thread in thread_list:
			thread.join()


if __name__=='__main__':

	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
	
	arguments = argcheck()
	args = arguments.Argcheck()

	if args.mode:
		mode = args.mode
	else:
		mode = 'dir'

	if args.threads:
		threads = args.threads
	else:
		threads = 40

	if args.ext:
		ext = args.ext
	else:
		ext = None

	show_banner = Banner(args.url, args.wordlist, mode.lower(), threads, ext)
	show_banner.banner()

	scan = dirEnum(args.url, args.wordlist, mode.lower(), threads, ext)
	try:
		scan.dirEnum()
	except Exception as e:
		print(e)

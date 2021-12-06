#!/usr/bin/env python

import requests
import sys
import threading
import urllib3
from queue import Queue
from checker.check import check_site


class dirCrack:
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

	def dirCrack(self):
		try:
			file = open(self.wordlist, 'r')
		except:
			file = open(self.wordlist, 'r', enoding='ISO-8859-1')
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

#!/usr/bin/env python
#this is a directory scanner cum fuzzer but is currently needs some bug fixing.
import requests
import sys
import threading
import argparse
from queue import Queue


class argcheck:
	def __init__(self):
		self.example=\
		f'example: python {sys.argv[0]} -u 192.168.0.1 -w wordlist.txt -m dir -e php,html,txt -t 20\n 	 python {sys.argv[0]} -u 192.168.0.1 -w wordlist.txt -m fuzz -t 20'

	def Argcheck(self):
		parser = argparse.ArgumentParser(description="Tool for web page & directory discovery and also good \nfor fuzzing or sub-domain enumeration", usage=f"python {sys.argv[0]} -u <url[:port]> -w <wordlist> [options]", epilog=self.example, formatter_class=argparse.RawTextHelpFormatter)
		parser.add_argument('-u', '--url', metavar='', dest='url', help='Enter url[:port] to scan')
		parser.add_argument('-w', '--wordlist', metavar='', dest='wordlist', help='Enter wordlist location')
		parser.add_argument('-e', '--ext', metavar='', dest='ext', help='Enter extensions to scan (eg., php,html)')
		parser.add_argument('-t', '--threads', metavar='', dest='threads', help='Enter number of threads')
		parser.add_argument('-m', '--mode', metavar='', dest='mode', help='choose between FUZZ (fuzzing) or DIR(directory enumeration)')
		args = parser.parse_args()

		if len(sys.argv) <= 2:
			parser.print_help()
			sys.exit()

		return args


class dirScanner:
	def __init__(self, ip, wordlist, mode, threads, ext):
		self.ip = ip
		self.wordlist = wordlist
		self.ext = ext
		self.threads = threads
		self.q = Queue()
		self.directories = []
		self.mode = mode

	def fuzzer(self):
		while not self.q.empty():
			sub = self.q.get()
			sub_domain = f"http://{sub}.{self.ip}"
			try:
				response = requests.get(sub_domain)
			except requests.ConnectionError:
				pass
			else:
				print(sub_domain,"                [Status code:",response.status_code,"]")


	def dirScan(self):
		while not self.q.empty():
			dir = self.q.get()
			for ext in self.ext.split():
				site = f"http://{self.ip}/{dir}.{ext.strip()}"
				
	def check(self):
		response = requests.get(site, verify=False)
			if response.status_code==404:
				pass
			else:
				self.directories.append(url)
				print(url,"                [Status code:",response.status_code,"]")

	def dirEnum(self):
		file = open(self.wordlist, 'r')
		for dir in file.read().split():
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

	scan = dirScanner(args.url, args.wordlist, mode.lower(), threads, ext)
	scan.dirEnum()

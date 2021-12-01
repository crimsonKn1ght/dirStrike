#!/usr/bin/env python

import requests
import sys
import threading
import argparse
import urllib3
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
		parser.add_argument('-v', '--version', action='version', version='Version: 1.0', help=f'Show version of {sys.argv[0]}')
		args = parser.parse_args()

		if len(sys.argv) <= 2:
			parser.print_help()
			sys.exit()

		return args


class dirEnum:
	def __init__(self, ip, wordlist, mode, threads, ext):
		self.ip = ip
		self.wordlist = wordlist
		self.ext = ext
		self.threads = threads
		self.q = Queue()
		self.directories = []
		self.mode = mode

	def banner(self):
		border = '='*100+'\n'
		creator = 'DirEnum created by Gourab Roy\nVersion: 1.0\nMeant for legal use only!\n'
		settings = f'Details:\n==> URL: http://{self.ip}\n==> Wordlist: {self.wordlist}\n==> Threads: {self.threads}\n==> Extensions: {self.ext}\n==> Mode:{self.mode}\n'
		prologue = '\nStarting Scan:\n'
		print('\n'+border+creator+border+settings+border+prologue)

	def fuzzer(self):
		while not self.q.empty():
			sub = self.q.get()
			sub_domain = f"http://{sub}.{self.ip}"
			self.check(sub_domain)

	def dirScan(self):
		while not self.q.empty():
			dir = self.q.get()
			site = f"http://{self.ip}/{dir}"
			self.check(site)
			if self.ext != None:
				for ext in self.ext.split(','):
					site = f"http://{self.ip}/{dir}.{ext.strip()}"
					self.check(site)
				
	def check(self, site):
		try: 
			response = requests.get(site, verify=False)
		except requests.ConnectionError:
			pass
		else:
			if response.status_code != 404:
				print("{:<50}                    {:>18}".format("[+] "+site, "[Status code:"+str(response.status_code)+"]"))

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

	scan = dirEnum(args.url, args.wordlist, mode.lower(), threads, ext)
	scan.banner()
	try:
		scan.dirEnum()
	except:
		pass

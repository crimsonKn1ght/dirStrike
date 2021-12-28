#!/usr/bin/env python

import pyfiglet
from termcolor import cprint

class Banner:
	def __init__(self, ip, wordlist, threads, ext, mode):
		self.ip = ip
		self.wordlist = wordlist
		self.threads = threads
		self.ext = ext
		self.mode = mode
		pass

	def banner(self):
		banner = pyfiglet.figlet_format('dirStrike', font='slant')
		border = '='*100
		creator = 'dirStrike created by Gourab Roy(@crimsonKn1ght)\nVersion: 1.1\nMeant for legal use only!'
		settings = f'Details:\n==> URL: {self.ip}\n==> Wordlist: {self.wordlist}\n==> Threads: {self.threads}\n==> Extensions: {self.ext}\n==> Mode:{self.mode}'
		prologue = '\nStarting Scan:'
		cprint('\n'+banner, 'red')
		cprint(border+'\n'+creator+'\n'+border, 'green')
		cprint(settings,'blue')
		cprint(border+'\n'+prologue, 'green')

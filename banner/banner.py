#!/usr/bin/env python

class Banner:
	def __init__(self, ip, wordlist, threads, ext, mode):
		self.ip = ip
		self.wordlist = wordlist
		self.threads = threads
		self.ext = ext
		self.mode = mode
		pass

	def banner(self):
		border = '='*100+'\n'
		creator = 'DirEnum created by Gourab Roy(@confusedHatHacker)\nVersion: 1.0\nMeant for legal use only!\n'
		settings = f'Details:\n==> URL: http://{self.ip}\n==> Wordlist: {self.wordlist}\n==> Threads: {self.threads}\n==> Extensions: {self.ext}\n==> Mode:{self.mode}\n'
		prologue = '\nStarting Scan:\n'
		print('\n'+border+creator+border+settings+border+prologue)

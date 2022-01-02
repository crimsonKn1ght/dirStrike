#!/usr/bin/env python

import argparse
import sys


class argcheck:
	def __init__(self):
		self.example=\
		f'example: python {sys.argv[0]} -u 192.168.0.1 -w wordlist.txt -m dir -e php,html,txt -t 20\n 	 python {sys.argv[0]} -u 192.168.0.1:443 -w wordlist.txt -m fuzz -t 20'

	def Argcheck(self):
		parser = argparse.ArgumentParser(description="Tool for web page & directory discovery and also good \nfor fuzzing or sub-domain enumeration", usage=f"python {sys.argv[0]} -u <url[:port]> -w <wordlist> [options]", epilog=self.example, formatter_class=argparse.RawTextHelpFormatter)
		parser.add_argument('-u', '--url', metavar='', dest='url', help='Enter url[:port] to scan')
		parser.add_argument('-w', '--wordlist', metavar='', dest='wordlist', help='Enter wordlist location')
		parser.add_argument('-e', '--ext', metavar='', dest='ext', help='Enter extensions to scan (eg., php,html)')
		parser.add_argument('-t', '--threads', metavar='', dest='threads', help='Enter number of threads')
		parser.add_argument('-r', '--retries', metavar='', dest='retries', help='No of retries in case of connection error (Default:2)')
		parser.add_argument('-H', '--headers', metavar='', dest='headers', help='Type in any headers you want to send [eg, -H "{\'User-Agent\':\'name\'}"]')
		parser.add_argument('-C', '--cookies', metavar='', dest='cookies', help='Type in cookie you want to send [eg, -C "{\'Cookie-name\':\'Cookie-value\'}"]')
		parser.add_argument('-U', '--user', metavar='', dest='User', help='Type in username for auth')
		parser.add_argument('-P', '--pass', metavar='', dest='Pass', help='Type in password for auth')
		parser.add_argument('-m', '--mode', metavar='', dest='mode', help='choose between FUZZ (fuzzing) or DIR(directory enumeration)')
		parser.add_argument('-v', '--version', action='version', version='Version: 1.0', help=f'Show version of {sys.argv[0]}')
		args = parser.parse_args()

		if len(sys.argv) <= 2:
			parser.print_help()
			sys.exit()

		return args

#!/usr/bin/env python


from args.arguments import argcheck
from banner.banner import Banner
from tools.main import dirStrike
import urllib3, json


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
        threads = 50

    if args.ext:
        ext = args.ext
    else:
        ext = None

    if args.User and args.Pass:
    	login=[args.User, args.Pass]
    else:
    	login = [None, None]

    if args.cookies:
    	try:
    		cookies=json.loads(args.cookies)
    	except json.decoder.JSONDecodeError:
    		cookies=json.loads(args.cookies.replace('\'','\"'))
    else:
    	cookies=None

    if args.headers:
    	try:
    		headers=json.loads(args.headers)
    	except json.decoder.JSONDecodeError:
    		headers=json.loads(args.headers.replace('\'','\"'))
    else:
    	headers={'User-Agent':'dirStrike/1.1'}
    	print('done2')

    if not args.url.startswith('http://') and not args.url.startswith('https://'):
    	url='http://'+args.url
    else:
    	url=args.url

    if args.retries:
    	retries = args.retries
    else:
    	retries = 2

    show_banner = Banner(url, args.wordlist, threads, ext, mode.lower())
    show_banner.banner()

    scan = dirStrike(url, args.wordlist, mode.lower(), threads, ext, retries, login, headers, cookies)

    try:
        scan.dirStrike()
    except Exception as e:
        print(e)

#!/usr/bin/env python


from args.arguments import argcheck
from banner.banner import Banner
from tools.main import dirStrike
import urllib3


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

    if not args.url.startswith('http://') or not args.url.startswith('https://'):
        if not args.url.startswith('www.'):
            url='https://www.'+args.url
        else:
            url='https://'+args.url
    if args.url.startswith('https://') or args.url.startswith('http://'):
        site=args.url.lstrip('https://')
        site=site.lstrip('http://')
        if not site.startswith('www.'):
            url='https://www.'+site
        else:
            url=args.url


    show_banner = Banner(url, args.wordlist, threads, ext, mode.lower())
    show_banner.banner()

    scan = dirStrike(url, args.wordlist, mode.lower(), threads, ext)
    try:
        scan.dirStrike()
    except Exception as e:
        print(e)

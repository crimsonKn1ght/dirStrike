# dirEnum
Python tool for enumerating directories and for fuzzing

Usage instructions:
`python dirEnum.py -u <url[:port]> -w <wordlist> [options]`
  
Optional arguments for dirEnum

```
optional arguments:
  -h, --help        show this help message and exit
  -u , --url        Enter url[:port] to scan
  -w , --wordlist   Enter wordlist location
  -e , --ext        Enter extensions to scan (eg., php,html)
  -t , --threads    Enter number of threads
  -m , --mode       choose between FUZZ (fuzzing) or DIR(directory enumeration) [Default: dir]
```

Examples:
```
python dirEnum.py -u 192.168.0.1 -w wordlist.txt -m dir -e php,html,txt -t 20
python dirEnum.py -u 192.168.0.1 -w wordlist.txt -m fuzz -t 20
```

Please note: For fuzzing change mode with -m option, by default it is in dir mode/does directory enumeration.

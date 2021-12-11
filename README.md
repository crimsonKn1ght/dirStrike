# dirHunter
Python tool for enumerating directories and for fuzzing

Download the tool with following command from shell:
```
git clone https://github.com/crimsonKn1ght/dirHunter
```

After cloning change directories and go to dirHunter folder. Run the following command from shell:
```
pip install -r requirements.txt
```

Usage instructions:
`python dirHunter.py -u <url[:port]> -w <wordlist> [options]`
  
Optional arguments for dirHunter

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
python dirHunter.py -u 192.168.0.1 -w wordlist.txt -m dir -e php,html,txt -t 20
python dirHunter.py -u 192.168.0.1:443 -w wordlist.txt -m fuzz -t 20
```

Please note: For fuzzing change mode with -m option, by default it is in dir mode/does directory enumeration.

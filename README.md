# dirStrike
Tool for web page & directory discovery and also good for fuzzing or sub-domain enumeration

Download the tool with following command from shell:
```
git clone https://github.com/crimsonKn1ght/dirStrike
```

After cloning change directories and go to dirStrike folder. Run the following command from shell:
```
pip install -r requirements.txt
```

Usage instructions:
`python dirStrike.py -u <url[:port]> -w <wordlist> [options]`
  
Optional arguments for dirStrike

```
optional arguments:
  -h, --help        show this help message and exit
  -u , --url        Enter url[:port] to scan
  -w , --wordlist   Enter wordlist location
  -e , --ext        Enter extensions to scan (eg., php,html)
  -t , --threads    Enter number of threads
  -r , --retries    No of retries in case of connection error (Default:2)
  -H , --headers    Type in any headers you want to send [eg, -H "{'User-Agent':'name'}"]
  -C , --cookies    Type in cookie you want to send [eg, -C "{'Cookie-name':'Cookie-value'}"]
  -U , --user       Type in username for auth
  -P , --pass       Type in password for auth
  -m , --mode       choose between FUZZ (fuzzing) or DIR(directory enumeration)
  -v, --version     Show version of ./dirStrike.py
```

Examples:
```
python ./dirStrike.py -u 192.168.0.1 -w wordlist.txt -m dir -e php,html,txt -t 50
python ./dirStrike.py -u 192.168.0.1:443 -w wordlist.txt -m fuzz -t 50 -H '{"User-Agent":"name"}'
```

Please note: For fuzzing change mode with -m option, by default it is in dir mode/does directory enumeration.

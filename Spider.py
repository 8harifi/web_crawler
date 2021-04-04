import requests
from bs4 import BeautifulSoup as bs
import re
import sys
from termcolor import colored


def banner():
	print("""



██╗░░░░░██╗███████╗░█████╗░██████╗░██████╗░  ███╗░░░███╗░█████╗░██████╗░███████╗  
██║░░░░░██║╚════██║██╔══██╗██╔══██╗██╔══██╗  ████╗░████║██╔══██╗██╔══██╗██╔════╝  
██║░░░░░██║░░███╔═╝███████║██████╔╝██║░░██║  ██╔████╔██║███████║██║░░██║█████╗░░  
██║░░░░░██║██╔══╝░░██╔══██║██╔══██╗██║░░██║  ██║╚██╔╝██║██╔══██║██║░░██║██╔══╝░░  
███████╗██║███████╗██║░░██║██║░░██║██████╔╝  ██║░╚═╝░██║██║░░██║██████╔╝███████╗  
╚══════╝╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝  

░██╗░░░░░░░██╗███████╗██████╗░  ░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗██╗░░░░░███████╗██████╗░
░██║░░██╗░░██║██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██║░░░░░██╔════╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██████╦╝  ██║░░╚═╝██████╔╝███████║░╚██╗████╗██╔╝██║░░░░░█████╗░░██████╔╝
░░████╔═████║░██╔══╝░░██╔══██╗  ██║░░██╗██╔══██╗██╔══██║░░████╔═████║░██║░░░░░██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░███████╗██████╦╝  ╚█████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░███████╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═╝░░╚═╝

		""")



def usage():
	print("""

		--single-domain                  only crawl one domain, crawl all domains
		--output                 -o      outout file's name
		--time-out               -t      set a time out for the requests

		""")



banner()


args = sys.argv
args.remove(sys.argv[0])


if len(args) < 1 :
	usage()
	exit()

SingleDomain = False


urls = []
domains = []

OutputFileName = "output.txt"
timeoutValue = ""

n = 0


for arg in args:
	n = n + 1
	if arg.startswith('-'):
		if arg == "-o" or arg == "--output":
			OutputFileName = args[n]
		elif arg == "--single-domain":
			SingleDomain = True
		elif arg == "--timeout" or arg == "-t":
			try :
				timeoutValue = int(args[n])
			except:
				print("[!] ERROR: Please select a valid number for timeout value")
				exit()

	else:
		if OutputFileName:
			if arg == OutputFileName:
				pass
		if timeoutValue:
			if arg == timeoutValue:
				pass
		else:
			urls.append(arg)


if len(urls) > 1:
	print("[!] ERROR: more than one url was given")
	exit()
elif len(urls) < 1:
	print("[!] Please specify a URL")
	exit()
else:
	mainURL = urls[0]


with open(OutputFileName, 'w') as f :
	pass

"""

proto = ''



for url in urls:
	if url.startswith("https://"):
		proto = "https://"
		rdomain = re.findall(r"https:\/\/(.+?)\/", url)
		if len(rdomain) == 1:
			domains.append(rdomain[0])
		elif len(rdomain) > 1:
			print(colored("[!] Unknown ERROR", 'red'))
			exit()
		elif len(rdomain) < 1 :
			rdomain = re.findall(r'https:\/\/(.+)', url)
			if len(rdomain) == 1:
				domains.append(rdomain[0])
			else:
				print(colored("[!] Unknown ERROR", 'red'))

	elif url.startswith("http://"):
		proto = "http://"
		rdomain = re.findall(r"http:\/\/(.+?)\/", url)
		if len(rdomain) == 1:
			domains.append(rdomain[0])
		elif len(rdomain) > 1:
			print(colored("[!] Unknown ERROR", 'red'))
			exit()
		elif len(rdomain) < 1 :
			rdomain = re.findall(r'http:\/\/(.+)', url)
			if len(rdomain) == 1:
				domains.append(rdomain[0])
			else :
				print(colored("[!] Unknown ERROR", 'red'))
	else:
		print(colored("[!] ERROR: please enter a valid URL(EX: https://example.net)", 'red'))
		print(colored("[!] ERROR: only HTTP and HTTPS can be accepted", 'red'))


if len(domains) > 1:
	print(colored("[!] ERROR: more than one domain found, but the '--single-domain' option is used", 'red'))
elif len(domains) < 1:
	print(colored("[!] ERROR: no Domain was found, check the url and try again", 'red'))
elif len(domains) == 1:
	domain = domains[0]
"""



tmpRes = re.findall(r"(.+):\/\/(.+)", mainURL)

proto = tmpRes[0][0]
domain = tmpRes[0][1]





index = 0

string = ""


for url in urls:
	index = index + 1
	print(colored(f"[*] Sending request to {url}", 'yellow'))
	try:
		if timeoutValue :
			res1 = requests.get(url = url, timeout = timeoutValue)
		else :
			res1 = requests.get(url)

		if res1.status_code == 200:
			print(colored(f"[+] {url}: {res1.status_code}", 'green'))
		else:
			print(colored(f"[-] {url}: {res1.status_code}", 'red'))
		print(colored(f"[*] Looking for Urls in {url}", 'yellow'))
		soup = bs(res1.text, "html.parser")
		tags = soup.select("a[href]")
		print(colored(f"[+] {len(tags)} urls was found in '{url}'", 'green'))
		print(colored("--------------------------------------", 'blue'))
		if SingleDomain :
			for a in tags:
				alink = a.attrs.get("href")
				if alink.startswith("/"):
					urls.append(proto + "://" + domain + alink)
				elif alink.startswith(url) or re.findall(rf".+:\/\/.*{domain}", url) :
					urls.append(alink)
		else:
			for a in tags:
				alink = a.attrs.get("href")
				if alink.startswith("/"):
					urls.append(proto + "://" + domain + alink)
				elif alink.startswith(url) or re.findall(rf".+:\/\/.*{domain}", url) :
					urls.append(alink)
				else:
					urls.append(alink)

	except requests.Timeout :
		print(colored(f"[-] {url}: Timeout", "red"))
		print(colored(f"--------------------------------------", "blue"))
	urls = list(set(urls))
	urls.remove(url)
	string = string + url + ": "+ str(res1.status_code) + "\n"

	if index >= 20:
		with open(OutputFileName, "a") as f :
			f.write(string)
			string = ""









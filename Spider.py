import requests
from bs4 import BeautifulSoup as bs
import re
import sys

def banner():
	print("Banner")

def usage():
	print("usage")


args = sys.argv
args.remove(sys.argv[0])


if len(args) < 1 :
	banner()
	usage()
	exit()

SingleDomain = False


urls = []
domains = []



n = 0
for arg in args:
	n = n + 1
	if arg.startswith('-'):
		if arg == "-o" or arg == "--output":
			OutputFileName = args[n]
		if arg == "--single-domain":
			SingleDomain = True
	else:
		urls.append(arg)





proto = ''


for url in urls:
	if url.startswith("https://"):
		proto = "https://"
		rdomain = re.findall(r"https:\/\/(.+?)\/", url)
		if len(rdomain) == 1:
			domains.append(rdomain[0])
		elif len(rdomain) > 1:
			print("[!] Unknown ERROR")
			exit()
		elif len(rdomain) < 1 :
			rdomain = re.findall(r'https:\/\/(.+)', url)
			if len(rdomain) == 1:
				domains.append(rdomain[0])
			else:
				print("[!] Unknown ERROR")

	elif url.startswith("http://"):
		proto = "http://"
		rdomain = re.findall(r"http:\/\/(.+?)\/", url)
		if len(rdomain) == 1:
			domains.append(rdomain[0])
		elif len(rdomain) > 1:
			print("[!] Unknown ERROR")
			exit()
		elif len(rdomain) < 1 :
			rdomain = re.findall(r'http:\/\/(.+)', url)
			if len(rdomain) == 1:
				domains.append(rdomain[0])
			else :
				print("[!] Unknown ERROR")


if len(domains) > 1:
	print("[!] ERROR: more than one domain found, but the '--single-domain' option is used")
elif len(domains) < 1:
	print("[!] ERROR: no Domain was found, check the url and try again")
elif len(domains) == 1:
	domain = domains[0]









for url in urls:
	print(f"[*] Sending request to {url}")
	res1 = requests.get(url)
	if res1.status_code == 200:
		print(f"[+] {url}: {res1.status_code}")
	else:
		print(f"[-] {url}: {res1.status_code}")
	print(f"[*] Looking for Urls in {url}")
	soup = bs(res1.text, "html.parser")
	tags = soup.select("a[href]")
	if SingleDomain :
		for a in tags:
			alink = a.attrs.get("href")
			if alink.startswith("/"):
				urls.append(proto + domain + alink)
			elif alink.startswith(url) or re.findall(rf".+:\/\/.*{domain}", url) :
				urls.append(alink)
	else:
		for a in tags:
			alink = a.attrs.get("href")
			urls.append(alink)




















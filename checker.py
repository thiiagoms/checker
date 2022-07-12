# -*- coding: utf-8 -*-

import colorama
from requests import get
from colorama import Fore

colorama.init(autoreset=True)

file = open('sites.txt', 'r')

sites = [line.strip() for line in file]

for site in sites:
	try:
		response = get(site)
		if response.status_code in range(200, 299):
			print(f"[*] {site}: is {Fore.GREEN}OK ")
		if response.status_code in range(400, 499):
			print(f"[*] {site}: is {Fore.RED}OFF ")
	except Exception as error:
		print(f"{Fore.RED} {error}")
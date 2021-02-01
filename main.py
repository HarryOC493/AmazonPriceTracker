import requests
import re
import csv
import threading
import sys

from bs4 import BeautifulSoup
from colorama import Fore, Style
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
# Get list of user agents.
user_agents = user_agent_rotator.get_user_agents()
# Get Random User Agent String.
user_agent = user_agent_rotator.get_random_user_agent()
#print("User-Agent: ", user_agent)

headers = {
        "User-Agent": user_agent
    }
url = "https://www.amazon.co.uk/Laser-5497-Large-Joint-Separator/dp/B00FZJOJNK/ref=pd_ybh_a_4?_encoding=UTF8&psc=1&refRID=79PYZT2X2WFC5NNRE6ZN"

def get_converted_price(price):
#Gets Rid of Currency Symbol E.g $, £
    converted_price = float(re.sub(r"[^\d.]", "", price)) # Thanks to https://medium.com/@oorjahalt
    return converted_price

def scrape(_url):
	try:
		details = {"name": "", "price": 0, "deal": True, "url": ""}
		if _url is None:
			details = 'Url is none'
		else:
			page = requests.get(_url, headers=headers)
			soup = BeautifulSoup(page.content, "html5lib")
			title = soup.find(id="productTitle")
			price = soup.find(id="priceblock_dealprice")
			if price is None:
			    price = soup.find(id="priceblock_ourprice")
			    details["deal"] = False
			if title is not None and price is not None:
			    details["name"] = title.get_text().strip()
			    details["price"] = get_converted_price(price.get_text())
			    details["url"] = _url
			else:
			    print("Product Page Not Found")
		return details['price'], details['name']
	except Exception as E:
		print(Fore.RED + "Error Occured, Most Likely An Ip ban")
		print(E)
		exit()




def check_price(TI):
	threading.Timer(TI * 60, check_price, args = [TI]).start()
	print("Designed And Built By Harry O'Connor Twitter @Harryoc493")
	with open('urls.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			#Iterate through rows in csv file
			if line_count == 0:
				#If its the top row, print the column names
				#print(f'Column names are {", ".join(row)}')
				timeInterval = str({row[2]})
				line_count += 1
			else:
				url = f'{row[0]}'
				#print(url)
				price, ItemName = scrape(url)
				#print(price)
				if price <= float(f'{row[1]}'):
					print(Fore.GREEN + "Price Of", ItemName, "Is Equal To Or Lower Than Its Threshold (", price, ")")
					#Send Telegram Message Here
				else:
					#Price Is Still To high do nothing
					print(Fore.WHITE + "Price Of", ItemName, "Is Higher Than Its Threshold (", price, ")")
				line_count += 1

with open('urls.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	count = 1
	for row in csv_reader:
		if count == 1:
			global timeInterval
			#Iterate through rows in csv file
			timeInterval = float(row[2])
			#print(timeInterval)
			count += 1

print("Designed And Built By Harry O'Connor Twitter @Harryoc493")
print(timeInterval, "minutes between checking prices")
Tiv = timeInterval
check_price(Tiv)












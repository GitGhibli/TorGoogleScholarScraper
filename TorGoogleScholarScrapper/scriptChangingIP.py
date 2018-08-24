import sys
import requests
from scrapy.selector import Selector
import threading
from stem import Signal
from stem.control import Controller
import time
		
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrapPage(googlePage):	
	# url = "https://scholar.google.cz/scholar?start=" + googlePage + "0&q=allintitle%3A+" + sys.argv[1] + "&hl=en&as_sdt=0%2C5&as_ylo=" + sys.argv[2] + "&as_yhi=" + sys.argv[3]
	url = "https://scholar.google.cz/scholar?start=" + googlePage + "0&q=allintitle%3A+Medic&hl=en&as_sdt=0%2C5&as_ylo=2010&as_yhi=2017"
	session = requests.Session()
	# session.proxies = {'http':'127.0.0.1:8118'}
	response = requests.get(url, headers=headers)
	print(response.content)
	searchResults = Selector(response=response).xpath('//div[@id="gs_res_ccl_mid"]//h3/a/@href').extract()
	for address in searchResults:
		print(address)

def renew_ip():
	with Controller.from_port(port=9051) as controller:
		controller.authenticate()
		controller.signal(Signal.NEWNYM)
		time.sleep(controller.get_newnym_wait())
		
url = "https://scholar.google.cz/scholar?start=00&q=allintitle%3A+Medic&hl=en&as_sdt=0%2C5&as_ylo=2010&as_yhi=2017"
response = requests.get(url, headers=headers)
print(response.content)
	
	
# for	x in range(0,1):
	# scrapPage(str(x));
	# if(x%5 == 0):
		# print("changing ip")
		# renew_ip()
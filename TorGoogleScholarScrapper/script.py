import sys
import requests
from scrapy.selector import Selector
import threading
from stem import Signal
from stem.control import Controller
import time

class myThread (threading.Thread):
	def __init__(self, googlePage):
		threading.Thread.__init__(self)
		self.googlePage = googlePage
	def run(self):
		url = "https://scholar.google.cz/scholar?start=" + self.googlePage + "0&q=allintitle%3A+" + sys.argv[1] + "&hl=en&as_sdt=0%2C5&as_ylo=" + sys.argv[2] + "&as_yhi=" + sys.argv[3]
		print(url)
		response = requests.get(url, headers=headers)
		print(response.content)
		searchResults = Selector(response=response.content).xpath('//div[@id="gs_res_ccl_mid"]//h3/a/@href').extract()
		print(searchResults)
		for address in searchResults:
			print(self.googlePage + ":" + address)
		
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

threads = []

def scrapPage(googlePage):	
	# url = "https://scholar.google.cz/scholar?start=" + googlePage + "0&q=allintitle%3A+" + sys.argv[1] + "&hl=en&as_sdt=0%2C5&as_ylo=" + sys.argv[2] + "&as_yhi=" + sys.argv[3]
	url = "https://scholar.google.cz/scholar?start=" + googlePage + "0&q=allintitle%3A+Medic&hl=en&as_sdt=0%2C5&as_ylo=2010&as_yhi=2017"
	print(url)
	response = requests.get(url, headers=headers)
	searchResults = Selector(response=response).xpath('//div[@id="gs_res_ccl_mid"]//h3/a/@href').extract()
	for address in searchResults:
		print(address)

def renew_ip():
	with Controller.from_port(port=9051) as controller:
		controller.authenticate()
		controller.signal(Signal.NEWNYM)
		time.sleep(controller.get_newnym_wait())
		
for	x in range(0,10):
	if(x%5 == 0):
		print("changing ip")
		renew_ip()
	scrapPage(str(x));
	# thread = myThread(str(x))
	# threads.append(thread)
	# thread.start()
	
# for t in threads:
	# t.join()
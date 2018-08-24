from stem import Signal
from stem.control import Controller
import requests
from scrapy.selector import Selector
import time

def renew_ip():
	with Controller.from_port(port=9051) as controller:
		controller.authenticate()
		controller.signal(Signal.NEWNYM)
		time.sleep(controller.get_newnym_wait())
	   
for tmp in list(range(0,20)):
	renew_ip()
	session = requests.Session()
	session.proxies = {'http':'127.0.0.1:8118'}
	response = session.get("http://www.icanhazip.com")
	searchResults = Selector(response=response).xpath('//pre').extract()
	print(response.content)

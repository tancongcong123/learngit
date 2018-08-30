#!/usr/bin/env python3
from urllib import request,parse

# url='https://api.douban.com/v2/book/2129650'
url = 'https://www.ebay.com/itm/adidas-NMD-R2-Primeknit-Shoes-Mens/153057156614?_trkparms=5373%3A5000006436%7C5374%3AFashion%7C5079%3A5000006436'

with request.urlopen(url) as f:
	data = f.read()
	print('Status:',f.status,f.reason)
	for k,v in f.getheaders():
		print('%s:%s' % (k,v)) 
	print('Data:',data.decode('utf-8'))
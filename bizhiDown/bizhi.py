# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import os
import time

		
			
def downImage(down_url):
	list_url = []
	hrefs = []
	titles = []
	filenames = []
	for num in range(1,3):
		if num == 1:
			url = down_url +  '/index.htm'
		else:
			url = down_url +  '/index_%d.htm' % num
		headers = {
				"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
		}
		req = requests.get(url = url,headers = headers)
		req.encoding = 'GBK'
		html = req.text
		
		bf = BeautifulSoup(html, 'lxml')
		
		targets_url = bf.find_all('a')

	 		




	
		for each in targets_url:
			href = each.get('href')
			title = each.get('title')
				
			if (href is None) == False:
				hrefs.append(href)
			if (title is None) == False:
				titles.append(title)	
				 
			

		
		for names in titles:
			str = "更新时间"
			# print(names)
			if str in names :
				name_split = names.split(' 更新时间')[0]
				filenames.append(name_split.strip())
				
		# print(filenames)

		for url in hrefs:
			str = "/desk"
			
			if str in url :
				list_url.append(url)
				
	
		# print(list_url)
			

	
	i = 0	
	for each_img in list_url:
		
		target_url = 'http://www.netbian.com' + each_img
		# print(target_url) 
		filename = 'images/' + filenames[i] + '.jpg'
		
		i += 1
		headers = {
			"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
		}
		
		img_req = requests.get(url = target_url,headers = headers)
		img_req.encoding = 'GBK'
		img_html = img_req.text
		img_bf_1 = BeautifulSoup(img_html, 'lxml')
		# img_url = img_bf_1.find_all('div', class_='pic')

		image_url = img_bf_1.find_all('div', class_='pic')
		down_url = image_url[0].find_all('img')[0].attrs['src']
		print(filename)

		urlretrieve(url = down_url,filename =  filename)	
		
		
if __name__ == '__main__':
	type = input('请输入下载的壁纸类型：（比如youxi,meinv）:')
	find_url = 'http://www.netbian.com/' + type
	downImage(find_url)		
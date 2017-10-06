# should have pyselenium installed
# have to install https://sites.google.com/a/chromium.org/chromedriver/ and put in PATH

from selenium import webdriver
import time
import urllib
import random
import os
# search terms: 
# red lipstick on face 
# pink lipstick on face 
# blue lipstick on face
# orange lipstick on face
# purple lipstick on face
# (can add asian, white, black, olive qualifiers to face)

d = webdriver.Chrome()

search_urls = [
	'https://www.google.com/search?q=blue+lipstick+on+face',
	'https://www.google.com/search?q=orange+lipstick+on+face',
	'https://www.google.com/search?q=pink+lipstick+on+face',
	'https://www.google.com/search?q=red+lipstick+on+face',
	'https://www.google.com/search?q=purple+lipstick+on+face',

	'https://www.google.com/search?q=blue+lipstick+on+asian+face',
	'https://www.google.com/search?q=orange+lipstick+on+asian+face',
	'https://www.google.com/search?q=pink+lipstick+on+asian+face',
	'https://www.google.com/search?q=red+lipstick+on+asian+face',
	'https://www.google.com/search?q=purple+lipstick+on+asian+face',

	'https://www.google.com/search?q=blue+lipstick+on+black+face',
	'https://www.google.com/search?q=orange+lipstick+on+black+face',
	'https://www.google.com/search?q=pink+lipstick+on+black+face',
	'https://www.google.com/search?q=red+lipstick+on+black+face',
	'https://www.google.com/search?q=purple+lipstick+on+black+face',

	'https://www.google.com/search?q=blue+lipstick+on+white+face',
	'https://www.google.com/search?q=orange+lipstick+on+white+face',
	'https://www.google.com/search?q=pink+lipstick+on+white+face',
	'https://www.google.com/search?q=red+lipstick+on+white+face',
	'https://www.google.com/search?q=purple+lipstick+on+white+face',

	'https://www.google.com/search?q=blue+lipstick+on+olive+face',
	'https://www.google.com/search?q=orange+lipstick+on+olive+face',
	'https://www.google.com/search?q=pink+lipstick+on+olive+face',
	'https://www.google.com/search?q=red+lipstick+on+olive+face',
	'https://www.google.com/search?q=purple+lipstick+on+olive+face',
]

base_path = '/Users/ssingla/repos/ava/datascripts/data/lipstickcolors/'
download_locations = [
	'blue/',
	'orange/',
	'pink/',
	'red/',
	'purple/',

	'blue/',
	'orange/',
	'pink/',
	'red/',
	'purple/',

	'blue/',
	'orange/',
	'pink/',
	'red/',
	'purple/',

	'blue/',
	'orange/',
	'pink/',
	'red/',
	'purple/',

	'blue/',
	'orange/',
	'pink/',
	'red/',
	'purple/',
] # should be same len as search_urls

# thanks https://stackoverflow.com/questions/13343347/randomizing-two-lists-and-maintaining-order-in-python 
# so different runs populate different colors first
combined = list(zip(search_urls, download_locations))
random.shuffle(combined)

search_urls[:], download_locations[:] = zip(*combined)

for i in range(len(search_urls)):
	search_url = search_urls[i]
	download_location = base_path + download_locations[i]
	d.get(search_url)
	# scroll down for some time
	images = d.find_element_by_link_text('Images')
	images.click()
	time.sleep(3)
	for i in range(7):
		d.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(1)
	images_block = d.find_element_by_id('rg_s')
	#print('images_block: ', images_block)
	images_arr = images_block.find_elements_by_class_name('rg_di')
	#print('images_arr: ', images_arr)
	links = set()
	print 'going to scrape ', len(images_arr), 'images'

	if not os.path.exists(download_location):
		os.mkdir(download_location)

	for j, image in enumerate(images_arr):
		# try:
		image.click()
		time.sleep(4)
		potential_links = d.find_elements_by_class_name('irc_mi')
		#print('potential_links: ', potential_links)
		for potential_link in potential_links:
			potential_link_url = potential_link.get_attribute('src')
			if potential_link_url and potential_link_url not in links:
				links.add(potential_link_url)
				print 'added link: ', potential_link.get_attribute('src')
				urllib.urlretrieve(potential_link_url, download_location + potential_link_url.split('/')[-1])
				time.sleep(2)
	# except:
		# 	print 'encountered a failure on a part img'


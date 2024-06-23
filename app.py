#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import codecs
import requests
from bs4 import BeautifulSoup

os.system("clear")
print('auzefdl')

with open('links.lst', 'r') as link_file:
	print('\n[Fetching Links]')
	links = link_file.readlines()
	
	for linkindex, link in enumerate(links):
		try:
			response = requests.get(link.strip())
			response.raise_for_status()
			htmltext = response.text
		except requests.RequestException as e:
			print(f"Connection error for link {link.strip()}: {e}")
			continue
		
		soup = BeautifulSoup(htmltext, 'html.parser')
		title_element = soup.find('span', id='assetName')
		url_element = soup.find('source', size='720')

		if title_element and url_element:
			video_title = title_element.get_text()
			video_url = url_element['src']
			
			print(f"[{linkindex+1}/{len(links)}] Adding {video_title} with url {video_url}")
			
			with codecs.open('videos.lst', 'a', 'utf-8') as video_file:
				video_file.write(f"{video_title},{video_url}\n")
		else:
			print(f"Could not find required elements {link.strip()}")

with open('videos.lst', 'r') as video_file:
	print('\n[Downloading]')
	videos = video_file.readlines()
	for videoindex, video in enumerate(videos):
		vs = video.split(',')
		print(f"[{videoindex}/{str(len(links))}] Downloading '{vs[0]}'")
		os.system(f"aria2c -x 10 --summary-interval 0 -d 'downloads/' -o '{vs[0]}.mp4' '{vs[1]}' ")
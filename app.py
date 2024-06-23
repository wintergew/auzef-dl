#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import codecs
import requests
from bs4 import BeautifulSoup

def main():
	os.system("clear")
	print('auzefdl')
	print('\n[Please paste the links and press enter to continue]')
	csl = input()
	links = csl.split(",")
	videos = {}
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
			videos[video_title] = video_url
		else:
			print(f"Could not find required elements {link.strip()}")

	print('\n[Downloading]')
	for videoindex, (title, url) in enumerate(videos.items()):
		print(f"[{videoindex}/{str(len(videos))}] Downloading '{title}'")
		os.system(f"aria2c -x 10 --summary-interval 0 -d 'downloads/' -o '{title}.mp4' '{url}' ")

if __name__ == "__main__":
    main()
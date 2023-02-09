#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import codecs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support import expected_conditions as EC

os.system("clear")
print('auzefdl')

with open('links.lst', 'r') as link_file:
	driver = webdriver.Firefox()
	print('\n[Fetching Links]')
	links = link_file.readlines()
	for linkindex, link in enumerate(links):
		driver.get(link.strip())
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ad")))
		time.sleep(2)
		linktitle = driver.find_element_by_id("ad").text
		link = link.strip()[:-10]+'{0}'+'/'+link.strip()[-10:]
		with codecs.open('videos.lst','a','utf-8') as video_file:
			for chapter in range(1,15):
				driver.get(link.format(chapter))
				WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "konu-1")))
				driver.find_element_by_id("ders-anlatimi").click()
				driver.switch_to_window(driver.window_handles[1])
				WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "video")))
				time.sleep(3)
				videolink = driver.find_elements_by_tag_name('video')[0].get_attribute("src")
				if videolink.endswith('.mp4'):
					print("[{0}/{1}][{2}/14] {3}".format(str(linkindex+1).zfill(len(str(len(links)))),str(len(links)),str(chapter).zfill(2),driver.title))
					video_file.write(linktitle+','+driver.title+','+videolink+'\n')
				else:
					print("[{0}/{1}][{2}/14] No Video!".format(str(linkindex+1).zfill(len(str(len(links)))),str(len(links)),str(chapter).zfill(2)))
				
				driver.close()
				driver.switch_to_window(driver.window_handles[0])	
	driver.quit()

with open('videos.lst', 'r') as video_file:
	print('\n[Downloading]')
	videos = video_file.readlines()
	for videoindex, video in enumerate(videos):
		vs = video.split(',')
		print("[{0}/{1}] {2}".format(str(videoindex).zfill(len(str(len(videos)))),str(len(videos)),vs[1].strip()))
		os.system("aria2c -x 10 --summary-interval 0 -d 'downloads/{0}' -o '{1}.mp4' '{2}' ".format(vs[0],vs[1],vs[2].strip()))
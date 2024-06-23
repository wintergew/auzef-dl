# auzef-dl

This tool is used to batch-download Istanbul University AUZEF lecture videos. 

## Requirements

* aria2c
* requests (python library)
* BeautifulSoup4 (python library)

## 6.2024 Update
* Rewrote the whole logic of the script based on the updated aos website. Required URLs are also changed to keep the script no-login.
* Replaced selenium with requests and bs4 for speed and simplicity.
* Link formats are also updated, example links can be found in the links.lst file.

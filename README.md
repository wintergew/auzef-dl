# auzef-dl

This tool is used to batch-download Istanbul University AUZEF lecture videos. 

## Requirements

* aria2c
* requests (python library)
* BeautifulSoup4 (python library)

## 6.2024 Update
* Rewrote the whole logic of the script based on the updated aos website. Required URLs are also changed to keep the script no-login.
* Replaced selenium with requests and bs4 for speed and simplicity.
* Link formats are also updated, example link can be found in the links.lst file.
* Refined the code to make it more readable.

## Usage
1. Add Tampermonkey or Greasemonkey extension to your browser.
2. Install linkfetcher userscript.
3. Browse the course page and click on "Konu Anlatımı (Video)" so it loads the video links.
4. You should see a "Extract Links" button in the bottom left corner of the page after installing the userscript. Click on the button to copy the video links. Then, paste them in "links.lst" file.
5. Run "app.py", it will download the videos in "./downloads/".
# auzef-dl

This tool is used to batch-download Istanbul University AUZEF lecture videos. Originally designed to work on Linux, it should also theoretically work on Windows.

## Requirements

* aria2c
* requests (python library)
* BeautifulSoup4 (python library)

## 6.2024 Update
* Rewrote the whole logic of the script based on the updated AOS website. Required URLs are also changed to keep the script no-login.
* Replaced selenium with requests and bs4 for speed and simplicity.
* Added a userscript that extracts video player page links from the course page to the clipboard.
* Changed the app logic to accept links from the terminal, and parses them internally instead of handling them with files.

## Usage
1. Add the Tampermonkey or Greasemonkey extension to your browser.
2. Install linkfetcher userscript.
3. Browse the course page and click on "Konu Anlatımı (Video)" so it loads the video links.
4. You should see an "Extract Links" button in the bottom left corner of the page after installing the userscript. Click on the button to copy the video links. 
5. Run "app.py". Then, paste the links in the script window. It will download the videos in "./downloads/".

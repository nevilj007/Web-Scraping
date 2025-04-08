

---


#  Human-Like Web Scraper (Bypassing Cloudflare) 

This project is a powerful, human-behavior-simulating web scraper written in Python. It uses undetected-chromedriver to bypass sophisticated bot protection mechanisms, including Cloudflare's anti-bot systems, and extracts readable content from web pages.

---

##  Features 

-  Bypasses **Cloudflare and bot detection** using `undetected_chromedriver` 
-  Mimics human behavior with **random delays** 
-  Recursively scrapes links up to a specified **depth** 
-  Saves all cleaned, readable text to a `.txt` file 
-  Automatically follows and scrapes **internal links** 
-  Uses **custom headers** for stealthy HTTP requests 

---

##  Requirements 

Install the required packages:

```bash
pip install undetected-chromedriver beautifulsoup4
```

You also need **Chrome browser** installed.

---

## Usage 

Edit the `__main__` section of the script:

```python
start_url = "https://example.com"   #  The URL you want to scrape 
max_links = 30                      #  Maximum number of links to scrape 
max_depth = 3                       #  How deep to go when following links 
output_file = "knowledgebase.txt"  #  Output file path 
```

Then run the script:

```bash
python scraper.py
```

---

##  Output 

All scraped data will be saved in a `knowledgebase.txt` file in the following format:

```
URL: https://example.com/page1
Content:
<Clean readable text>

--------------------------------------------------------------------------------
```

---

##  How It Works 

- Uses `undetected_chromedriver` to launch a Chrome browser instance.
- Spoofs headers like **User-Agent**, **Referer**, etc.
- Waits random time intervals (2-5 sec) between visits to mimic human interaction.
- Extracts raw text using **BeautifulSoup**.
- Recursively follows internal links, respecting depth and link count limits.

---

##  Disclaimer 

This tool is for **educational and ethical scraping purposes only**. Make sure you are complying with the [robots.txt] (https://www.robotstxt.org/) rules and terms of service of the website you're scraping.



```

---


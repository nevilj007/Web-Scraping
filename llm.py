import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from random import uniform
import time


def human_web_scraper_with_headers_and_chromedriver(start_url, max_links=20, max_depth=3, output_file="knowledgebase.txt"):
    """
    A web scraper that uses undetected-chromedriver with custom headers to bypass bot protection like Cloudflare.
    Mimics human behavior for scraping pages and extracts text content.

    Parameters:
        - start_url (str): The initial URL to start scraping.
        - max_links (int): The maximum number of links to scrape.
        - max_depth (int): The maximum depth of links to crawl.
        - output_file (str): File to save the crawled content.

    Returns:
        str: A message indicating completion and file location.
    """
   
    visited_links = set()
    links_to_crawl = [(start_url, 0)]

   
    options = uc.ChromeOptions()
    options.headless = False  
    options.add_argument("--disable-blink-features=AutomationControlled") 
    driver = uc.Chrome(options=options)

    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://google.com", 
    }

    
    driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": headers["User-Agent"]})
    driver.execute_cdp_cmd("Network.enable", {})
    print("Custom headers applied!")

   
    with open(output_file, "w", encoding="utf-8") as file:
        try:
            while links_to_crawl and len(visited_links) < max_links:
                url, depth = links_to_crawl.pop(0)

               
                if url in visited_links or depth > max_depth:
                    continue

                try:

                    time.sleep(uniform(2, 5)) 

                    
                    driver.get(url)
                    visited_links.add(url)

                   
                    page_source = driver.page_source
                    soup = BeautifulSoup(page_source, "html.parser")
                    page_content = soup.get_text(separator="\n").strip()

                   
                    file.write(f"URL: {url}\n")
                    file.write("Content:\n")
                    file.write(page_content)
                    file.write("\n" + "-" * 80 + "\n")

                   
                    print(f"Visited: {url}")

                   
                    for link in soup.find_all("a", href=True):
                        full_link = urljoin(url, link["href"])
                        if full_link not in visited_links:
                            links_to_crawl.append((full_link, depth + 1))

                except Exception as e:
                    print(f"Failed to process {url}: {e}")

        except KeyboardInterrupt:
            print("Scraper stopped by user.")
        finally:
           
            driver.quit()

    return f"Crawling complete! Content saved to '{output_file}'."



if __name__ == "__main__":

    start_url = "paste the link to be scraped"  
    max_links = 30
    max_depth = 3  
    output_file = "knowledgebase.txt"  

    result = human_web_scraper_with_headers_and_chromedriver(start_url, max_links, max_depth, output_file)
    print(result)

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
    # Initialize visited links and links to crawl
    visited_links = set()
    links_to_crawl = [(start_url, 0)]  # (url, depth)

    # Start an undetected Chrome driver instance
    options = uc.ChromeOptions()
    options.headless = False  # Run in headless mode (set to True if you don't need a visible browser)
    options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection
    driver = uc.Chrome(options=options)

    # Define headers to mimic a real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://google.com",  # Mimics coming from a search engine
    }

    # Add headers to the Chrome instance
    driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": headers["User-Agent"]})
    driver.execute_cdp_cmd("Network.enable", {})
    print("Custom headers applied!")

    # Open the output file for writing
    with open(output_file, "w", encoding="utf-8") as file:
        try:
            while links_to_crawl and len(visited_links) < max_links:
                url, depth = links_to_crawl.pop(0)

                # Skip if URL is already visited or depth exceeds the limit
                if url in visited_links or depth > max_depth:
                    continue

                try:

                    time.sleep(uniform(2, 5))  # Random delay between 2 to 5 seconds

                    # Use the undetected-chromedriver to open the URL
                    driver.get(url)
                    visited_links.add(url)

                    # Extract page content using BeautifulSoup
                    page_source = driver.page_source
                    soup = BeautifulSoup(page_source, "html.parser")
                    page_content = soup.get_text(separator="\n").strip()

                    # Save the page content to the file
                    file.write(f"URL: {url}\n")
                    file.write("Content:\n")
                    file.write(page_content)
                    file.write("\n" + "-" * 80 + "\n")

                    # Print progress
                    print(f"Visited: {url}")

                    # Extract and queue links for crawling
                    for link in soup.find_all("a", href=True):
                        full_link = urljoin(url, link["href"])
                        if full_link not in visited_links:
                            links_to_crawl.append((full_link, depth + 1))

                except Exception as e:
                    print(f"Failed to process {url}: {e}")

        except KeyboardInterrupt:
            print("Scraper stopped by user.")
        finally:
            # Close the browser
            driver.quit()

    return f"Crawling complete! Content saved to '{output_file}'."


# Example usage
if __name__ == "__main__":

    start_url = "paste the link to be scraped"  # The website to scrape
    max_links = 30# Maximum number of links to scrape
    max_depth = 3  # Maximum depth of recursive crawling
    output_file = "knowledgebase.txt"  # Output file to save scraped content

    result = human_web_scraper_with_headers_and_chromedriver(start_url, max_links, max_depth, output_file)
    print(result)

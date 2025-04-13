import requests
from bs4 import BeautifulSoup
import random
import unittest
from urllib.parse import urljoin
class BaseScraper:
    def __init__(self,url):
        self.url = url
        self.headers = {"User-Agent":random.choice(self._get_user_agents())}
        self.data = None
    
    def _get_user_agents(self):
         return [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0)...",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)..."
        ]
    
    def fetch_data(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                self.data = response.content
            else:
                print(f"Failed to fetch data. Status: {response.status_code}")
        except Exception as e:
            print(f"Error occurred while fetching data: {e}")


class BBCScraper(BaseScraper):
    def __init__(self):
        super().__init__("https://www.bbc.com/")
        self.all_links=[] 
    
    # -------------Scraping BBC News Headlines Logic---------------------
    def scrape_headlines(self):
        if not self.data:
            print("No data to scrape. Please Fetch Data first.")
            return
        
        self.all_links = []
        try:
            soup = BeautifulSoup(self.data,'html.parser')

            for link in soup.find_all('a',href=True):
                headline_name = link.get_text(strip=True)
                href = link['href']
            
                if "articles" in href:
                    full_url = urljoin(self.url,href)
                    img_tag = link.find_previous('img',src=True)
                    img_url = img_tag['src'] if img_tag else None
                    full_img_url = urljoin(self.url,img_url) if img_url else None
                    self.all_links.append((headline_name,full_url,full_img_url))
                    
            if not self.all_links:
                print("No Headlines Found")
        except Exception as e:
            print(f"An Error Occured {e}")
    # -------------Scraping BBC News Headlines Logic End---------------------

class ScrapURLContent(BaseScraper):
    def __init__(self,url):
        super().__init__(url)
        self.all_content = []

    def scrap_url_content(self):
        if not self.data:
            print("No data to scrape. Please Fetch Data first.")
            return
        try:
            soup = BeautifulSoup(self.data,'html.parser')
            article = soup.find('article')
            # title = soup.find_all('h1')
            # paragraph = soup.find_all('p')
            if article:
                for tag in article.find_all(['h1', 'p']):
                    content = tag.text
                    self.all_content.append(content)
                print(self.all_content)
        except Exception as e:
            print(f"An Error Occured {e}")

# if __name__ == "__main__":
#     article = ScrapURLContent("https://www.bbc.com/news/articles/cn80r185vmro")
#     article.fetch_data()
#     article.scrap_url_content()
    # news = BBCScraper()
    # news.fetch_data()
    # news.scrape_headlines()
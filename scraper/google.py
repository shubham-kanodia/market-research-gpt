import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, urlparse

from scraper.headers import HEADERS

import json
import time


class GoogleScraper:
    def __init__(self):
        self.BASE_URL = "https://www.google.com/search"
        self.MIN_CHUNK_LEN = 50

    def _process_keyword(self, keyword):
        return "+".join(keyword.split(" "))

    @staticmethod
    def _process_link(link):
        link = unquote(link)
        link = link.split("&")[0]

        domain = urlparse(link).netloc

        if "google" in domain:
            link = ""
        if link.endswith(".pdf"):
            link = ""
        return link

    @staticmethod
    def _make_search_request(url):
        response = requests.get(url, headers=HEADERS)

        if response.status_code == 200:
            html_code = response.content
            return html_code

        else:
            raise Exception("Request Failed")

    def _get_links(self, keyword):
        processed_keyword = self._process_keyword(keyword)
        search_url = f"{self.BASE_URL}?q={processed_keyword}"

        html_code = self._make_search_request(search_url)

        soup = BeautifulSoup(html_code, 'html.parser')

        search_results = soup.find_all('a')

        links = []

        for link in search_results:
            if link:
                href = link['href']

                if href[0:7] == "/url?q=":
                    links.append(href[7:])

        return [self._process_link(link) for link in links if self._process_link(link) != ""]

    def scrape_text(self, url: str):
        response = self._make_search_request(url)

        soup = BeautifulSoup(response, "html.parser")

        for script in soup(["script", "style"]):
            script.extract()

        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = "\n".join(chunk for chunk in chunks if len(chunk) > self.MIN_CHUNK_LEN)

        return text

    def get_data(self, keywords_list):
        data = {}
        for keywords in keywords_list:
            search_links = self._get_links(keywords)

            for link in search_links:
                try:
                    text = self.scrape_text(link)

                    data[keywords] = data.get(keywords, []) + [text]

                except Exception as exp:
                    continue

                time.sleep(0.1)

            print("Completed 1 keyword")
        return data

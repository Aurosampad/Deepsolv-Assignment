# web_crawler_module.py
import requests
from bs4 import BeautifulSoup

class WebCrawler:
    def warmup(self):
        pass  # Optional setup

    def run(self, url, word_count_threshodl, extraction_startegy, bypass_cache=False):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            html_content = response.text

            # Use BeautifulSoup to extract plain text (you can enhance this)
            soup = BeautifulSoup(html_content, "html.parser")
            cleaned_text = soup.get_text(separator="\n", strip=True)

            # Simulate a result object similar to what LLMExtractionStrategy might expect
            class Result:
                def __init__(self, content):
                    self.extracted_content = extraction_startegy.extract_text(content)

            return Result(cleaned_text)

        except requests.RequestException as e:
            raise ValueError(f"Request failed: {e}")

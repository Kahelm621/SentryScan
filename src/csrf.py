# src/csrf.py
from bs4 import BeautifulSoup

class CSRFScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def has_csrf_token(self):
        response = requests.get(self.target_url)
        soup = BeautifulSoup(response.text, 'lxml')
        csrf_token = soup.find("input", {"name": "csrf_token"})
        return csrf_token is not None
# src/xss.py
class XSSScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def is_vulnerable(self):
        test_payload = "<script>alert('XSS');</script>"
        response = requests.get(self.target_url + "?input=" + test_payload)
        if test_payload in response.text:
            return True
        return False
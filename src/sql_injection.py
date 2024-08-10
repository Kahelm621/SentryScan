# src/sql_injection.py
class SQLInjectionScanner:
    def __init__(self, target_url):
        self.target_url = target_url
    
    def is_vulnerable(self):
        test_payloads = ["' OR '1'='1", "'; DROP TABLE users; --"]
        for payload in test_payloads:
            response = requests.get(self.target_url + payload)
            if "error" in response.text.lower():
                return True
        return False
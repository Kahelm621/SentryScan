# src/scanner.py
import requests
from sql_injection import SQLInjectionScanner
from xss import XSSScanner
from csrf import CSRFScanner

class WebVulnScanner:
    def __init__(self, target_url):
        self.target_url = target_url
        self.vulnerabilities = []

    def scan(self):
        print(f"Scanning {self.target_url} for vulnerabilities...")
        self.scan_sql_injection()
        self.scan_xss()
        self.scan_csrf()
        self.generate_report()

    def scan_sql_injection(self):
        sql_scan = SQLInjectionScanner(self.target_url)
        if sql_scan.is_vulnerable():
            self.vulnerabilities.append("SQL Injection Vulnerability Found")

    def scan_xss(self):
        xss_scan = XSSScanner(self.target_url)
        if xss_scan.is_vulnerable():
            self.vulnerabilities.append("XSS Vulnerability Found")

    def scan_csrf(self):
        csrf_scan = CSRFScanner(self.target_url)
        if not csrf_scan.has_csrf_token():
            self.vulnerabilities.append("CSRF Vulnerability Found")

    def generate_report(self):
        print("Scan complete. Reporting:")
        for vulnerability in self.vulnerabilities:
            print(vulnerability)

if __name__ == "__main__":
    target = input("Enter the URL to scan: ")
    scanner = WebVulnScanner(target)
    scanner.scan()
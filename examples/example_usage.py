# examples/example_usage.py
from src.scanner import WebVulnScanner

target_url = "http://your-test-url.com"
scanner = WebVulnScanner(target_url)
scanner.scan()
# SentryScan

A beginner-friendly Python web application vulnerability scanner. It sends simple test requests to a target URL and checks the responses for common signs of SQL injection, cross-site scripting (XSS) and missing CSRF protection.

> ⚠️ **For learning and authorized testing only.** Only scan websites you own or have written permission to test.

## Features
- **SQL injection check:** appends test payloads (such as `' OR '1'='1`) to the URL and flags the page if the response contains the word "error".
- **Reflected XSS check:** sends a `<script>` payload in an `input` query parameter and flags the page if the payload is reflected back unchanged.
- **CSRF check:** parses the page with BeautifulSoup and flags it if no `<input name="csrf_token">` field is found.
- **Console report:** prints each finding when the scan finishes.

These are simple heuristic checks meant to show the concepts. They are not a replacement for professional security tools.

## Tech Stack
- Python 3
- [requests](https://pypi.org/project/requests/)
- [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/) with the `lxml` parser

## How to Run
```bash
git clone https://github.com/Kahelm621/SentryScan.git
cd SentryScan
pip install -r requirements.txt
python -m src.scanner
# Enter the URL to scan when prompted
```

See `examples/example_usage.py` for using `WebVulnScanner` from your own code.

## Project Structure
```
SentryScan/
├── src/
│   ├── scanner.py         # WebVulnScanner: runs all checks and prints the report
│   ├── sql_injection.py   # SQLInjectionScanner
│   ├── xss.py             # XSSScanner
│   └── csrf.py            # CSRFScanner
├── tests/                 # Test files for each scanner
├── examples/example_usage.py
├── docs/user_guide.md
├── requirements.txt
└── LICENSE
```

## License
MIT. See [LICENSE](LICENSE).

gh auth refresh -h github.com -s workflow

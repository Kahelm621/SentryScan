import unittest
from unittest.mock import patch

from src.scanner import WebVulnScanner


class TestWebVulnScanner(unittest.TestCase):
    @patch("src.scanner.CSRFScanner")
    @patch("src.scanner.XSSScanner")
    @patch("src.scanner.SQLInjectionScanner")
    def test_collects_findings(self, mock_sql, mock_xss, mock_csrf):
        mock_sql.return_value.is_vulnerable.return_value = True
        mock_xss.return_value.is_vulnerable.return_value = False
        mock_csrf.return_value.has_csrf_token.return_value = False

        scanner = WebVulnScanner("http://example.com")
        scanner.scan()

        self.assertEqual(
            scanner.vulnerabilities,
            ["SQL Injection Vulnerability Found", "CSRF Vulnerability Found"],
        )


if __name__ == "__main__":
    unittest.main()

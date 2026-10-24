import unittest
from unittest.mock import patch, Mock

from src.xss import XSSScanner

PAYLOAD = "<script>alert('XSS');</script>"


class TestXSSScanner(unittest.TestCase):
    @patch("src.xss.requests.get")
    def test_reflected_payload_is_flagged(self, mock_get):
        mock_get.return_value = Mock(text=f"<p>You searched for {PAYLOAD}</p>")
        self.assertTrue(XSSScanner("http://example.com/search").is_vulnerable())

    @patch("src.xss.requests.get")
    def test_escaped_payload_is_safe(self, mock_get):
        mock_get.return_value = Mock(text="<p>You searched for &lt;script&gt;</p>")
        self.assertFalse(XSSScanner("http://example.com/search").is_vulnerable())


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch, Mock

from src.sql_injection import SQLInjectionScanner


class TestSQLInjectionScanner(unittest.TestCase):
    @patch("src.sql_injection.requests.get")
    def test_safe_page_is_not_vulnerable(self, mock_get):
        mock_get.return_value = Mock(text="<html>Welcome</html>")
        self.assertFalse(SQLInjectionScanner("http://example.com/?id=").is_vulnerable())

    @patch("src.sql_injection.requests.get")
    def test_sql_error_is_flagged(self, mock_get):
        mock_get.return_value = Mock(text="You have an error in your SQL syntax")
        self.assertTrue(SQLInjectionScanner("http://example.com/?id=").is_vulnerable())


if __name__ == "__main__":
    unittest.main()

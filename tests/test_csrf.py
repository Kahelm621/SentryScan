import unittest
from unittest.mock import patch, Mock

from src.csrf import CSRFScanner


class TestCSRFScanner(unittest.TestCase):
    @patch("src.csrf.requests.get")
    def test_form_with_token(self, mock_get):
        mock_get.return_value = Mock(text='<form><input name="csrf_token" value="abc"></form>')
        self.assertTrue(CSRFScanner("http://example.com/login").has_csrf_token())

    @patch("src.csrf.requests.get")
    def test_form_without_token(self, mock_get):
        mock_get.return_value = Mock(text='<form><input name="username"></form>')
        self.assertFalse(CSRFScanner("http://example.com/login").has_csrf_token())


if __name__ == "__main__":
    unittest.main()

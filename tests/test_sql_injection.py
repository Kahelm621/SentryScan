# tests/test_sql_injection.py
import unittest
from src.sql_injection import SQLInjectionScanner

class TestSQLInjectionScanner(unittest.TestCase):
    def test_vuln_detection(self):
        sql_scan = SQLInjectionScanner("http://example.com")
        self.assertFalse(sql_scan.is_vulnerable())

if __name__ == '__main__':
    unittest.main()
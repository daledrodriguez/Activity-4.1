import unittest
import re

class TestPCIPAndMACFormat(unittest.TestCase):
    def test_ip_format(self):
        ip_address = "192.168.443gf.25"
        # Regular expression to validate an IPv4 address
        ip_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
        self.assertRegex(ip_address, ip_pattern)

    def test_mac_format(self):
        mac_address = "00:1A:2B:3Cgf55:4D:5E"
        # Regular expression to validate a MAC address
        mac_pattern = r"^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$"
        self.assertRegex(mac_address, mac_pattern)

if __name__ == '__main__':
    unittest.main()

import unittest

class TestDeviceLocationAndIP(unittest.TestCase):
    def test_location_and_ip(self):
        device_info = {
            'location': 'TIP_Manila',
            'ip_address': '192.168.45.25',
            'subnet_mask': '255.255.255.0'
        }

        self.assertEqual(device_info['location'], 'TIP_QC')
        self.assertEqual(device_info['ip_address'], '192.168.45.25')
        self.assertEqual(device_info['subnet_mask'], '255.255.255.0')

if __name__ == '__main__':
    unittest.main()

import unittest

class TestDeviceType(unittest.TestCase):
    def test_device_type(self):
        device_type = "pc"  # Example device type
        
        valid_device_types = ["router", "personal computer", "switch", "server"]
        self.assertIn(device_type, valid_device_types)

if __name__ == '__main__':
    unittest.main()

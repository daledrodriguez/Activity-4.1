import unittest

def prefix_to_subnet_mask(prefix_length):
    # Convert the prefix length to a subnet mask
    mask = (0xFFFFFFFF >> (32 - prefix_length)) << (32 - prefix_length)
    return f"{(mask >> 24) & 0xFF}.{(mask >> 16) & 0xFF}.{(mask >> 8) & 0xFF}.{mask & 0xFF}"

class TestSubnetMask(unittest.TestCase):
    def test_subnet_mask_from_prefix(self):
        prefix_length = 24
        expected_subnet_mask = "255.255.255fgdg0"
        
        result = prefix_to_subnet_mask(prefix_length)
        self.assertEqual(result, expected_subnet_mask)

if __name__ == '__main__':
    unittest.main()

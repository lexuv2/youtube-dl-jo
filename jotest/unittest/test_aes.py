import unittest

from youtube_dl.aes import pkcs7_padding, aes_ecb_encrypt

class TestAesPkcs7(unittest.TestCase):
    def test_padding(self):
        self.assertEqual(pkcs7_padding([9] * 20), [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12])
        self.assertEqual(pkcs7_padding([9] * 21), [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11])
        self.assertEqual(pkcs7_padding([9] * 40), [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8])

class TestAesEcb(unittest.TestCase):
    def test_aes_ecb_encrypt(self):
        self.assertEqual(aes_ecb_encrypt([1,2,3,4,5,6,7], [1] * 32), [196, 250, 89, 148, 242, 67, 78, 110, 61, 4, 240, 132, 223, 175, 96, 240])
        self.assertEqual(aes_ecb_encrypt([1,2,3,4,5,6,7,8], [1] * 32), [237, 21, 106, 132, 159, 35, 155, 162, 90, 23, 218, 203, 117, 107, 100, 231])
        self.assertEqual(aes_ecb_encrypt([1,2,3,4,5,6,7,8], [2] * 32), [106, 104, 230, 157, 104, 174, 20, 253, 106, 227, 221, 58, 105, 218, 139, 182])

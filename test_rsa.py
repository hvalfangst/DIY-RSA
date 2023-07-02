# diy_rsa_tests.py

import unittest
from diy_rsa import gcd, extended_gcd, mod_pow, is_prime, generate_rsa_key, rsa_encrypt, rsa_decrypt


class RSATestCase(unittest.TestCase):

    def test_rsa_encrypt_and_decrypt(self):
        n, e, d = generate_rsa_key(64)
        plaintext = 42
        print("Plain text:", plaintext)
        ciphertext = rsa_encrypt(plaintext, e, n)
        print("Cipher text:", ciphertext)
        decrypted_text = rsa_decrypt(ciphertext, d, n)
        print("Decrypted test:", decrypted_text)
        self.assertEqual(plaintext, decrypted_text)


if __name__ == '__main__':
    unittest.main()

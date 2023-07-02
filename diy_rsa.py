import random


# Euclidean algorithm for finding the greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Extended Euclidean algorithm for finding modular inverse
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd_outer, x, y = extended_gcd(b % a, a)
        return gcd_outer, y - (b // a) * x, x


# Modular exponentiation
def mod_pow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent >>= 1
    return result


# Generate random prime number based on the number of supplied bits and returns it if prime
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if num % 2 != 0 and is_prime(num):
            return num


# Check if a number is prime
def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num <= 1 or num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


# RSA key generation
def generate_rsa_key(bits):
    # Choose two prime numbers
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    print("Prime numbers:")
    print("p:", p)
    print("q:", q)
    print("- - - - - - - - - - - - - - - ")

    # Compute n and phi(n)
    n = p * q
    phi = (p - 1) * (q - 1)
    print("Key Generation:")
    print("Compute n and phi(n):")
    print("n:", n)
    print("phi(n):", phi)
    print("- - - - - - - - - - - - - - - ")

    # Choose public key e
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    print("Choose public key e:")
    print("e:", e)
    print("- - - - - - - - - - - - - - - ")

    # Compute private key d
    _, d, _ = extended_gcd(e, phi)
    d %= phi
    print("Compute private key d:")
    print("d:", d)
    print("- - - - - - - - - - - - - - - ")

    return n, e, d


# RSA encryption
def rsa_encrypt(message, e, n):
    return mod_pow(message, e, n)


# RSA decryption
def rsa_decrypt(ciphertext, d, n):
    return mod_pow(ciphertext, d, n)


# Test the RSA encryption and decryption
def main():
    # Key generation
    bits = 64
    print("Bits:", bits)
    print("- - - - - - - - - - - - - - - ")
    n, e, d = generate_rsa_key(bits)
    print("Public key (n, e):")
    print("n:", n)
    print("e:", e)
    print("- - - - - - - - - - - - - - - ")
    print("Private key (n, d):")
    print("n:", n)
    print("d:", d)
    print("- - - - - - - - - - - - - - - ")

    # Message to encrypt
    message = 42
    print("Original message:")
    print("M:", message)
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    # Encryption
    ciphertext = rsa_encrypt(message, e, n)
    print("Encryption:")
    print("Apply the encryption formula: C = M^e mod N")
    print("C = ", message, "^", e, "mod", n)
    print("C = ", ciphertext)
    print("The ciphertext C is", ciphertext)
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    # Decryption
    decrypted_message = rsa_decrypt(ciphertext, d, n)
    print("Decryption:")
    print("Apply the decryption formula: M = C^d mod N")
    print("M = ", ciphertext, "^", d, "mod", n)
    print("M = ", decrypted_message)
    print("The decrypted message M is", decrypted_message)


if __name__ == '__main__':
    main()

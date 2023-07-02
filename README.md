# Do It Yourself: RSA

This piece of code demonstrates the underlying steps that comprise the RSA algorithm utilizing Python. A modest (and highly insecure) bit size of 64 have been chosen merely to for sake of ease wrt piping results to terminal.

## Trivia

RSA (Rivest-Shamir-Adleman) is a widely used public-key encryption algorithm that allows secure communication over insecure networks. It utilizes the properties of prime numbers (see last section) and modular arithmetic to provide confidentiality and data integrity.


## Prerequisites

    Python 3.x

## Usage

1. Clone the repository or download the rsa_example.py file.
2. Open a terminal or command prompt and navigate to the directory where you saved the rsa_example.py file.
3. Run the program by executing the command: python diy_rsa.py.

## Gist

The program generates a pair of RSA keys with a specified number of bits and uses them to encrypt and decrypt a sample message. The output is displayed in the terminal, showing the generated prime numbers, key generation steps, original message, encryption steps, and the decrypted message.

## Functions Overview

The code consists of several functions that perform various operations involved in the RSA encryption and decryption process. Here's a brief explanation of each function:

* gcd(a, b): Implements the Euclidean algorithm to calculate the greatest common divisor of two numbers a and b.
* extended_gcd(a, b): Implements the Extended Euclidean algorithm to find the modular inverse of a modulo b.
* mod_pow(base, exponent, modulus): Performs modular exponentiation efficiently using the binary method.
* generate_prime(bits): Generates a random prime number with the specified number of bits.
* is_prime(num): Checks whether a number is prime.
* generate_rsa_key(bits): Generates a pair of public and private keys for RSA encryption. It chooses two random prime numbers, computes the modulus and Euler's totient function, selects a public key, and calculates the corresponding private key.
* rsa_encrypt(message, e, n): Encrypts a given message using the public key and modulus.
* rsa_decrypt(ciphertext, d, n): Decrypts a ciphertext using the private key and modulus.
* main(): The main function where the key generation, encryption, and decryption are demonstrated.


## Prime Numbers
RSA encryption algorithm utilizes the properties of prime numbers and modular arithmetic in the following ways:

* Key Generation: The first step in RSA is to generate a pair of public and private keys. This involves selecting two distinct prime numbers, typically denoted as p and q. These prime numbers are used to construct the modulus N by computing N = p * q. The security of RSA relies on the difficulty of factoring large composite numbers into their prime factors.


* Euler's Totient Function: The next step is to calculate Euler's totient function (φ(N)) for the modulus N. Euler's totient function counts the number of positive integers less than N that are coprime with N. For RSA, φ(N) is computed as (p - 1) * (q - 1). Euler's totient function is crucial for selecting the public exponent e and calculating the private exponent d.


* Public Key Encryption: The public key consists of the modulus N and the public exponent e. The public exponent is selected as an integer e that is coprime with φ(N). This ensures that the encryption process is reversible. The message to be encrypted is raised to the power of e modulo N, using modular exponentiation. The resulting ciphertext is the encrypted form of the original message.


* Private Key Decryption: The private key consists of the modulus N and the private exponent d. The private exponent is calculated using the Extended Euclidean Algorithm, which finds the modular inverse of the public exponent e modulo φ(N). The modular inverse allows for the decryption process. The ciphertext is raised to the power of d modulo N using modular exponentiation, resulting in the original plaintext message.


* Modular Arithmetic: Modular arithmetic plays a crucial role in both encryption and decryption steps. Modular exponentiation ensures that the calculations are performed efficiently and remain within the range of the modulus N. It allows for the encryption and decryption operations to be reversible and computationally feasible.


By leveraging the properties of prime numbers, RSA provides a secure encryption scheme. The difficulty of factoring large composite numbers into their prime factors makes it computationally infeasible to break the encryption without the private key. The use of modular arithmetic ensures that the encryption and decryption operations can be performed efficiently and consistently within the defined modulus.

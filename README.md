XOR Encryption and Decryption

This project contains a simple implementation of XOR-based encryption and decryption in Python. The provided scripts demonstrate how to encrypt and decrypt messages using XOR operations with a given key, and convert between plaintext, encrypted text, and hexadecimal representations.
Overview

    Encryption:
        The xor_encrypt function takes a plaintext message and a key to produce an encrypted message.
        The encryption process uses XOR operations between the ASCII values of the message characters and the key characters.

    Decryption:
        The xor_decrypt function takes an encrypted message and the same key used for encryption to return the original plaintext message.
        The decryption process is essentially the same as encryption due to the reversible nature of XOR.

    Hex Conversion:
        The to_hex_string function converts an encrypted message to a hexadecimal string for easier display and storage.
        The from_hex_string function converts a hexadecimal string back to the encrypted message.

Files

    xor_encrypt_decrypt.py: Contains functions for XOR encryption, decryption, and conversion between text and hexadecimal.

Usage
Encryption

    Input:
        The user is prompted to enter a plaintext message and a key.
    Output:
        The script will output the encrypted message in hexadecimal format.

Decryption

    Input:
        The user is prompted to enter the encrypted message (in hexadecimal format) and the key used for encryption.
    Output:
        The script will output the decrypted plaintext message.

Example
Encrypting a Message


Enter the message to encrypt: Hello, XOR!
Enter the key: key
Encrypted message (hex): 7d4c0b7d1d0f0c0d7e7d3e1e1b


Decrypting a Message


Enter the encrypted message (hex): 7d4c0b7d1d0f0c0d7e7d3e1e1b
Enter the key: key
Decrypted message: Hello, XOR!


Code Details
xor_encrypt(message, key)

    Encrypts a message using XOR with the provided key.
    Returns the encrypted message as a string.

xor_decrypt(encrypted_message, key)

    Decrypts an XOR-encrypted message using the provided key.
    Returns the original plaintext message.

to_hex_string(s)

    Converts a string to its hexadecimal representation.

from_hex_string(hex_string)

    Converts a hexadecimal string back to a regular string.

Requirements

    Python 3.x

License

This project is licensed under the MIT License. See the LICENSE file for more details.

import time
import random


#This function encrypts a plaintext message using a simple symmetric encryption algorithm.
def saes_encrypt(plaintext, key):
    # Encrypts the plaintext by performing an XOR operation between 
    # each character's ASCII value and the key, then converts it back to a character.
    # The key is expected to be a number between 0 and 255.
    encrypted = ''.join(chr(ord(c) ^ key) for c in plaintext)
    return encrypted

# This function decrypts a ciphertext message that was encrypted using the same key.
def saes_decrypt(ciphertext, key):
    # Decrypts the ciphertext by performing an XOR operation between 
    # each character's ASCII value and the key, similar to the encryption process.
    # Since XOR is its own inverse, applying it again with the same key decrypts the message.
    decrypted = ''.join(chr(ord(c) ^ key) for c in ciphertext)
    return decrypted

# Automatically generate a numerical key (0-255)
key = random.randint(0, 255)
print(f"Generated Key: {key}")

plaintext = input("Enter your message: ")

start_time = time.perf_counter()
encrypted = saes_encrypt(plaintext, key)
end_time = time.perf_counter()
encryption_time = end_time - start_time

start_time = time.perf_counter()
decrypted = saes_decrypt(encrypted, key)
end_time = time.perf_counter()
decryption_time = end_time - start_time

print(f"Encrypted: {encrypted}")
print(f"Encryption Time: {encryption_time:.6f} seconds.")
print(f"Decrypted: {decrypted}")
print(f"Decryption Time: {decryption_time:.6f} seconds.")

import random
import math
import time

# The function checks if a number is prime. Test
def is_prime(number): 
    if number < 2: # Any number less than 2 is not prime
        return False
    for i in range(2, int(math.sqrt(number)) + 1): # Loop from 2 to sqrt(number) + 1
        if number % i == 0: # If number is divisible by i, it's not prime
            return False
    return True  # If no divisors found, number is prime


# Generates a random prime number within a specified range.
def generate_prime(min_value, max_value): 
    prime = random.randint(min_value, max_value) # Generate a random number within range
    while not is_prime(prime):  # Keep generating if not prime
        prime = random.randint(min_value, max_value)
    return prime # Return the prime number


# Calculates the modular inverse of e modulo phi.
def mod_inverse(e, phi): 
    for d in range(3, phi): # Start loop from 3 to phi
        if (d * e) % phi == 1:
            return d # d is the modular inverse
    raise ValueError("Mod Inverse does not exist.")  # If not found, raise error

# Generate primes p and q
p, q = generate_prime(1, 100), generate_prime(1, 100)
while p == q:
    q = generate_prime(1, 100)

# Calculate n and phi(n)
n = p * q
phi_n = (p - 1) * (q - 1)

# Choose e
e = random.randint(3, phi_n - 1)
while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n - 1)

# Calculate d
d = mod_inverse(e, phi_n)

print("Public Key (e):", e)
print("Private Key (d):", d)
print("n:", n)
print("Phi of n:", phi_n)
print("p:", p)
print("q:", q)

# Prompt the user to enter a message
print("\n")
message = input("Enter your message: ")

start_time = time.perf_counter() # Start timing for encryption

# Encode and encrypt the message
message_encoded = [ord(c) for c in message] #converts each character to ASCII 
ciphertext = [pow(c, e, n) for c in message_encoded]

end_time = time.perf_counter() # End timing
encryption_time = end_time - start_time # Calculate duration
print("\n")
print("Ciphertext:", ciphertext)
print(f"Encryption took {encryption_time:.6f} seconds.")

start_time = time.perf_counter() # Start timing for decryption

# Decrypt the message
message_decoded = [pow(ch, d, n) for ch in ciphertext]
decrypted_message = "".join(chr(ch) for ch in message_decoded)

end_time = time.perf_counter() # End timings
decryption_time = end_time - start_time # Calculate duration
print("\n")
print("Decrypted message:", decrypted_message)
print(f"Decryption took {decryption_time:.6f} seconds.")

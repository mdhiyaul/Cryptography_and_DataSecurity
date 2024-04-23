import matplotlib.pyplot as plt


# Mock data for RSA
rsa_message_size = [10, 20, 30, 40]
rsa_encryption_time = [0.000138, 0.000270, 0.000300, 0.000343]
rsa_decryption_time = [0.000250, 0.000511, 0.000667, 0.000891]

# Mock data for S-AES
saes_message_size = [10, 20, 30, 40]
saes_encryption_time = [0.000272, 0.000421, 0.000562, 0.000812]
saes_decryption_time = [0.000186, 0.000327, 0.000464, 0.000731]

# Plot the merged graph with the legend outside
plt.figure(figsize=(10, 6))

# Plot RSA data
plt.plot(rsa_message_size, rsa_encryption_time, label='RSA Encryption Time', color='orange', marker='o')
plt.plot(rsa_message_size, rsa_decryption_time, label='RSA Decryption Time', color='blue', marker ='o')

# Plot S-AES data
plt.plot(saes_message_size, saes_encryption_time, label='S-AES Encryption Time', color='red', linestyle='dashed', marker='x')
plt.plot(saes_message_size, saes_decryption_time, label='S-AES Decryption Time', color='green', linestyle='dashed', marker='x')

# Adding labels and title
plt.xlabel('Message Size (words)')
plt.ylabel('Time (seconds)')
plt.title('RSA vs S-AES Runtime Efficiency Comparison')

# Place the legend outside the plot area
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Make the plot layout fit the legend
plt.tight_layout()

plt.grid(True)

# Display the merged graph
plt.show()
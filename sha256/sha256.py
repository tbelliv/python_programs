import math

# Helper function to convert a string into binary representation
def translate(message):
    bincharslist = [bin(ord(c))[2:].zfill(8) for c in message]  # Convert string to binary
    bincharscat = ''.join(bincharslist)
    bitlength = len(bincharscat)
    return bincharscat, bitlength

# Function to pad the binary string to ensure it's 448 bits long
def rounding(bincharscat):
    bincharscat += '1'  # Append '1'
    while len(bincharscat) % 512 != 448:
        bincharscat += '0'
    return bincharscat

# Function to append the length of the original message as a 64-bit binary
def append64str(bincharscat, bitlength):
    binbitlength = bin(bitlength)[2:].zfill(64)  # Ensure the bitlength is 64 bits long
    bincharscat = bincharscat + binbitlength
    return bincharscat

# Function to split the binary string into chunks of a given size
def split_into_chunks(bincharscat, chunk_size=32):
    return [bincharscat[i:i + chunk_size] for i in range(0, len(bincharscat), chunk_size)]

# Helper function to convert a fractional part to binary with specified precision
def fractional_to_binary(num, k_precision):
    binary = ""
    while k_precision:
        num *= 2
        bit = int(num)
        num -= bit
        binary += '1' if bit == 1 else '0'
        k_precision -= 1
    return binary

# Helper function to convert binary string to hexadecimal
def binary_to_hex(binary_str):
    return hex(int(binary_str, 2))[2:].zfill(len(binary_str) // 4)

# Function to compute the initial hash values (square roots of the first 8 primes)
def compute_initial_hash_values():
    primes_8 = [2, 3, 5, 7, 11, 13, 17, 19]
    hex_values_sqrt = {}
    for i, prime in enumerate(primes_8):
        h0 = math.sqrt(prime)
        fractional_part = h0 - int(h0)
        binary_fractional_part = fractional_to_binary(fractional_part, 32)
        hex_string = ''.join(binary_to_hex(binary_fractional_part[j:j + 4]) for j in range(0, len(binary_fractional_part), 4))
        hex_values_sqrt[f'h{i}'] = hex_string
    return hex_values_sqrt

# Function to compute cube roots of the first 64 primes
def compute_cube_roots():
    primes_64 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
                 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
                 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
                 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]
    hex_values_cubert = {}
    for i, prime in enumerate(primes_64):
        k0 = prime ** (1/3)
        fractional_part = k0 - int(k0)
        binary_fractional_part = fractional_to_binary(fractional_part, 32)
        hex_string = ''.join(binary_to_hex(binary_fractional_part[j:j + 4]) for j in range(0, len(binary_fractional_part), 4))
        hex_values_cubert[f'k{i}'] = hex_string
    return hex_values_cubert

# Helper function for bitwise rotation
def right_rotate(value, shift):
    return ((value >> shift) | (value << (32 - shift))) & 0xFFFFFFFF

# Function to process the hashed values (SHA-256 hash computation)
def hashval(bincharscat, chunks):
    # Initialize hash values with the computed initial values
    h = [int(hex_values_sqrt[f'h{i}'], 16) for i in range(8)]

    # Extend the first 16 words into 64 words
    w = [int(chunk, 2) for chunk in chunks[:16]]
    for i in range(16, 64):
        s0 = (right_rotate(w[i-15], 7) ^ right_rotate(w[i-15], 18) ^ (w[i-15] >> 3))
        s1 = (right_rotate(w[i-2], 17) ^ right_rotate(w[i-2], 19) ^ (w[i-2] >> 10))
        w.append((w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFF)

    # Compression function
    a, b, c, d, e, f, g, h = h
    for i in range(64):
        S1 = (right_rotate(e, 6) ^ right_rotate(e, 11) ^ right_rotate(e, 25))
        ch = (e & f) ^ (~e & g)
        temp1 = (h + S1 + ch + int(hex_values_cubert[f'k{i}'], 16) + w[i]) & 0xFFFFFFFF
        S0 = (right_rotate(a, 2) ^ right_rotate(a, 13) ^ right_rotate(a, 22))
        maj = (a & b) ^ (a & c) ^ (b & c)
        temp2 = (S0 + maj) & 0xFFFFFFFF

        h = g
        g = f
        f = e
        e = (d + temp1) & 0xFFFFFFFF
        d = c
        c = b
        b = a
        a = (temp1 + temp2) & 0xFFFFFFFF

    # Add the compressed chunk to the current hash value
    h0 = (int(hex_values_sqrt['h0'], 16) + a) & 0xFFFFFFFF
    h1 = (int(hex_values_sqrt['h1'], 16) + b) & 0xFFFFFFFF
    h2 = (int(hex_values_sqrt['h2'], 16) + c) & 0xFFFFFFFF
    h3 = (int(hex_values_sqrt['h3'], 16) + d) & 0xFFFFFFFF
    h4 = (int(hex_values_sqrt['h4'], 16) + e) & 0xFFFFFFFF
    h5 = (int(hex_values_sqrt['h5'], 16) + f) & 0xFFFFFFFF
    h6 = (int(hex_values_sqrt['h6'], 16) + g) & 0xFFFFFFFF
    h7 = (int(hex_values_sqrt['h7'], 16) + h) & 0xFFFFFFFF

    # Produce the final hash (combine all hash values into a single 256-bit value)
    hash_output = f'{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}{h5:08x}{h6:08x}{h7:08x}'
    print(f"Hash: {hash_output}")

# Get user input and strip leading/trailing whitespace (but leave internal spaces intact)
message = input("Please enter a string of text: ").strip()

# Call the functions to process the input
bincharscat, bitlength = translate(message)
bincharscat = rounding(bincharscat)
bincharscat = append64str(bincharscat, bitlength)
chunks = split_into_chunks(bincharscat)

# Compute initial hash values and cube roots
hex_values_sqrt = compute_initial_hash_values()
hex_values_cubert = compute_cube_roots()

# Call hashval function to finalize processing
hashval(bincharscat, chunks)

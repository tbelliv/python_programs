import math

def translate(message):
    # Convert string characters to Unicode binary values
    bincharslist = [bin(ord(c))[2:].zfill(8) for c in message]  # zfill(8) ensures each character is represented by 8 bits
    bincharscat = ''.join(bincharslist)
    print(bincharscat)
    print(len(bincharscat))
    bitlength = len(bincharscat)
    return bincharscat, bitlength

def rounding(bincharscat):
    # Append '1' and then '0's until the length is 448 bits
    print("Binary string before rounding:", bincharscat)
    if len(bincharscat) < 448:
        bincharscat += '1'  # Append '1' to the string
        while len(bincharscat) < 448:
            bincharscat += '0'
    else:
        print("Binary string length exceeds 448 bits.")
    print(f"Rounding increased the length of the string to {len(bincharscat)}")
    return bincharscat

def append64str(bincharscat, bitlength):
    binbitlength = bin(bitlength)[2:].zfill(64)  # Ensure the bitlength is 64 bits long
    bincharscat = bincharscat + binbitlength
    print(f"Length of bincharscat: {len(bincharscat)}")
    print(f"Binary string: {bincharscat}")
    return bincharscat  # Ensure it returns the modified string

def split_into_chunks(bincharscat, chunk_size=32):
    chunks = [bincharscat[i:i + chunk_size] for i in range(0, len(bincharscat), chunk_size)]
    N = len(chunks) // (512 // chunk_size)
    return chunks, N

def fractional_to_binary(num, k_precision):
    binary = ""

    while k_precision:
        num *= 2
        bit = int(num)

        if bit == 1:
            num -= bit
            binary += '1'
        else:
            binary += '0'

        k_precision -= 1

    return binary

def binary_to_hex(binary_str):
    return hex(int(binary_str, 2))[2:]

# List of the first 8 prime numbers
primes_8 = [2, 3, 5, 7, 11, 13, 17, 19]

# Dictionary to store the hex values for square roots
hex_values_sqrt = {}

for i, prime in enumerate(primes_8):
    # Get the square root of the prime number
    h0 = math.sqrt(prime)

    # Get the fractional part of sqrt(prime)
    fractional_part = h0 - int(h0)

    # Convert the fractional part to binary
    binary_fractional_part = fractional_to_binary(fractional_part, 32)  # 32 is the precision

    # Split the binary string into parts of 4 bits
    split_binary = [binary_fractional_part[i:i + 4] for i in range(0, len(binary_fractional_part), 4)]

    # Convert each 4-bit part to hexadecimal
    hex_parts = [binary_to_hex(bits) for bits in split_binary]

    # Concatenate the hex values into a single string
    hex_string = ''.join(hex_parts)

    # Store the hex string in the dictionary with the appropriate key
    hex_values_sqrt[f'h{i}'] = hex_string

    print(f"For prime number {prime}, sqrt({prime}) = {h0}")
    print(f"Its fractional part in binary (split into 4-bit parts) is: {split_binary}")
    print(f"And the corresponding hexadecimal values are: {hex_parts}")
    print(f"Concatenated hex string: {hex_string}")

# Print the dictionary to ensure it ran properly
print("\nDictionary of prime numbers and their corresponding concatenated hex strings for square roots:")
for key, hex_string in hex_values_sqrt.items():
    print(f"{key}: {hex_string}")

# Function to compute cube roots of the first 64 prime numbers and store in dictionary
def compute_cube_roots():
    # List of the first 64 prime numbers
    primes_64 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
                 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
                 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
                 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]

    # Dictionary to store the hex values for cube roots
    hex_values_cubert = {}

    for i, prime in enumerate(primes_64):
        # Get the cube root of the prime number
        k0 = prime ** (1/3)

        # Get the fractional part of cbrt(prime)
        fractional_part = k0 - int(k0)

        # Convert the fractional part to binary
        binary_fractional_part = fractional_to_binary(fractional_part, 32)  # 32 is the precision

        # Split the binary string into parts of 4 bits
        split_binary = [binary_fractional_part[j:j + 4] for j in range(0, len(binary_fractional_part), 4)]

        # Convert each 4-bit part to hexadecimal
        hex_parts = [binary_to_hex(bits) for bits in split_binary]

        # Concatenate the hex values into a single string
        hex_string = ''.join(hex_parts)

        # Store the hex string in the dictionary with the appropriate key
        hex_values_cubert[f'k{i}'] = hex_string

        print(f"For prime number {prime}, cbrt({prime}) = {k0}")
        print(f"Its fractional part in binary (split into 4-bit parts) is: {split_binary}")
        print(f"And the corresponding hexadecimal values are: {hex_parts}")
        print(f"Concatenated hex string: {hex_string}")

    # Print the dictionary to ensure it ran properly
    print("\nDictionary of prime numbers and their corresponding concatenated hex strings for cube roots:")
    for key, hex_string in hex_values_cubert.items():
        print(f"{key}: {hex_string}")

    return hex_values_cubert

# Compute the cube roots and store the results in a dictionary
hex_values_cubert = compute_cube_roots()

# Now you can pass the hex_values_sqrt and hex_values_cubert dictionaries to the next function

def hashval(bincharscat, chunks):
    print("placeholder")

# Get user input
message = input("Please enter a string of text: ")

# Call translate function and unpack the returned values
bincharscat, bitlength = translate(message)

# Call rounding function and pass the returned values
bincharscat = rounding(bincharscat)

# Pass the updated bincharscat and original bitlength to append64str function
bincharscat = append64str(bincharscat, bitlength)

# Split bincharscat into 32 char chunks
chunks, N = split_into_chunks(bincharscat)

# Print the chunks and N for debugging
print(f"Chunks of 32 characters: {chunks}")
print(f"N value: {N}")

# Call the hashval function with bincharscat and chunks
hashval(bincharscat, chunks)
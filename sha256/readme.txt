SHA-256 Implementation

This script implements a basic SHA-256 hashing algorithm in Python.

Usage:
1. run script: python3 sha256.py 
2. Enter a string
3. The program outputs the hash value for the string (SHA-256)

Description:
* translate: Converts a string into binary.
* rounding: Pads binary data to 448 bits.
* append64str: Appends the length of the message as 64-bit binary.
* split_into_chunks: Splits binary data into 32-bit chunks.
* fractional_to_binary: Converts fractional numbers to binary.
* binary_to_hex: Converts binary strings to hexadecimal.
* compute_initial_hash_values: Computes initial hash values based on square roots of the first 8 primes.
* compute_cube_roots: Computes cube roots of the first 64 primes.
* right_rotate: Performs bitwise rotation.
* hashval: Processes the binary data and computes the SHA-256 hash.

Example:
Please enter a string of text: hello
Hash: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

Credits:

Timothy Belliveau (author)
Sam Baker (contributor)

License:
Unlicense

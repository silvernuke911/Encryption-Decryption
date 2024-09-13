def string_to_binary(input_string):
    # Convert each character to its 8-bit binary representation and concatenate
    binary_string = ''.join(format(ord(char), '08b') for char in input_string)
    return binary_string

def binary_to_string(binary_string):
    # Split the binary string into chunks of 8 bits
    characters = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    # Convert each chunk from binary to an ASCII character
    ascii_string = ''.join(chr(int(char, 2)) for char in characters)
    return ascii_string

def rotate_string(input_string, n):
    # Ensure n is within the bounds of the string length
    n = n % len(input_string)
    # Slice the string and concatenate
    rotated_string = input_string[n:] + input_string[:n]
    return rotated_string

def split_into_fours(binary_string):
    # Initialize an empty list to store the substrings
    substrings = []
    
    # Iterate over the binary string in steps of 4
    for i in range(0, len(binary_string), 4):
        # Extract a substring of length 4
        substring = binary_string[i:i+4]
        # Add the substring to the list
        substrings.append(substring)
    
    return substrings

def add_prefix(strings_list):
    # Initialize an empty list to store the modified strings
    modified_strings = []
    
    # Iterate over the list of strings
    for string in strings_list:
        # Add the prefix '0100' to the front of each string
        modified_string = '0100' + string
        # Append the modified string to the list
        modified_strings.append(modified_string)
    
    return modified_strings

def concatenate_strings(strings_list):
    # Use the join() method to concatenate all strings in the list
    concatenated_string = ''.join(strings_list)
    return concatenated_string

def bin_encryptor(message,n):
    bin_message = str(string_to_binary(message))
    print(bin_message)
    four_list = split_into_fours(bin_message)
    print(four_list)
    prefixed_list = add_prefix(four_list)
    print(prefixed_list)
    rot_message = concatenate_strings(prefixed_list)
    print(rot_message)
    str_message = str(binary_to_string(rot_message))
    return str_message

def bin_decryptor(message,n):
    bin_message = str(string_to_binary(message))
    rot_message = rotate_string(bin_message, -n)
    str_message = str(binary_to_string(rot_message))
    return str_message




n=1
print()
encrypt = bin_encryptor('For we are many, and we are more than thee, you do not know where I am, do not know where I came from',n)
print(encrypt)
decrypt='Kvwwjhfwjfdrfs_'
decrypt = bin_decryptor(decrypt,n)
print(decrypt)


# # Example usage
# input_string = "Why? Hello World, how are you"
# n = 5
# result = rotate_string(input_string, n)
# print(f"Result after rotating '{input_string}' by {n} positions: {result}")

# # Example usage
# input_string = "Hello there"
# binary_representation = string_to_binary(input_string)
# print(f"Binary representation of '{input_string}': {binary_representation}")

# # Example usage
# binary_string = "0100100001100101011011000110110001101111001000000111010001101000011001010111001001100101"
# ascii_representation = binary_to_string(binary_string)
# print(f"ASCII representation of '{binary_string}': {ascii_representation}")

# def bin_encryptor(message,n):
#     bin_message = str(string_to_binary(message))
#     rot_message = rotate_string(bin_message, n)
#     str_message = str(binary_to_string(rot_message))
#     return str_message

# def bin_decryptor(message,n):
#     bin_message = str(string_to_binary(message))
#     rot_message = rotate_string(bin_message, -n)
#     str_message = str(binary_to_string(rot_message))
#     return str_message
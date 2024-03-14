import hashlib

def calculate_hash(input_string, algorithm = 'sha256'):
    hash_algorithm = getattr(hashlib,algorithm,None)
    if hash_algorithm is None:
        print("Error: Invalid hash algorithm specified.")
        return None

    hash_object = hash_algorithm(input_string.encode())
    return hash_object.hexdigest()

#Example Usage:
input_string = "Hello World!"
hash_value = calculate_hash(input_string)
if hash_value is not None:
    print("Input String:", input_string)
    print("Hash Value (SHA-256):", hash_value)
import hashlib

user_hash_dict = {}

# Read and store usernames and hashed passwords from 'username_hashes.txt'
with open('username_hashes.txt', 'r', encoding='utf-8') as user_hash_file:
    for line in user_hash_file:
        username, hashed_password = line.strip().split(":")
        user_hash_dict[username] = hashed_password

# Read passwords from 'password_list.txt' and check for matches
with open('password_list.txt', 'r', encoding='utf-8') as password_file:
    for password in password_file:
        password = password.strip()  # Remove leading/trailing whitespace
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        for username, stored_hash in user_hash_dict.items():
            if hashed_password == stored_hash:
                print(f'HASH FOUND\n{username}:{password}')
                break  # Assuming one user cannot have multiple passwords
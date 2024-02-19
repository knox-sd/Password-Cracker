import hashlib

user_hash_dict = {}

with open('password_list.txt', 'r') as p:
    '''c_pass.append(p.read().splitlines()) #list all password with in bracket need to seprate'''
    c_pass = p.read().splitlines()
    # print(c_pass)


with open('username_hashes.txt', 'r') as p:
    text = p.read().splitlines()
    for user_hash in text:
        username = user_hash.split(":")[0]
        hash = user_hash.split(":")[1]
        user_hash_dict[username] = hash
        # print(hash)

for password in c_pass:
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    # print(hashed_password)
    for username, hash in user_hash_dict.items():
        if hashed_password == hash:
            print(f'HASH FOUND\n{username}:{password}')
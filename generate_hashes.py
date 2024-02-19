import hashlib

password = "welcome1"
hash = hashlib.sha256(password.encode('utf-8'))
# print(hash)
print(hash.hexdigest())
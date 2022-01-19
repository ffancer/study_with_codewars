import hashlib


def pass_hash(str):
    return hashlib.md5(str.encode('utf-8')).hexdigest()


print(pass_hash("password"))
print(pass_hash("abc123"))

from sha3 import sha3


def make_hash(file, hash_file, sha_type):
    file_string = open(file, 'r').read()
    res = sha3(file_string, sha_type).upper()

    f = open(hash_file, 'w')
    f.write(res)
    f.close()

    f = open(hash_file, 'r')
    hash = f.readline()
    f.close()

    return hash


print(f"Полученный хеш для SHA3-224 - {make_hash('1.txt', '2.txt', 224)}")
print(f"Полученный хеш для SHA3-256 - {make_hash('1.txt', '2.txt', 256)}")
print(f"Полученный хеш для SHA3-384 - {make_hash('1.txt', '2.txt', 384)}")
print(f"Полученный хеш для SHA3-512 - {make_hash('1.txt', '2.txt', 512)}")
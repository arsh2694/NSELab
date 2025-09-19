# String hashing
import hashlib

M = "Hello"
print("Message:", M)
print("SHA-256:", hashlib.sha256(M.encode()).hexdigest())

M = "Hell"
print("SHA-256:", hashlib.sha256(M.encode()).hexdigest())

# File hashing
def hash_file(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

filename = "abc.txt"
print(f"SHA-256 Hash of '{filename}':", hash_file(filename))

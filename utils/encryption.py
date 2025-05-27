#imports
import hashlib

#encrypt
def make_hash(data_string: str) -> str:
    data_bytes = data_string.encode('utf-8')
    sha256_hasher = hashlib.sha256()
    sha256_hasher.update(data_bytes)
    hex_digest = sha256_hasher.hexdigest()
    return hex_digest

#check
def check(original_string: str, candidate_hash: str) -> bool:
    computed_hash = make_hash(original_string)
    is_match = (computed_hash == candidate_hash)
    return is_match
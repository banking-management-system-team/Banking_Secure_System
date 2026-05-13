import bcrypt
import hashlib


def hash_password(password: str) -> str:
    password_bytes = password.encode('utf-8')
    sha256_bytes = hashlib.sha256(password_bytes).digest()
    hashed_bytes = bcrypt.hashpw(sha256_bytes, bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    password_bytes = plain_password.encode('utf-8')
    sha256_bytes = hashlib.sha256(password_bytes).digest()
    return bcrypt.checkpw(
        sha256_bytes,
        hashed_password.encode('utf-8')
    )

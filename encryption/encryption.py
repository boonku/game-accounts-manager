import secrets
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

import config

backend = default_backend()


def _derive_key(password: bytes, salt: bytes) -> bytes:
    """Derive a secret key from a given password and salt"""
    iterations = 100_000
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt,
        iterations=iterations, backend=backend)
    return b64e(kdf.derive(password))


def password_encrypt(message: bytes, password: str) -> bytes:
    iterations = 100_000
    salt = secrets.token_bytes(16)
    key = _derive_key(password.encode(), salt)
    return b64e(
        b'%b%b%b' % (
            salt,
            iterations.to_bytes(4, 'big'),
            b64d(Fernet(key).encrypt(message)),
        )
    )


def password_decrypt(token: bytes, password: str) -> bytes:
    decoded = b64d(token)
    salt, token = decoded[:16], b64e(decoded[20:])
    key = _derive_key(password.encode(), salt)
    return Fernet(key).decrypt(token)


def load_key():
    key_file = config.encryption['file']
    root_dir = config.app['root_dir']
    with open(root_dir + key_file, 'rb') as file:
        return file.read()


def encrypt_message(message):
    encoded_msg = message.encode()
    f = Fernet(load_key())
    return f.encrypt(encoded_msg)


def decrypt_message(encrypted_message):
    f = Fernet(load_key())
    return f.decrypt(encrypted_message)

from cryptography.fernet import Fernet
import config


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

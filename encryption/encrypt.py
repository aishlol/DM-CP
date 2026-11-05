
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def generate_key():
    """Generate a secure 256-bit AES key."""
    return AESGCM.generate_key(bit_length=256)


def encrypt_file(file_data: bytes):
    """
    Encrypt file bytes using AES-256-GCM.

    Returns:
        encrypted_data: nonce + ciphertext + authentication tag
        key: 256-bit encryption key
    """

    key = generate_key()

    # Generate a fresh 96-bit nonce
    nonce = os.urandom(12)

    # Create AES-GCM cipher
    aesgcm = AESGCM(key)

    # Encrypt the file data
    ciphertext = aesgcm.encrypt(
        nonce,
        file_data,
        None
    )

    # Store nonce with encrypted data
    encrypted_data = nonce + ciphertext

    return encrypted_data, key

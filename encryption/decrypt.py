
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag


def decrypt_file(encrypted_data: bytes, key: bytes):
    """
    Decrypt AES-256-GCM encrypted file data.

    The first 12 bytes contain the nonce.
    Remaining bytes contain ciphertext and authentication tag.
    """

    if len(key) != 32:
        raise ValueError("Invalid AES-256 key. Expected 32 bytes.")

    if len(encrypted_data) < 28:
        raise ValueError("Invalid encrypted file.")

    nonce = encrypted_data[:12]
    ciphertext = encrypted_data[12:]

    aesgcm = AESGCM(key)

    try:
        original_data = aesgcm.decrypt(
            nonce,
            ciphertext,
            None
        )

        return original_data

    except InvalidTag:
        raise ValueError(
            "Authentication failed! Wrong key or modified file."
        )

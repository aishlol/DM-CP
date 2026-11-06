
import hashlib
import hmac
from pathlib import Path


def calculate_sha256(file_data: bytes) -> str:
    """
    Calculate SHA-256 hash of given file data.

    Args:
        file_data: File content in bytes.

    Returns:
        SHA-256 hexadecimal hash.
    """
    return hashlib.sha256(file_data).hexdigest()


def calculate_file_hash(file_path: str) -> str:
    """
    Calculate SHA-256 hash directly from a file.

    Reads large files in chunks to reduce memory usage.
    """
    sha256_hash = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                sha256_hash.update(chunk)

        return sha256_hash.hexdigest()

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    except PermissionError:
        raise PermissionError(f"Permission denied: {file_path}")


def verify_sha256(file_data: bytes, expected_hash: str) -> bool:
    """
    Verify file data against an expected SHA-256 hash.
    """
    if not expected_hash or not isinstance(expected_hash, str):
        return False

    actual_hash = calculate_sha256(file_data)

    return hmac.compare_digest(
        actual_hash.lower(),
        expected_hash.strip().lower()
    )


def verify_file_integrity(file_path: str, expected_hash: str) -> bool:
    """
    Verify the integrity of a file using SHA-256.
    """
    if not expected_hash or not isinstance(expected_hash, str):
        return False

    actual_hash = calculate_file_hash(file_path)

    return hmac.compare_digest(
        actual_hash.lower(),
        expected_hash.strip().lower()
    )


def compare_files(file1_path: str, file2_path: str) -> bool:
    """
    Compare two files using their SHA-256 hashes.
    """
    hash1 = calculate_file_hash(file1_path)
    hash2 = calculate_file_hash(file2_path)

    return hmac.compare_digest(hash1, hash2)


def get_file_information(file_path: str) -> dict:
    """
    Return file name, size and SHA-256 hash.
    """
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    return {
        "file_name": path.name,
        "file_size": path.stat().st_size,
        "sha256_hash": calculate_file_hash(file_path)
    }

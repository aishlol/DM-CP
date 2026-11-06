
from math_lab.gcd import calculate_gcd
from math_lab.modular_arithmetic import modular_inverse, modular_exponentiation


def generate_rsa_keys(p: int, q: int) -> dict:
    """
    Generate educational RSA public and private keys.

    p and q must be distinct prime numbers.
    """

    if not isinstance(p, int) or isinstance(p, bool):
        raise TypeError("p must be an integer.")

    if not isinstance(q, int) or isinstance(q, bool):
        raise TypeError("q must be an integer.")

    if p <= 1 or q <= 1 or p == q:
        raise ValueError("p and q must be distinct prime numbers.")

    if not _is_prime(p) or not _is_prime(q):
        raise ValueError("Both p and q must be prime numbers.")

    # Step 1: Calculate n
    n = p * q

    # Step 2: Calculate Euler's totient
    phi = (p - 1) * (q - 1)

    # Step 3: Choose public exponent e
    e = 3

    while e < phi and calculate_gcd(e, phi) != 1:
        e += 2

    if e >= phi:
        raise ValueError("Unable to find a valid public exponent.")

    # Step 4: Calculate private exponent d
    d = modular_inverse(e, phi)

    return {
        "p": p,
        "q": q,
        "n": n,
        "phi": phi,
        "e": e,
        "d": d,
        "public_key": (n, e),
        "private_key": (n, d)
    }


def rsa_encrypt(message: int, public_key: tuple) -> int:
    """
    Encrypt an integer message using the RSA public key.
    """

    n, e = public_key

    if not isinstance(message, int) or isinstance(message, bool):
        raise TypeError("Message must be an integer.")

    if not 0 <= message < n:
        raise ValueError("Message must be between 0 and n-1.")

    return modular_exponentiation(message, e, n)


def rsa_decrypt(ciphertext: int, private_key: tuple) -> int:
    """
    Decrypt an integer ciphertext using the RSA private key.
    """

    n, d = private_key

    if not isinstance(ciphertext, int) or isinstance(ciphertext, bool):
        raise TypeError("Ciphertext must be an integer.")

    if not 0 <= ciphertext < n:
        raise ValueError("Ciphertext must be between 0 and n-1.")

    return modular_exponentiation(ciphertext, d, n)


def _is_prime(number: int) -> bool:
    """Check whether a number is prime."""

    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def rsa_demo() -> dict:
    """
    Run the RSA demonstration from the CipherShield PPT.
    """

    keys = generate_rsa_keys(5, 11)

    message = 7

    ciphertext = rsa_encrypt(message, keys["public_key"])

    decrypted_message = rsa_decrypt(
        ciphertext,
        keys["private_key"]
    )

    return {
        "keys": keys,
        "original_message": message,
        "encrypted_message": ciphertext,
        "decrypted_message": decrypted_message,
        "successful": message == decrypted_message
    }

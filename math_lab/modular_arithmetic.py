
def _validate_modulus(modulus: int):
    """Validate that modulus is a positive integer."""
    if not isinstance(modulus, int) or isinstance(modulus, bool):
        raise TypeError("Modulus must be an integer.")

    if modulus <= 0:
        raise ValueError("Modulus must be greater than zero.")


def modular_addition(a: int, b: int, modulus: int) -> int:
    """Calculate (a + b) mod m."""
    _validate_modulus(modulus)
    return (a + b) % modulus


def modular_subtraction(a: int, b: int, modulus: int) -> int:
    """Calculate (a - b) mod m."""
    _validate_modulus(modulus)
    return (a - b) % modulus


def modular_multiplication(a: int, b: int, modulus: int) -> int:
    """Calculate (a * b) mod m."""
    _validate_modulus(modulus)
    return (a * b) % modulus


def modular_exponentiation(base: int, exponent: int, modulus: int) -> int:
    """Calculate (base^exponent) mod m efficiently."""
    _validate_modulus(modulus)

    if not isinstance(exponent, int) or isinstance(exponent, bool):
        raise TypeError("Exponent must be an integer.")

    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")

    return pow(base, exponent, modulus)


def modular_inverse(a: int, modulus: int):
    """
    Find the modular multiplicative inverse of a modulo m.

    The inverse exists only when gcd(a, m) = 1.
    """
    _validate_modulus(modulus)

    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError("Input must be an integer.")

    if modulus == 1:
        raise ValueError("Modular inverse is not defined for modulus 1.")

    try:
        return pow(a, -1, modulus)
    except ValueError:
        raise ValueError(
            f"Modular inverse does not exist because gcd({a}, {modulus}) != 1."
        )

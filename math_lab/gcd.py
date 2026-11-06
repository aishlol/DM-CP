
def calculate_gcd(a: int, b: int) -> int:
    """
    Calculate GCD using the Euclidean Algorithm.

    GCD is the greatest positive integer
    that divides both numbers.
    """

    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError("First input must be an integer.")

    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError("Second input must be an integer.")

    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a


def calculate_lcm(a: int, b: int) -> int:
    """
    Calculate Least Common Multiple (LCM).

    Formula:
    LCM(a, b) = |a * b| / GCD(a, b)
    """

    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError("First input must be an integer.")

    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError("Second input must be an integer.")

    if a == 0 or b == 0:
        return 0

    return abs(a * b) // calculate_gcd(a, b)


def extended_euclidean(a: int, b: int) -> tuple:
    """
    Extended Euclidean Algorithm.

    Returns (gcd, x, y) satisfying:
    a*x + b*y = gcd(a, b)
    """

    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError("First input must be an integer.")

    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError("Second input must be an integer.")

    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r

        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    if old_r < 0:
        old_r, old_s, old_t = -old_r, -old_s, -old_t

    return old_r, old_s, old_t

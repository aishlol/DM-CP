
import math


def is_prime(number: int) -> bool:
    """
    Check whether a number is prime.

    A prime number is a natural number greater than 1
    that has exactly two factors: 1 and itself.
    """

    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("Input must be an integer.")

    if number <= 1:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for i in range(3, math.isqrt(number) + 1, 2):
        if number % i == 0:
            return False

    return True


def get_prime_factors(number: int) -> list:
    """
    Find all prime factors of a positive integer.
    """

    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("Input must be an integer.")

    if number < 1:
        raise ValueError("Number must be positive.")

    factors = []
    divisor = 2

    while divisor * divisor <= number:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor

        divisor += 1

    if number > 1:
        factors.append(number)

    return factors


def generate_primes(limit: int) -> list:
    """
    Generate all prime numbers up to a given limit
    using the Sieve of Eratosthenes.
    """

    if not isinstance(limit, int) or isinstance(limit, bool):
        raise TypeError("Limit must be an integer.")

    if limit < 2:
        return []

    is_prime_list = [True] * (limit + 1)
    is_prime_list[0] = False
    is_prime_list[1] = False

    for i in range(2, math.isqrt(limit) + 1):
        if is_prime_list[i]:
            for j in range(i * i, limit + 1, i):
                is_prime_list[j] = False

    return [
        number
        for number, prime in enumerate(is_prime_list)
        if prime
    ]

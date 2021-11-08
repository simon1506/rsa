import secrets
from sympy import isprime


def modexp(base, exponent, modulus):
    result = 1
    while exponent:
        if exponent & 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result


def extgcd(a, b):
    if b == 0:
        return 1, 0
    else:
        x, y = extgcd(b, a % b)
        q = a // b
        return y, x-y*q


def modinv(a, n):
    x, y = extgcd(a, n)
    return x % n


def genprime(b):
    n = secrets.randbits(b - 1)
    n |= 1 << b - 1
    n |= 1

    while not isprime(n):
        n += 2
    return n


class RSAKey:
    def __init__(self, n, e, d):
        self.n = n
        self.e = e
        self.d = d


def generate_keys(b):
    prime_length = b // 2
    e = 65537
    phi, p, q = 0, 0, 0

    while phi % e == 0:
        p = genprime(prime_length)
        q = genprime(prime_length)
        phi = (p - 1) * (q - 1)

    n = p * q
    d = modinv(e, phi)

    return RSAKey(n, e, d)


def encrypt(m, key):
    return modexp(m, key.e, key.n)


def decrypt(c, key):
    return modexp(c, key.d, key.n)

import rsa

if __name__ == "__main__":
    key_length = int(input("Enter key length in bits (integer only): "))

    if not key_length >= 1024:
        print("Key length must be greater than 1024 Bits!")
        exit(1)

    print("Generating keys...")
    key = rsa.generate_keys(key_length)
    print(f"Modulus: {key.n}")
    print(f"Public exponent: {key.e}")
    print(f"Private exponent: {key.d}")

    print()
    message = int(input("Message (integer only): "))

    if 0 < message < key.n:
        print(f"Cipher text: {rsa.encrypt(message, key)}")
    else:
        print("Message must be smaller than the modulus!")
        exit(1)

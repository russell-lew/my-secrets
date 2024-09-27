#!/usr/bin/env python3

from argparse import ArgumentParser
from base64 import b64encode
from Crypto.Cipher import AES


def encrypt(flag: bytes, key: bytes, iv: bytes) -> bytes:
    aes = AES.new(key, AES.MODE_CBC, iv)
    cipher = iv + aes.encrypt(flag)
    return b64encode(cipher)


def main() -> None:
    required_key_size = max(AES.key_size)

    parser = ArgumentParser()
    parser.add_argument("flag")
    parser.add_argument("password")
    parser.add_argument("iv")

    args = parser.parse_args()
    flag: bytes = str(args.flag).encode()
    password: bytes = str(args.password).lower().ljust(required_key_size, "5").encode()
    iv: bytes = str(args.iv).encode()

    encrypted_message = encrypt(flag, password, iv)
    print(encrypted_message)


if __name__ == "__main__":
    main()

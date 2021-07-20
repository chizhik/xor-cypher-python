def string_to_bytes(string):
    return bytes(string, 'utf-8')


def bytes_to_string(bytes):
    return str(bytes, 'utf-8')


def xor_bytes(plaintext: bytes, key: bytes):
    return bytes(
        [plaintext[i] ^ key[i % len(key)] for i in range(len(plaintext))])


# XOR encypher and return cyphertext in hex format
def xor_encypher(plaintext: str, key: str):
    plaintext = string_to_bytes(plaintext)
    key = string_to_bytes(key)
    cyphertext = xor_bytes(plaintext, key)
    return cyphertext.hex()


# XOR decipher cyphertext in hex format and return plaintext
def xor_decipher(cyphertext: str, key: str):
    cyphertext = bytes.fromhex(cyphertext)
    key = string_to_bytes(key)
    plaintext = xor_bytes(cyphertext, key)
    return bytes_to_string(plaintext)


if __name__ == "__main__":
    plaintexts = ["meetjoeblack"]
    key = "thisismykey"
    for plaintext in plaintexts:
        cyphertext = xor_encypher(plaintext, key)
        print(plaintext, "->", cyphertext)
        assert xor_decipher(cyphertext, key) == plaintext

    cyphertexts = []
    for cyphertext in cyphertexts:
        plaintext = xor_decipher(cyphertext, key)
        print(cyphertext, "->", plaintext)
        assert xor_encypher(plaintext, key) == cyphertext

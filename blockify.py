# TUDE algorithm implementation
from helper import text_to_bin, text_to_block


def generate_key(key: str, n: int) -> list:
    pass


def feistel_function(round_key: str, partial_block: str) -> str:
    pass


def encrypt(plain_text: str, key: str, mode: str) -> str:
    # bikin text per block
    # split block jadi dua
    # R = split_block[1]
    # untuk setiap i, panggil feistel_function(key[i], R)
    # concat L dan R hasil iterasi sebagai hasil encrypt
    # return hasil encrypt
    pass


def decrypt(cipher_text: str, key: str, mode: str) -> str:
    # kebalikan dari encrypt
    pass


if __name__ == "__main__":
    pass

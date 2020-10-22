# TUDE algorithm implementation
from helper import text_to_bin, text_to_block, split_block, xor, initiate_counter_block
from constant import BLOCK_SIZE, ROUNDS


def generate_key(key: str, n: int) -> list:
    pass


def feistel_function(round_key: str, partial_block: str) -> str:
    pass


def encrypt_per_block(block: str, keys: list) -> str:
    pass


def decrypt_per_block(block: str, keys: list) -> str:
    pass


def encrypt(plain_text: str, key: str, mode: str) -> str:
    text_blocks = text_to_block(plain_text)
    keys = generate_key(key, ROUNDS)
    iv = '0' * BLOCK_SIZE
    counter_block = initiate_counter_block(ROUNDS)

    encrypted_text = ''
    for i in range(len(text_blocks)):
        block = text_blocks[i]
        if mode == 'ecb':
            encrypted_text += encrypt_per_block(block, keys)
        elif mode == 'cbc':
            block = xor(block, iv)
            encrypted_block = encrypt_per_block(block, keys)
            encrypted_text += encrypted_block
            iv = encrypted_block
        else:
            encrypted_block = encrypt_per_block(block, keys)
            encrypted_text += xor(encrypted_block, counter_block[i])

    return encrypted_text


def decrypt(cipher_text: str, key: str, mode: str) -> str:
    # kebalikan dari encrypt
    pass


if __name__ == "__main__":
    pass

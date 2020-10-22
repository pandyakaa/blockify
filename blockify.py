# TUDE algorithm implementation
from helper import text_to_bin, text_to_block, split_block, xor, initiate_counter_block, rotate_left, bin_to_hex, substitute, hex_to_bin, negate, odd_even_permute
from constant import BLOCK_SIZE, ROUNDS, SBOX, SBOX_INV
from helper import bin_to_text
import codecs
import random


def generate_key(key: str, n: int) -> list:
    key = codecs.encode(key, 'rot_13')
    binary_key = text_to_bin(key)
    keys = []

    random.seed(n)
    # for i in range(n):
    #     sample_binary_key = random.sample(binary_key, 64)
    #     sample_binary_key = rotate_left(sample_binary_key, 4, 64)
    #     sample_binary_key = "".join(sample_binary_key)
    #     keys.append(sample_binary_key)

    for i in range(n):
        sample_binary_key = [binary_key[j] for j in range(64)]
        # sample_binary_key = rotate_left(sample_binary_key, 4, 64)
        # sample_binary_key = random.sample(binary_key, 64)
        sample_binary_key = "".join(sample_binary_key)
        keys.append(sample_binary_key)

    return keys


def feistel_function(round_key: str, partial_block: str, mode: str) -> str:
    feistel_result = xor(round_key, partial_block)

    feistel_result = bin_to_hex(feistel_result)
    if mode == encrypt:
        feistel_result = substitute(feistel_result, SBOX)
    else:
        feistel_result = substitute(feistel_result, SBOX_INV)
    feistel_result = hex_to_bin(feistel_result)

    # feistel_result = odd_even_permute(feistel_result)
    # feistel_result = negate(feistel_result)

    return feistel_result


def encrypt_per_block(block: str, keys: list) -> str:
    left_block, right_block = split_block(block)
    for i in range(ROUNDS):
        feistel_function_result = feistel_function(
            keys[i], right_block, 'encrypt')
        temp = xor(left_block, feistel_function_result)

        left_block = right_block
        right_block = temp

    encrypted_text_per_block = left_block + right_block
    return encrypted_text_per_block


def decrypt_per_block(block: str, keys: list) -> str:
    left_block, right_block = split_block(block)
    for i in range(ROUNDS-1, -1, -1):
        feistel_function_result = feistel_function(
            keys[i], left_block, 'decrypt')
        temp = xor(right_block, feistel_function_result)

        right_block = left_block
        left_block = temp

    decrypted_text_per_block = left_block + right_block
    return decrypted_text_per_block


def encrypt(plain_text: str, key: str, mode: str) -> str:
    text_blocks = text_to_block(plain_text)
    keys = generate_key(key, ROUNDS)
    iv = '0' * BLOCK_SIZE
    counter_block = initiate_counter_block(len(text_blocks))

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
        elif mode == 'counter':
            encrypted_block = encrypt_per_block(counter_block[i], keys)
            encrypted_text += xor(encrypted_block, block)

    encrypted_text = bin_to_text(encrypted_text)
    return encrypted_text


def decrypt(cipher_text: str, key: str, mode: str) -> str:
    text_blocks = text_to_block(cipher_text)
    keys = generate_key(key, ROUNDS)
    iv = '0' * BLOCK_SIZE
    counter_block = initiate_counter_block(len(text_blocks))

    decrypted_text = ''
    for i in range(len(text_blocks)):
        block = text_blocks[i]
        if mode == 'ecb':
            decrypted_text += decrypt_per_block(block, keys)
        elif mode == 'cbc':
            decrypted_block = decrypt_per_block(block, keys)
            decrypted_block = xor(decrypted_block, iv)
            decrypted_text += decrypted_block
            iv = block
        elif mode == 'counter':
            decrypted_block = encrypt_per_block(counter_block[i], keys)
            decrypted_text += xor(decrypted_block, block)

    decrypted_text = bin_to_text(decrypted_text)
    return decrypted_text


if __name__ == "__main__":
    pass

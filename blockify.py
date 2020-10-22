# TUDE algorithm implementation
from helper import text_to_bin, text_to_block, split_block, xor, initiate_counter_block
from constant import BLOCK_SIZE, ROUNDS


def generate_key(key: str, n: int) -> list:
    pass


def feistel_function(round_key: str, partial_block: str) -> str:
    pass


def encrypt_per_block(block: str, keys: list) -> str:
    left_block, right_block = split_block(block)
    for i in range(ROUNDS):
        feistel_function_result = feistel_function(keys[i], right_block)
        temp = xor(left_block, feistel_function_result)

        left_block = right_block
        right_block = temp
    
    encrypted_text_per_block = left_block + right_block
    return encrypted_text_per_block


def decrypt_per_block(block: str, keys: list) -> str:
    left_block, right_block = split_block(block)
    for i in range(ROUNDS-1, -1 , -1):
        feistel_function_result = feistel_function(keys[i], left_block)
        temp = xor(right_block, feistel_function_result)

        right_block = left_block
        left_block = temp
    
    decrypted_text_per_block = left_block + right_block
    return decrypted_text_per_block


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
            encrypted_block = encrypt_per_block(counter_block[i], keys)
            encrypted_text += xor(encrypted_block, block)

    return encrypted_text


def decrypt(cipher_text: str, key: str, mode: str) -> str:
    text_blocks = text_to_block(cipher_text)
    keys = generate_key(key, ROUNDS)
    iv = '0' * BLOCK_SIZE
    counter_block = initiate_counter_block(ROUNDS)

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
        else:
            decrypted_block = decrypt_per_block(counter_block[i], keys)
            decrypted_text += xor(decrypted_block, block)

    return decrypted_text



if __name__ == "__main__":
    pass

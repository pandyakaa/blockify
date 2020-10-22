from blockify import encrypt, decrypt
import time

if __name__ == "__main__":

    ecb_enc_start_time = time.time()
    enc_tc = encrypt('pandyaka aptanagi', 'ini adalah kunci', 'ecb')
    ecb_enc_end_time = time.time()
    print('ecb time {}'.format(ecb_enc_end_time - ecb_enc_start_time))

    ecb_dec_start_time = time.time()
    dec_tc = decrypt(enc_tc, 'ini adalah kunci', 'ecb')
    ecb_dec_end_time = time.time()
    print('ecb time {}'.format(ecb_dec_end_time - ecb_dec_start_time))

    print('ecb encryption result: {}'.format(enc_tc))
    print('ecb decryption result: {}'.format(dec_tc))

    print('===============================================================')

    # cbc_enc_start_time = time.time()
    # enc_tc = encrypt('pandyaka aptanagi', 'ini adalah kunci', 'cbc')
    # cbc_enc_end_time = time.time()
    # print('cbc time {}'.format(cbc_enc_end_time - cbc_enc_start_time))

    # cbc_dec_start_time = time.time()
    # dec_tc = decrypt(enc_tc, 'ini adalah kunci', 'cbc')
    # cbc_dec_end_time = time.time()
    # print('cbc time {}'.format(cbc_dec_end_time - cbc_dec_start_time))

    # print('cbc encryption result: {}'.format(enc_tc))
    # print('cbc decryption result: {}'.format(dec_tc))

    # print('===============================================================')

    # counter_enc_start_time = time.time()
    # enc_tc = encrypt('pandyaka aptanagi', 'aptanagi', 'counter')
    # counter_enc_end_time = time.time()
    # print('counter time {}'.format(counter_enc_end_time - counter_enc_start_time))

    # counter_dec_start_time = time.time()
    # dec_tc = decrypt(enc_tc, 'aptanagi', 'counter')
    # counter_dec_end_time = time.time()
    # print('counter time {}'.format(counter_dec_end_time - counter_dec_start_time))

    # print('counter encryption result: {}'.format(enc_tc))
    # print('counter decryption result: {}'.format(dec_tc))

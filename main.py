from blockify import encrypt, decrypt
import time

if __name__ == "__main__":

    ebc_enc_start_time = time.time()
    enc_tc = encrypt('pandyaka', 'aptanagi', 'ebc')
    ebc_enc_end_time = time.time()
    print('ebc time {}'.format(ebc_enc_end_time - ebc_enc_start_time))

    ebc_dec_start_time = time.time()
    dec_tc = decrypt(enc_tc, 'aptanagi', 'ebc')
    ebc_dec_end_time = time.time()
    print('ebc time {}'.format(ebc_dec_end_time - ebc_dec_start_time))

    print('ebc encryption result: {}'.format(enc_tc))
    print('ebc decryption result: {}'.format(dec_tc))

    print('===============================================================')

    cbc_enc_start_time = time.time()
    enc_tc = encrypt('pandyaka', 'aptanagi', 'cbc')
    cbc_enc_end_time = time.time()
    print('cbc time {}'.format(cbc_enc_end_time - cbc_enc_start_time))

    cbc_dec_start_time = time.time()
    dec_tc = decrypt(enc_tc, 'aptanagi', 'cbc')
    cbc_dec_end_time = time.time()
    print('cbc time {}'.format(cbc_dec_end_time - cbc_dec_start_time))

    print('cbc encryption result: {}'.format(enc_tc))
    print('cbc decryption result: {}'.format(dec_tc))

    print('===============================================================')

    counter_enc_start_time = time.time()
    enc_tc = encrypt('pandyaka', 'aptanagi', 'counter')
    counter_enc_end_time = time.time()
    print('counter time {}'.format(counter_enc_end_time - counter_enc_start_time))

    counter_dec_start_time = time.time()
    dec_tc = decrypt(enc_tc, 'aptanagi', 'counter')
    counter_dec_end_time = time.time()
    print('counter time {}'.format(counter_dec_end_time - counter_dec_start_time))

    print('counter encryption result: {}'.format(enc_tc))
    print('counter decryption result: {}'.format(dec_tc))

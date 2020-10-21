from blockify import encrypt, decrypt

if __name__ == "__main__":
    enc_tc = encrypt('pandyaka', 'aptanagi', 'ebc')
    dec_tc = decrypt(enc_tc, 'aptanagi', 'ebc')

    print(enc_tc)
    print(dec_tc)
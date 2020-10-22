# Some functions source: https://www.geeksforgeeks.org/data-encryption-standard-des-set-1/
from typing import Tuple
from constant import BLOCK_SIZE
import copy


# Hexadecimal to binary conversion
def hex_to_bin(s: str) -> str:
    mp = {'0': "0000",
          '1': "0001",
          '2': "0010",
          '3': "0011",
          '4': "0100",
          '5': "0101",
          '6': "0110",
          '7': "0111",
          '8': "1000",
          '9': "1001",
          'A': "1010",
          'B': "1011",
          'C': "1100",
          'D': "1101",
          'E': "1110",
          'F': "1111"}
    bin_res = ""
    for i in range(len(s)):
        bin_res = bin_res + mp[s[i]]
    return bin_res


# Binary to hexadecimal conversion
def bin_to_hex(s: str) -> str:
    mp = {"0000": '0',
          "0001": '1',
          "0010": '2',
          "0011": '3',
          "0100": '4',
          "0101": '5',
          "0110": '6',
          "0111": '7',
          "1000": '8',
          "1001": '9',
          "1010": 'A',
          "1011": 'B',
          "1100": 'C',
          "1101": 'D',
          "1110": 'E',
          "1111": 'F'}
    hex_res = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex_res = hex_res + mp[ch]

    return hex_res


# Binary to decimal conversion
def bin_to_dec(binary: int) -> int:
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


# Decimal to binary conversion
def dec_to_bin(num: str) -> str:
    res = bin(num).replace("0b", "")
    if(len(res) % 4 != 0):
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res


# Permute function to rearrange the bits
def permute(k: str, arr: list, n: int) -> str:
    permutation = ""
    for i in range(0, n):
        permutation = permutation + k[arr[i] - 1]
    return permutation


def bin_to_text(binary: str) -> str:
    chunk_size = 8
    bin_block = [binary[i:i+chunk_size]
                 for i in range(0, len(binary), chunk_size)]

    text = "".join([chr(int(binary, 2)) for binary in bin_block])

    return text


# calculating xow of two strings of binary number a and b
def xor(a: str, b: str) -> str:
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans


def text_to_bin(text: str) -> str:
    if len(text) < 8:
        for i in range(8-len(text)):
            text += text[i % 8]

    res = ''
    for i in bytearray(text, encoding='utf-8'):
        i = format(i, 'b')
        if len(i) != 8:
            i = '0' * (8 - len(i)) + i
        res += i

    return res


def text_to_block(text: str, block_size=BLOCK_SIZE) -> list:
    res = ''
    for i in bytearray(text, encoding='utf-8'):
        i = format(i, 'b')
        if len(i) != 8:
            i = '0' * (8 - len(i)) + i
        res += i

    if len(res) % 128 != 0:
        res += ('0' * (128 - (len(res) % 128)))

    blocks = [res[i:i+block_size] for i in range(0, len(res), block_size)]

    return blocks


def split_block(block: str) -> Tuple[str, str]:
    chunk_size = len(block) // 2
    splitted_block = [block[i:i+chunk_size]
                      for i in range(0, len(block), chunk_size)]

    return splitted_block[0], splitted_block[1]


def initiate_counter_block(n: int) -> list:
    counter_blocks = []
    for i in range(n):
        counter_block = ('0' * (BLOCK_SIZE-i)) + ('1' * i)
        counter_blocks.append(counter_block)

    return counter_blocks


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def rotate_left(arr: list, d: int, n: int):
    # arr_copy = copy.deepcopy(arr)
    for i in range(gcd(d, n)):
        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

    return arr


def substitute(hex_arr: list, box: list) -> list:
    return hex_arr


def negate(string: str):
    res = ''
    for s in string:
        if s == '0':
            res += '1'
        else:
            res += ('0')

    return res


def odd_even_permute(string: str):
    odd_str = ''
    even_str = ''
    for i in range(len(string)):
        if i % 2 == 0:
            even_str += string[i]
        else:
            odd_str += string[i]

    res = even_str + odd_str

    return res


if __name__ == "__main__":
    print(hex_to_bin('123'))
    print(bin_to_hex('0100'))

    print(negate('1111'))

    print(dec_to_bin(5))
    print(bin_to_dec(1010))

    print(xor('111', '010'))

    print(permute(hex_to_bin("AABCC"), [1, 2, 3, 4], 4))

    print(text_to_bin('pandyaka pandyaka pandyaka'))
    print(text_to_block('pandyaka pandyaka pandyaka'))

    print(split_block("pandyaka"))
    print(initiate_counter_block(16))

    print(bin_to_text('111000101001100110100101001000001110001010011001101001100010000011100010100110011010000000100000111000101001100110100011'))

    print(rotate_left([5, 6, 7, 8, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3,
                       4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4], 4, 64))

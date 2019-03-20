# -*- coding: utf-8 -*-
# chr() là hàm chuyển số về kiểu ký tự trong bảng mã ascii
# ord() là hàm chuyển kí tự đơn về số thứ tự trong bảng mã ascii

# Không mã hóa khoảng trống (32)

def encrypt(plainText, k):
    cipherText = ""
    for i in range(len(plainText)):
        if plainText[i] == " ":
            cipherText += plainText[i]
        else:
            cipherText += chr((ord(plainText[i]) - 33 + k) % 94 + 33) # 126 - 33 + 1 = 94
    return cipherText

def decrypt(cipherText, k):
    plainText = ""
    for i in range(len(cipherText)):
        if cipherText[i] == " ":
            plainText += cipherText[i]
        else:
            plainText += chr((ord(cipherText[i]) - 33 - k) % 94 + 33) # 126 - 33 + 1 = 94
    return plainText

def Ceasar_encode():
    print('Nhập bản rõ: ')
    plainText = str(input())
    print('Nhập khóa k = ')
    k = int(input())
    while k < 0:
        print('Nhập lại khóa k = ')
        k = int(input())
    cipherText = encrypt(plainText, k)
    print('Bản mã: %s' % cipherText)

def Ceasar_decode():
    print('Nhập bản mã: ')
    cipherText = str(input())
    print('Nhập khóa k = ')
    k = int(input())
    while k < 0:
        print('Nhập lại khóa k = ')
        k = int(input())
    plainText = decrypt(cipherText, k)
    print('Bản rõ: %s' % plainText)


Ceasar_encode()
Ceasar_decode()
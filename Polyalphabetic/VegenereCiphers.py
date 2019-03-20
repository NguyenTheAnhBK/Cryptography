#-*- coding: utf-8 -*-
import numpy as np

# Mã hóa chuỗi ký tự phân biệt hoa thường (không mã hóa khoảng trăng) vành N = 26
# Mật mã Vegenere: C = (P[i]+k[j]) mod 26, i chạy từ 0->len(P), j từ 0->len(k) và j lặp lại => C = (P[i] + k[i%len(k)]) mod 26
# P = (C[i] - k[i%len(k)]) mod 26

def stringToArray(k):
    arr = []
    for i in k:
        charIndex = ord(i)
        if charIndex >= 65 and charIndex <= 90: #chữ hoa
            arr.append(charIndex - 65)
        else:
            arr.append(charIndex - 97)
    return np.asarray(arr)

def encrypt(plainText, k):
    k = stringToArray(k)
    cipherText = ""
    for i in range(len(plainText)):
        charIndex = ord(plainText[i])
        if charIndex == 32:
            cipherText += " "
        elif charIndex >= 65 and charIndex <= 90:
            cipherText += chr((charIndex - 65 + k[i % len(k)]) % 26 + 65)
        else :
            cipherText += chr((charIndex - 97 + k[i % len(k)]) % 26 + 97)
    return cipherText

def decrypt(cipherText, k):
    k = stringToArray(k)
    plainText = ""
    for i in range(len(cipherText)):
        charIndex = ord(cipherText[i])
        if charIndex == 32:
            plainText += " "
        elif charIndex >= 65 and charIndex <= 90:
            plainText += chr((charIndex - 65 - k[i % len(k)]) % 26 + 65)
        else:
            plainText += chr((charIndex - 97 - k[i % len(k)]) % 26 + 97)
    return plainText

cipherText = encrypt("The Anh Nguyen", "ltmm")
print(cipherText)
print(decrypt(cipherText, "ltmm"))
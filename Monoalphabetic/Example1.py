# -*- coding: utf-8 -*-
# chr() là hàm chuyển số về kiểu ký tự trong bảng mã ascii
# ord() là hàm chuyển kí tự đơn về số thứ tự trong bảng mã ascii

# Không mã hóa khoảng trống (32)

def Cesare_encode(plainText, k):
    cipherText = ""
    for i in range(len(plainText)):
        if plainText[i] == " ":
            cipherText += plainText[i]
        else:
            cipherText += chr((ord(plainText[i]) - 33 + k) % 94 + 33) # 126 - 33 + 1 = 94
    return cipherText

def Cesare_decode(cipherText, k):
    plainText = ""
    for i in range(len(cipherText)):
        if cipherText[i] == " ":
            plainText += cipherText[i]
        else:
            plainText += chr((ord(cipherText[i]) - 33 - k) % 94 + 33) # 126 - 33 + 1 = 94
    return plainText


cipherText = Cesare_encode("Nguyen the Anh 123 012212", 17)
print(cipherText)
print(Cesare_decode(cipherText, 17))
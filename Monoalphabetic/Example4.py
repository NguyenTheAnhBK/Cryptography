#-*- coding: utf-8 -*-

# Mã hóa chuỗi ký tự phân biệt hoa thường (N= 26)
def encrypt(plainText, k):
    cipherText = ""
    for i in range(len(plainText)):
        charIndex = ord(plainText[i])
        if charIndex == 32:
            cipherText += " "
        elif charIndex >= 65 and charIndex <= 90:
            cipherText += chr((charIndex - 65 + k) % 26 + 65) 
        else:
            cipherText += chr((charIndex - 97 + k) % 26 + 97) 
    return cipherText

def decrypt(cipherText, k):
    plainText = ""
    for i in range(len(cipherText)):
        charIndex = ord(cipherText[i])
        if charIndex == 32:
            plainText += " "
        elif charIndex >= 65 and charIndex <= 90:
            plainText += chr((charIndex - 65 - k) % 26 + 65) 
        else:
            plainText += chr((charIndex - 97 - k) % 26 + 97) 
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

# def module_inverse(k, N = 26): 
#     t1, t2 = 0, 1
#     while k > 0:
#         q = N // k
#         r = N - k*q
#         N, k = k, r
#         t = t1 - t2*q
#         t1, t2 = t2, t
#     if N == 1: 
#         return t1
#     return 0 

# def encrypt(plainText, k):
#     cipherText = ""
#     for i in range(len(plainText)):
#         charIndex = ord(plainText[i])
#         if charIndex == 32:
#             cipherText += " "
#         elif charIndex >= 65 and charIndex <= 90:
#             cipherText += chr(((charIndex - 65) * k) % 26 + 65) 
#         else:
#             cipherText += chr(((charIndex - 97) * k) % 26 + 97) 
#     return cipherText

# def decrypt(cipherText, k):
#     k = module_inverse(k)
#     if k != 0:
#         plainText = ""
#         for i in range(len(cipherText)):
#             charIndex = ord(cipherText[i])
#             if charIndex == 32:
#                 plainText += " "
#             elif charIndex >= 65 and charIndex <= 90:
#                 plainText += chr(((charIndex - 65) * k) % 26 + 65) 
#             else:
#                 plainText += chr(((charIndex - 97) * k) % 26 + 97) 
#         return plainText
#     return 0 

# def multiplicativeCipher_encode():
#     print('Nhập bản rõ: ')
#     plainText = str(input())
#     print("Nhập k: ")
#     k = int(input())
#     while k < 0:
#         print("Nhập lại k: ")
#         k = int(input())
#     cipherText = encrypt(plainText, k)
#     print('Bản mã: %s' % cipherText)

# def multiplicativeCipher_decode():
#     print('Nhập bản mã: ')
#     cipherText = str(input())
#     print("Nhập k: ")
#     k = int(input())
#     while k < 0:
#         print("Nhập lại k: ")
#         k = int(input())
#     plainText = decrypt(cipherText, k)
#     if plainText == 0:
#         print('Không thể giải mã !')
#     else:
#         print('Bản mã: %s' % plainText)

# # Main
# multiplicativeCipher_encode()
# multiplicativeCipher_decode()
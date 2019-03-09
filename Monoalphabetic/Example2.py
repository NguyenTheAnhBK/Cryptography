# -*- coding: utf-8 -*-

# Mã hóa chuỗi ký tự bất kỳ sử dụng mật mã nhân (không mã hóa khoảng trống)

def gcd(a, b):
    while b > 0:
        q = a // b
        r = a - b*q
        a, b = b, r
    return a

# Hàm tìm nghịch đảo của k (k')
def module_inverse(k, n): # với n bất kỳ
    t1, t2 = 0, 1
    while k > 0:
        q = n // k
        r = n - k*q
        n, k = k, r
        t = t1 - t2*q
        t1, t2 = t2, t
    if n == 1: 
        return t1
    else:
        return 0 # với 0 là không tồn tại nghịch đảo của k với phép module n

# Hàm mã hóa mật mã nhân
def encode(plainText, k):
    cipherText = ""
    for i in range(len(plainText)):
        if plainText[i] == " ":
            cipherText += plainText[i] # += " "
        else:
            cipherText += chr((((ord(plainText[i]) - 33) * k ) % 94) + 33 ) # 94 = 126 - 33 + 1
    return cipherText

# Hàm giải mã mật mã nhân
def decode(cipherText, k):
    k = module_inverse(k, 94)
    if k != 0:
        plainText = ""
        for i in range(len(cipherText)):
            if cipherText[i] == " ":
                plainText += cipherText[i] # += " "
            else:
                plainText += chr((((ord(cipherText[i]) - 33) * k ) % 94) + 33 ) # 94 = 126 - 33 + 1
        return plainText
    return 0 # Không thể giải mã được

print("Nhập chuỗi cần mã hóa: ")
plainText = str(input())
print("Nhập k: ")
k = int(input())

cipherText = encode(plainText, k) 
print(cipherText)
print(decode(cipherText, k))

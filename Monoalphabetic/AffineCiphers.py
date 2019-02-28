#-*- coding: utf-8 -*-
# Mật mã affine: là sự kết hợp của mật mã nhân và mật mã cộng (ceasar)
# Công thức: 
    # Mã hóa: C = (P*k1 + k2) mod 26
    # Giải mã: P = ((C-k2)*k1') mod 26

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Mã hóa:
def Encrypt(input_string, k1, k2): #với k1 là khóa của mật mã nhân, k2 là khóa của mật mã cộng
    output_string = ""
    input_len = len(input_string)
    for i in range(input_len):
        output_string += alphabet[(alphabet.find(input_string[i])*k1 + k2)%26]
    return output_string

# Giải mã:
def Decrypt(input_string, k1, k2):
    output_string = ""
    input_len = len(input_string)
    for i in range(input_len):
        output_string += alphabet[((alphabet.find(input_string[i]) - k2)*k1)%26]
    return output_string

# Tìm nghịch đảo của k1 (k1')
def mudule_inverse(k1, n): # n= 26 (số ký tự bảng chữ cái không phân biệt hoa thường)
    t1, t2 = 0, 1
    while(k1>0):
        q = n // k1 #// phép chia hết
        r = n - k1*q
        n, k1 = k1, r
        t = t1 - t2*q
        t1, t2 = t2, t
    if n==1: # vì gcd(k1, n)=1 điều kiện tồn tại mật mã nhân
        return t1 
    return 0 # Không tồn tại khả nghịch của k

plainText = "LYTHUYETMATMA"
cipherText = Encrypt(plainText, 5, 12)
print(cipherText)
print(Decrypt(cipherText, mudule_inverse(5, 26), 12))
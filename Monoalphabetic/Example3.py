# -*- coding: utf-8 -*-

# Mã hóa chuỗi ký tự bất kỳ trong bảng mã ASCII sử dụng mật mã Affine
# Lưu ý: Không mã hóa khoảng trống

# Hàm tính GCD
def gcd(a, b):
    while b > 0:
        q = a // b
        r = a - b *q
        a, b = b, r
    return a

# Hàm tìm nghịch đảo module N của k
def module_inverse(k, N = 94):
    t1, t2 = 0, 1 # định lý Euclid mở rộng: (s * N + t * k ) mod N = gcd(a, b) mod N = 1 do điều kiện tồn tại mật mã nhân 
    # suy ra: (t * k ) mod N = 1 => tồn tại nghịch đảo module N của k => k' = t
    while k > 0:
        q = N // k
        r = N - k * q
        N, k = k, r
        t = t1 -t2 * q
        t1, t2 = t2, t
    if N == 1:
        return t1
    return 0 # Không tồn tại nghịch đảo module n của k

# Hàm mã hóa Affine
def encrypt(plainText, k1, k2):
    cipherText = ""
    for i in range(len(plainText)):
        if plainText[i] == " ":
            cipherText += " "
        else:
            cipherText += chr(((ord(plainText[i]) - 33) * k1 + k2) % 94 + 33)
    return cipherText

# Hàm giải mã Affine
def decrypt(cipherText, k1, k2):
    k1 = module_inverse(k1)
    if k1 != 0:
        plainText = ""
        for i in range(len(cipherText)):
            if cipherText[i] == " ":
                plainText += " "
            else:
                plainText += chr(((ord(cipherText[i]) - 33 - k2) * k1) % 94 + 33)
        return plainText
    return 0

cipherText = encrypt("Nguyen the anh 121 21421", 11, 100)
print(cipherText)
print(decrypt(cipherText, 11, 100))
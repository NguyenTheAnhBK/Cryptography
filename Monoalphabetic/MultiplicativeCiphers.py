#-*- coding: utf-8 -*-
#Mật mã nhân
# C = (P*k) mod 26
# P = (C*k') mod 26
# Với k' là khả nghịch của k theo module n
# k và k' thỏa mãn: k*k' đồng dư 1 (mod n)
# Không phải lúc nào k' cũng tồn tại . Vd: k=4 ta không thể tìm được khả nghịch của k theo module n
# Có thể chứng minh được rằng: k' luôn luôn tồn tại nếu gcd(k, n) = 1 (gcd là ƯCLN)

alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Giải thuật mã hóa
def encrypted(string_input, k):
    string_output = ""
    input_len = len(string_input)
    for i in range(input_len):
        string_output += alpha_upper[(alpha_upper.find(string_input[i]) * k) % len(alpha_upper)]
    return string_output

#Giải thuật giải mã
def decrypted(string_input, k): #k' là khả nghịch của k theo module n
    string_output = ""
    input_len = len(string_input)
    for i in range(input_len):
        string_output += alpha_upper[(alpha_upper.find(string_input[i]) * k) % len(alpha_upper)]
    return string_output

#Tìm khả nghịch của k
def module_inverse(n, k): #với n = 26
    t1, t2 = 0, 1
    while(k > 0):
        q = n // k
        r = n - q*k
        n, k = k, r
        t = t1 - t2*q
        t1, t2 = t2, t
    if n == 1:
        return t1 # t1 là k'
    return 0 # Không tồn tại khả nghịch của k thưo module n

#Test
ciphertext = encrypted("LYTHUYETMATMA", 5)
print(ciphertext)
#Giải mã
plaintext = print(decrypted(ciphertext, module_inverse(26, 5)))
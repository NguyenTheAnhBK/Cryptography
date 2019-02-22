#-*- coding: utf-8 -*-
#Mật mã cộng
    # Mã hóa: C = (P + k) mod 26
    # Giải mã: P = (C - k) mod 26

alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def Encrypted(string_input, k):
    string_output = ""
    input_len = len(string_input)
    for i in range(input_len):
        string_output += alpha_upper[(alpha_upper.find(string_input[i]) + k) % 26]

    return string_output

def Decrypted(string_input, k):
    string_output = ""
    input_len = len(string_input)
    for i in range(input_len):
        string_output += alpha_upper[(alpha_upper.find(string_input[i]) - k) % 26]

    return string_output


ciphertext = Encrypted("HELLO", 15)
print(ciphertext)
print(Decrypted(ciphertext, 15))


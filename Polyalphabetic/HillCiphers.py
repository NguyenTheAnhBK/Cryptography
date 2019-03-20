#-*- coding: utf-8 -*-
import numpy as np


def stringToMatrix(text, m):
    if len(text) % m  == 0:
        return np.array([[ord(i) for i in text]]).reshape((-1, m))
    return np.zeros((2, 2))

def matrixToString(matrix):
    array = np.ravel(matrix)
    text = ""
    for i in array:
        text += chr(i)
    return text;

def getChildMatrix(matrix, p, q):
    childMatrix = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i != p and j != q: 
                childMatrix.append(matrix[i][j])
    x = np.asarray(childMatrix).reshape((matrix.shape[0] - 1, -1))
    return np.asarray(childMatrix).reshape((matrix.shape[0] - 1, -1))

def moduleInverse(k, N):
    t1, t2 = 0, 1
    while k > 0:
        q = N // k
        r = N - k*q
        N, k = k, r
        t = t1 - t2*q
        t1, t2 = t2, t
    if N == 1:
        return t1
    return 0

def multiplicativeInverse(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        print("Ma tran khoa phai la ma tran vuong")
        return np.zeros_like(matrix)
    
    detMatrix = int(np.linalg.det(matrix) % 26)
    detInverse = moduleInverse(detMatrix, 26)
    if detInverse != 0:
        inverseMatrix = np.zeros_like(matrix)
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                x = int(np.linalg.det(getChildMatrix(matrix, i, j)))
                inverseMatrix[i][j] = (-1)**(i+j) * round(np.linalg.det(getChildMatrix(matrix, i, j)))
        return (detInverse * np.transpose(inverseMatrix)) % 26
    return np.zeros_like(matrix)

def hillCipherEncrypt(plainText, k):
    if k.shape[0] != k.shape[1]:
        print("Khoa k phai la ma tran vuong")
    else:
        matrixPlainText = stringToMatrix(plainText, k.shape[0])
        if matrixPlainText.all() == 0:
            print("Khoa k khong hop le!")
        else:
            cipherText = (matrixPlainText - 65 ).dot(k) % 26
            cipherText = matrixToString(cipherText + 65)
            return cipherText
    return 0

def hillCipherDecrypt(cipherText, k):
    k_inv = multiplicativeInverse(k)
    if k_inv.all() == 0:
        print("Khong the giai ma")
        return 0
    matrixCipherText = stringToMatrix(cipherText, k.shape[0])
    if matrixCipherText.all() == 0:
        print("Khoa k khong hop le!")
        return 0
    plainText = (matrixCipherText - 65).dot(k_inv) % 26
    plainText = matrixToString(plainText + 65)
    return plainText
# plainText = "abc"
# k = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
# print(matrixToString(k))
k = np.array([[3, 3], [2, 5]])
# k_inv = multiplicativeInverse(k)
# print((stringToMatrix("HELP", 2) - 65) % 26)
# cipherText1 = (stringToMatrix("HELP", 2) - 65).dot(k) % 26
# # x = (stringToMatrix("ACT") - 65).reshape((-1, 1))
# # cipherText2 = k.dot(x) % 26
# cipherText1 = matrixToString(cipherText1 + 65)
# # print(matrixToString(cipherText2 + 65))
# plainText1 = (stringToMatrix(cipherText1, 2)  - 65).dot(k_inv) % 26
# print(matrixToString(plainText1 + 65))
cipherText = hillCipherEncrypt("HELP", k)
print(cipherText)
print(hillCipherDecrypt(cipherText, k))

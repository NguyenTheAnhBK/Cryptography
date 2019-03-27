#-*- coding: utf-8 -*-
# C = (P*K) mod 26
# P = (C*K-1) mod 26, K-1 la ma tran nghich dao cua K
import numpy as np

def stringToMatrix(text, m):
    k = (m - len(text) % m ) % m # Số ký tự cần thêm vào chuỗi
    while k:
        text += 'z'
        k -= 1
    return np.array([[ord(i) for i in text]]).reshape((-1, m))

def matrixToString(matrix):
    array = np.ravel(matrix)
    text = ""
    for i in array:
        text += chr(i)
    return text

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
    return 0 # không tồn tại nghịch đảo module N của k

# hàm lấy ma trận con tại vị trí i, j của ma trận 
def getChildMatrix(matrix, p, q):
    childMatrix = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i != p and j != q:
                childMatrix.append(matrix[i][j])
    return np.asarray(childMatrix).reshape((matrix.shape[0]-1, -1))

# hàm tính ma trận nghịch đảo của ma trận K
def multiplicativeInverse(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        print("Ma tran khoa phai la ma tran vuong")
        return np.zeros_like(matrix)
    
    detMatrix = int(np.linalg.det(matrix) % 26)
    detMatrixInverse = moduleInverse(detMatrix, 26)

    if detMatrix != 0:
        inverseMatrix = np.zeros_like(matrix)
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                x = np.linalg.det(getChildMatrix(matrix, i, j))
                inverseMatrix[i][j] = (-1)**(i+j) * round(x)
        return (detMatrixInverse * np.transpose(inverseMatrix)) % 26
    return np.zeros_like(matrix)

def hillCipherEncrypt(plainText, k):
    if k.shape[0] != k.shape[1]:
        print("Ma tran khoa phai la ma tran vuong")
        return 0
    matrixPlainText = stringToMatrix(plainText, k.shape[0])
    cipherText = (matrixPlainText - 97).dot(k) % 26
    cipherText = matrixToString(cipherText + 97)
    return cipherText

def hillCipherDecrypt(cipherText, k):
    k_inv = multiplicativeInverse(k)
    if k_inv.all() == 0:
        print("khong the giai ma voi khoa k")
        return 0
    matrixCipherText = stringToMatrix(cipherText, k.shape[0])
    plainText = (matrixCipherText - 97).dot(k_inv) % 26
    plainText = matrixToString(plainText + 97)
    return plainText

k = np.array([[3, 3], [2, 5]])
cipherText = hillCipherEncrypt("help", k)

print(cipherText)
print(hillCipherDecrypt(cipherText, k))
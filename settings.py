from Crypto.Random import *
import random
import math

KEY = b'Bv\xaf\x9c\xab\xafkc\xce\x12\xcf\xbfF\xf1\xca\xef'

def generateKeys():
    p = random.getrandbits(16)
    while is_prime(p) == False:
        p = random.getrandbits(16)
    q = random.getrandbits(16)
    while is_prime(q) == False:
        q = random.getrandbits(16)
    #q will always be largest number
    if p > q:
        x = p
        p = q
        q = x
    n = p*q
    theta = (p-1)*(q-1)
    e = gcd(theta, n)
    d = pow(e, -1, theta)
    h, d = pulverizor(theta, e)
    return n, e, p, q, d%theta

def rsaEncrypt(m, n, e):
    msg = to_IntArray(m)
    cipher = ""
    for ms in msg:
        cipher += str(pow(ord(ms), e, n)) + " "
    return cipher
    
def rsaDecrypt(y, n, p, q, d):
    cipher = y.split(" ")
    decr = ""
    for i in range(2,len(cipher[:-2])):
        c = cipher[i]
        A = pow(int(c), d%(p-1), p)
        B = pow(int(c), d%(q-1), q)
        qPrime, pPrime = pulverizor(q, p)
        m = (A*q*qPrime + B*p*pPrime)%n
        decr += str(chr(m))
    return decr

def gcd(e, n):
    for i in range(3, n):
        x = e
        y = i
        while y != 0:
            a = y
            y = x % y
            x = a
        if x == 1:
            return i

def is_prime(num): 
    if num > 1:
        for i in range(2, math.ceil(num/2)):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
    else:
        return False
    return True

def pulverizor(q, p):
    A = q
    B = p
    Q = math.floor(A/B)
    R = A%B
    X1 = 1
    Y1 = 0
    X2 = 0
    Y2 = 1
    while R != 0:
        a = B
        b = R
        q = math.floor(a/b)
        r = a%b
        x1 = X2
        y1 = Y2
        x2 = X1-(Q*X2)
        y2 = Y1-(Q*Y2)
        A = a
        B = b
        Q = q
        R = r
        X1 = x1
        Y1 = y1
        X2 = x2
        Y2 = y2
    return X2, Y2

def to_IntArray(msg):
    array = [*str(msg)]
    return [*str(msg)]

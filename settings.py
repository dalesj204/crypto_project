from Crypto.Random import *
import random
import math

KEY = b'Bv\xaf\x9c\xab\xafkc\xce\x12\xcf\xbfF\xf1\xca\xef'

def generateKeys():
    p = random.getrandbits(64)
    while is_prime(p):
        p = random.getrandbits(64)
    q = random.getrandbits(64)
    while is_prime(q) :
        q = random.getrandbits(64)
    #q will always be largest number
    if p > q:
        x = p
        p = q
        q = x
    n = p*q
    theta = (p-1)*(q-1)
    e = gcd(theta, n)
    d = pow(e, -1, theta)
    return n, e, p, q, d

def rsaEncrypt(m, n, e):
    return pow(m, e, n)

def rsaDecrypt(y, n, p, q, d):
    A = pow(y, d%(p-1), p)
    B = pow(y, d%(q-1), q)
    qPrime, pPrime = pulverizor(q, p)
    m = (A*q*qPrime + B*p*pPrime)%n
    return m

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
                return True
            else:
                return False
    else:
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
    return X2%p, Y2%q
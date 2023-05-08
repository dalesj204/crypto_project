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
    n = p*q
    theta = (p-1)*(q-1)
    e = gcd(theta, n)
    d = pow(e, -1, theta)
    return n, e, p, q, d

def rsaEncrypt(n, e):
    print("unfinished")

def rsaDecrypt(n, e, p, q, d):
    print("unfinished")

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
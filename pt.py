import random

def CheckA(n,a):
    d = (n-1)//2
    while(d%2==0):
        if (pow(a,d,n) == n-1):
            return True
        d = d//2
    tmp = pow(a,d,n)
    if tmp == n-1 or tmp ==1:
        return True
    else:
        return False

def prime(N):
    a = 97
    while(not(CheckA(N,a)) or N%a == 0):
        N = N + 1
    return N

print(prime(75768765656547))

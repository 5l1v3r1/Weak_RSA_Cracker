#JYCSEC
from Crypto.PublicKey import RSA
import fractions

#f = open(raw_input("Enter pub key: "),'r')
f = open ('key.pub','r')
key = RSA.importKey(f.read())
print ("n is = " + str(key.n))
print ("e is = " + str(key.e))

n=key.n
t = 0
for i in range(1,n+1):
    if fractions.gcd(n,i)==1:
        t += 1
print ("Euler Totient is " + str(t))


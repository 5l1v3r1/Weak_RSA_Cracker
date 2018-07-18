#JYCSEC
from Crypto.PublicKey import RSA
import fractions

#f = open(raw_input("Enter pub key: "),'r')
f = open ('key.pub','r')
key = RSA.importKey(f.read())
print ("n is = " + str(key.n))
print ("e is = " + str(key.e))

t = 0
for i in range(1,key.n+1):
    if fractions.gcd(key.n,i)==1:
        t += 1
print ("Euler Totient is " + str(t))
priv_key = RSA.construct(key.n,key.e,t)
out = priv_key.decrypt(open(raw_input("Enter encrypted file: "),'r'))
print ("Decrypted message is" + out)
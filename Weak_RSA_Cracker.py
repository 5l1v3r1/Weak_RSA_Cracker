#JYCSEC
from Crypto.PublicKey import RSA

#f = open(raw_input("Enter pub key: "),'r')
f = open ('key.pub','r')
key = RSA.importKey(f.read())
print "n is = " + str(key.n)
print "e is = " + str(key.e)

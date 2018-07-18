from Crypto.PublicKey import RSA

f = open(raw_input("Enter pub key: "),'r')
key = RSA.importKey(f.read())
print key.n
print key.e
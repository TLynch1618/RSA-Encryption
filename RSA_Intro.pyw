import math
import numpy

#This is an example of RSA I created to teach myself the process.  This code should not be used to encrypt sensitive or commercial information.

#This is a very simple version of the RSA encryption system.  First we pick two prime numbers 'p' and 'q' which are then multiplied together to make the RSA public key 'n'.  There are also constants 'e' and 'k' used in the process.  

p = 13

q = 11

n = p * q

#The constant 'e' must be coprime with the Lowest Common Multiple of p-1 and q-1.  The next several lines establish 'e' and check for this issue.

e = 7

x = numpy.lcm(p-1, q-1)

if x % e == 0:
	print("Warning! The value for e evenly divides x, the LCM.")

k = 2

#For the decryption side, we must find a number 'd' such that 1 = (d * e) % LCM(p-1,q-1).  The next six lines ultimately find and define 'd'.  

j = 0

r = 0

while r != 1:
	j = j + 1
	r = (j * e) % x

d = j

print('The value of the public key is: ' + str(n))

#Let's request the message to be encrypted and store it as variable 'msg'.

msg = input("Enter the message to be encrypted: ")

#Now we begin encrypting the user-entered message from above.  First we establish an array "msgarr" to hold the message.

msgarr = []

#Here we need to convert the characters of the message into numbers upon which we will mathematically operate.  For this example we can use ord().

for i in range(len(msg)):

	msgarr.append(ord(msg[i]))

#'msgarr' is an array of numbers ready to be encrypted (variable 'enc') via this for loop. The encrypted values then get added to 'cipherarr' to be sent to the recipient.

cipherarr = []

for i in range(len(msgarr)):

	enc = ((msgarr[i])**e) % n

	cipherarr.append(enc)

print('The user-entered message has been converted to ciphertext: ')

print(cipherarr)

#The cipher text has been sent and received.  We are ready to decrypt the original message.  Let's establish 'decryptedarr' to hold the decrypted values.  After that, we cycle through the cipherarr and decrypt each entry (variable 'dec').  Then the decrypted entry gets added to 'decryptedarr'.

decryptedarr = []

for i in range(len(cipherarr)):

	dec = ((cipherarr[i])**d) % n

	decryptedarr.append(dec)

#Finally, we setup a string 'deliveredmsg'.  The code uses the chr() function to reverse ord() above where we converted from characters into integers.

deliveredmsg = ""

for i in range(len(decryptedarr)):

	deliveredmsg = deliveredmsg + chr(decryptedarr[i])

print('The transmitted message has been decrypted to read: ' + deliveredmsg)





















import math
import numpy

#This is an example of RSA-cracking I created to teach myself the process.  This code should not be used to decrypt any RSA or other encrypted information.

#This is a simple introduction to the idea behind bruteforce breaking an RSA-encrypted message. Given a public key 'n', this code runs through a short list of primes (list variable 'primes') to factor the public key. Since this is a simple example it is limited to the requirement that the public key be comprised of at least one prime within the search list.

primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

#Here the user would need to enter the correct public key for the "stolen message".  I also use counter variable 's' and beginng prime z = 2 to initiate the while loop that checks all of the list 'primes' above for a possible factorization of public key 'n'.  The public key entered currently matches the corresponding RSAIntro code

n = 143

s = 0

z = 2

while n % z != 0:

	z = n / primes[s]

	s = s + 1

#So long as the public key 'n' is comprised of one of the primes listed, we now have 'p' and 'q' from the RSAIntro file.  For simplicity, we will make assumptions of 'e' and 'k' which also match the RSAIntro file.  From here we follow the standard decryption protocol.

p = int(z)

q = int(n / z)

e = 7

k = 2

x = numpy.lcm(p-1, q-1)

#For the decryption side, we must find a number 'd' such that 1 = (d * e) % LCM(p-1,q-1).  The next six lines ultimately find and define 'd'.  

j = 0

r = 0

while r != 1:
	j = j + 1
	r = (j * e) % x

d = j

#Now that the basics are covered, we are ready to decrypt the intercepted message.  Let's establish 'decryptedarr' to hold the decrypted values.  After that, we cycle through the cipherarr and decrypt each entry.  Then the decrypted entry gets added to 'decryptedarr'.

decryptedarr = []

#The cipher array (variable 'cipherarr') value(s) must be copied and pasted below from the RSAIntro file which prints its 'cipherarr' halfway through the code.  The array shown now is from a sample run of the RSAIntro file when the 'msg' entered was: The quick, brown fox jumps over the lazy dog.

cipherarr = [72, 91, 62, 98, 9, 39, 118, 44, 68, 99, 98, 32, 49, 45, 37, 33, 98, 119, 45, 120, 98, 50, 39, 21, 18, 80, 98, 45, 79, 62, 49, 98, 129, 91, 62, 98, 4, 59, 34, 121, 98, 100, 45, 38, 84, 98]

#Let's loop through 'cipherarr' to decrypt (variable 'dec') each entry and append it to 'decryptedarr' as promised.

for i in range(len(cipherarr)):

	dec = ((cipherarr[i])**d) % n

	decryptedarr.append(dec)

#Finally, we setup a string 'interceptedmsg'.  The code uses the chr() function to reverse ord() in the RSAIntro code where we converted from characters into integers.

interceptedmsg = ""

for i in range(len(decryptedarr)):

	interceptedmsg = interceptedmsg + chr(decryptedarr[i])

print('The intercepted message has been decrypted to read: ' + interceptedmsg)


















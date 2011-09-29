"""
@author Angad Singh
Adapted from MIT CS6.006 
"""
import sys

class RollingHash:

	def __init__(self, base = 256, prime = 1009):
		self.hash_value = 0
		self.base = base
		self.prime = prime
		# inv_base = base * inv_base % prime = 1
		# base^(prime-2) % prime
		self.inv_base = pow(base, prime - 2, prime) 
		self.skip_multiplier = 1
		
	def append(self, value):
		self.hash_value = (self.hash_value * self.base + value) % self.prime
		self.skip_multiplier = (self.skip_multiplier * self.base) % self.prime
	
	def skip(self, value):
		self.skip_multiplier = (self.skip_multiplier * self.inv_base) %self.prime
		self.hash_value = (self.hash_value + self.prime - (value * self.skip_multiplier) % self.prime) % self.prime

class KarpRabin:

	def search(self, str, sub):
		ht = RollingHash()
		hs = RollingHash()
		
		for c in sub: hs.append(ord(c))
		for c in str[:len(sub)]: ht.append(ord(c))
		
		if ht.hash_value == hs.hash_value:
			return True
			
		for i in range(len(sub), len(str)): 
			ht.skip(ord(str[i-len(sub)]))
			ht.append(ord(str[i]))
			if ht.hash_value == hs.hash_value:
				if sub == str[i-len(sub)+1:i+1]:
					return True
		return False

def main():
	if len(sys.argv) != 3:
		print "Usage: karp_rabin.py string substring"
		exit()

	kr = KarpRabin()
	str = sys.argv[1]
	sub = sys.argv[2]
	print kr.search(str, sub)

if __name__ == "__main__":
	import profile
	profile.run("main()")
"""
@author Angad Singh
Adapted from MIT CS6.006 
"""

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
				return True
		return False
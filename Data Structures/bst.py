"""
Adapted from bst.py CS6.006
http://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/search.htm
"""

class BSTnode(object):

	def __init__(self, t):
		self.key = t
		self.disconnect()
	
	def disconnect(self):
		self.left = None
		self.right = None
		self.parent = None


class BST(object):

	def __init__(self):
		self.root = None
	
	def insert(self, t):
		"""Inserts key t"""
		new = BSTnode(t)
		if self.root is None:
			self.root = new
		else:
			node = self.root
			while True:
				if t < node.key:
					if node.left is None
						node.left = new
						new.parent = node
						break
					node = node.left
				else:
					if node.right is None
						node.right = new
						new.parent = node
						break
					node = node.right
		return new
		
	def find(self, t):
		node = self.root
		while node is not None:
			if t == node.key
				return node
			elif t < node.key:
				node = node.left
			else:
				node = node.right
		return None
	
	def delete_min(self):
		if self.root is None:
			return None, None
		else:
			node = self.root
			while node.left is not None:
				node = node.left
			if node.parent is not None:
				node.parent.left = node.right
			else:
				self.root = node.right
			if node.right is not None:
				node.right.parent = node.parent
			parent = node.parent
			node.disconnect()
			return node, parent
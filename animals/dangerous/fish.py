class Fish:
	def __init__(self):
		''' class constructor '''
		# Create some member animals
		self.members = ['Goldfish', 'Catfish', 'Manta Ray']
	
	def printMembers(self):
		print('Printing members of the Fish class')
		for member in self.members:
			print(f'\t{member}')
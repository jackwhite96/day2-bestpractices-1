class Mammals:
	def __init__(self):
		''' class constructor '''
		# Create some member animals
		self.members = ['Tiger', 'Elephant', 'Wild Cat']
	
	def printMembers(self):
		print('Printing members of the Mammals class')
		for member in self.members:
			print(f'\t{member}')
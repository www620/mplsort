b = 128

class Data:
	def __init__(self, i):
		self.value = i
		self.c = (0, 1 - i / b / 2, i / b / 2 + 0.5)
		self.color = self.c


import shapely as sh

class Obstacle:
	def __init__(self,name, origin, shape, blocking = False):
		self.name = name
		self.origin = origin
		self.blocking = blocking
		self.shape = shape

	@property
	def passable(self):
		return not self.blocking
	


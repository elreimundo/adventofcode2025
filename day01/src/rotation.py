from .direction import Direction

class Rotation:
	def __init__(self, direction: Direction, amount: int):
		self.direction = direction
		self.amount = amount

	def __eq__(self, other) -> bool:
		return isinstance(self, other.__class__) and self.direction == other.direction and self.amount == other.amount

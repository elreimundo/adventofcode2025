from .direction import Direction
from .rotation import Rotation

from typing import List

class CombinationLock:
	def __init__(self, *, ticks: int, initial_value: int, target_value: int = 0):
		self.ticks = ticks
		self.value = initial_value
		self.target_value = target_value
		self.target_value_count = 0
		self.click_count = 0

	def rotate(self, rotation: Rotation):
		new_value = self.value
		remaining_value = rotation.amount
		while remaining_value > 0:
			this_rotation_amount = min(remaining_value, self.ticks)
			possible_new_value = new_value + this_rotation_amount * (1 if rotation.direction == Direction.RIGHT else -1)
			modular_new_value = possible_new_value % self.ticks
			if (
				(
					possible_new_value != modular_new_value # went through zero
					and not (new_value == 0 and modular_new_value != 0) # ignore turns starting at 0, especially leftward turns
				)
				or modular_new_value == self.target_value # landing on 0
			):
				self.click_count += 1
			new_value = modular_new_value
			remaining_value -= this_rotation_amount
		if new_value == self.target_value:
			self.target_value_count += 1
		self.value = new_value

	def multi_rotate(self, rotations: List[Rotation]):
		for rotation in rotations:
			self.rotate(rotation)

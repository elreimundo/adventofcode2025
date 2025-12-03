import os

from src.parser import parse
from src.combination_lock import CombinationLock

inputs = open(os.path.join(os.path.dirname(__file__), "rotations.my_data"), "r").readlines()

lock = CombinationLock(
	ticks = 100,
	initial_value = 50
)

lock.multi_rotate(parse(inputs))

print(lock.target_value_count)
print(lock.click_count)
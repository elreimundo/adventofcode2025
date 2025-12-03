from day01.src.combination_lock import CombinationLock
from day01.src.direction import Direction
from day01.src.rotation import Rotation

def test_combination_lock():
	lock = CombinationLock(ticks = 100, initial_value = 0)
	lock.rotate(Rotation(Direction.RIGHT, 20))
	assert(lock.value == 20)
	lock.rotate(Rotation(Direction.LEFT, 5))
	assert(lock.value == 15)
	lock.rotate(Rotation(Direction.LEFT, 30))
	assert(lock.value == 85)
	lock.rotate(Rotation(Direction.RIGHT, 40))
	assert(lock.value == 25)

def test_target_count():
	lock = CombinationLock(ticks = 100, initial_value = 50)
	lock.multi_rotate([
		Rotation(Direction.LEFT, 68),
		Rotation(Direction.LEFT, 30),
		Rotation(Direction.RIGHT, 48),
		Rotation(Direction.LEFT, 5),
		Rotation(Direction.RIGHT, 60),
		Rotation(Direction.LEFT, 55),
		Rotation(Direction.LEFT, 1),
		Rotation(Direction.LEFT, 99),
		Rotation(Direction.RIGHT, 14),
		Rotation(Direction.LEFT, 82),
	])
	assert(lock.target_value_count == 3)

def test_click_count_with_lots_of_turns():
	lock = CombinationLock(ticks = 100, initial_value = 50)
	lock.multi_rotate([
		Rotation(Direction.LEFT, 68),
		Rotation(Direction.LEFT, 30),
		Rotation(Direction.RIGHT, 48),
		Rotation(Direction.LEFT, 5),
		Rotation(Direction.RIGHT, 60),
		Rotation(Direction.LEFT, 55),
		Rotation(Direction.LEFT, 1),
		Rotation(Direction.LEFT, 99),
		Rotation(Direction.RIGHT, 14),
		Rotation(Direction.LEFT, 82),
	])
	assert(lock.click_count == 6)
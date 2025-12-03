from day01.src.parser import parse
from day01.src.rotation import Rotation
from day01.src.direction import Direction

def test_parse():
	test_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".splitlines()
	expected = [
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
	]
	assert(parse(test_input) == expected)

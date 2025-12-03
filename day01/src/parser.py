from .direction import Direction
from .rotation import Rotation

direction_mapping = { 'R': Direction.RIGHT, 'L': Direction.LEFT }

def parse(lines: list[str]) -> list[Rotation]:
	rotations = []
	for line in lines:
		[letter, *digits] = list(line)
		if letter in direction_mapping:
			rotations.append(
				Rotation(
					direction_mapping[letter],
					int(''.join(digits))
				)
			)
		else:
			raise ValueError(f'received invalid direction {letter}')
	return rotations

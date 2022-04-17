# Guess number

import random

r = random.randint(1, 100)

while True:
	r_input = input('Please take a guess: ')
	r_input = int(r_input)

	if r_input == r:
		print('You are right!')
		break

	elif r_input < r:
		print('The number is bigger than your guess.')

	elif r_input > r:
		print('The number is smaller than your guess.')

	
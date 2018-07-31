colors = ['red', 'green', 'yellow', 'black', 'purple', 'blue']

for color in colors:
	print(color.title())

print('-'*40)

color_it = iter(colors)

while True:
	try:
		color = next(color_it)
		print(color.title())
	except StopIteration:
		break

print('DONE')

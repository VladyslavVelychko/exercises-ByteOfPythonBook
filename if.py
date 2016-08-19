number=23
guess=int(input('Введите свое число: '))
if guess==number:
	print('Поздравляю, вы угадали!')
elif guess<number:
	print('Указанное число немного больше.')
else:
	print('Указанное число немного меньше.')
print('Завершено.')

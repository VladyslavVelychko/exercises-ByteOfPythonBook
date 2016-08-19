number=23
running=True
while running:
	guess=int(input('Введите число: '))
	
	if guess==number:
		print('Поздравляю, Вы угадали!')
		running=False
	elif guess<number:
		print('Указанное число больше.')
	else:
		print('Указанное число меньше.')
else:
	print('Цикл while завершено.')
print('Завершено.')

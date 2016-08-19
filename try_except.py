try:
	text=input('Введите что-то:')
except EOFError:
	print('Зачем вы сделали мне EOF?')
except KeyboardInterrupt:
	print('Вы отменили операцию.')
else:
	print('Вы ввели {0}'.format(text))

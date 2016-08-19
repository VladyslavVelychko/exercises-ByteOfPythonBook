class ShortInputException(Exception):
	def __init__(self,length,atleast):
		Exception.__init__(self)
		self.length=length
		self.atleast=atleast

try:
	text=input('Введите что-нибудь:')
	if len(text)<3:
		raise ShortInputException(len(text), 3)

except EOFError:
	print('Зачем вы сделали мне EOF?')
except KeyboardInterrupt:
	print('Вы отменили операцию.')
except ShortInputException as ex:
	print('ShortInputException: Длина введённой строки -- {0} \nОжидалось, как минимум, {1}.'.format(ex.length,ex.atleast))
else:
	print('Без исключений.')

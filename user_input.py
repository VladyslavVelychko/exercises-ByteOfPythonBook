def reverse(text):
	return text[::-1]

def is_palindrome(text):
	return text == reverse(text)
smth=input('Введите текст: ')
if (is_palindrome(smth)):
	print('Да, это палиндром.')
else:
	print('Нет, это не палиндром.')

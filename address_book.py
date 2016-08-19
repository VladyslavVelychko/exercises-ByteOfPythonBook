import os
import time

def choose():
	
	print('0. Показать текущую адресную книгу')
	print('1. Добавить контактные данные')
	print('2. Изменить контактные данные')
	print('3. Удалить контактные данные')
	print('4. Искать контактные данные')

def save():
	print('Нужно сохранить эту информацию в файл?(0-да, 1-нет)')
	num=int(input())
	if num==0:
		f=open('text.txt','w') #Открываем для записи(writing)
		f.write(str(ab)) #записываем текст в файл
		f.close() #закрываем файл

		f=open('text.txt')

		while True:
			line=f.readline()
			if len(line)==0:
				break
			print(line)

		f.close()
	else:
		return 0

def numbers():
	global ab
	ab={'Swaroop': 'swaroop@swaroopch.com',
	'Larry': 'larry@wall.org',
	'Spammer': 'spammer@hotmail.com',
	'Vlad': 'velyk95@gmail.com'}
	number=int(input())
	if number==0:
		for name,address in ab.items():
			print('Контакт {0} с адресом {1}.'.format(name,address))

	elif number==1:
		print('Введите имя')
		name1=input()
		print('Введите адрес')
		address1=input()
		ab[name1]=address1
		if name1 in ab:
			print('Добавлен контакт {0} {1}.'.format(name1,ab[name1]))
		print('Теперь адрессная книга выглядит так!')
		for name,address in ab.items():
			print('Контакт {0} с адресом {1}.'.format(name,address))
		save()
	elif number==2:
		for name,address in ab.items():
			print('Контакт {0} с адресом {1}.'.format(name,address))
		print('Введите имя, которое нужно изменить')
		name2=input()
		print('Введите измененный адрес для этого имени')
		address2=input()
		name=name2
		print('Добавлен контакт {0} {1}.'.format(name,address2))
	elif number==3:
		for name,address in ab.items():
			print('Контакт {0} с адресом {1}.'.format(name,address))
		print('Введите имя, которое нужно удалить')
		name3=input()
		name=name3
		del ab[name]
		print('Теперь адрессная книга выглядит так!')
		for name,address in ab.items():
			print('Контакт {0} с адресом {1}.'.format(name,address))
		save()
	elif number==4:
		for name,address in ab.items():
			print('Контакт {0} с адресом {1}.'.format(name,address))
		print('Введите имя, которое нужно найти')
		name4=input()
		name=name4
		if name in ab:
			print('Ваш контакт {0} {1}.'.format(name,ab[name]))

def main():
	print('Программа Адресная книга версия 1.0\nВозможности программы(для выбора функции используйте цифры 0..4)')	
	choose()
	numbers()
	
main()

name='Swaroop'
if name.startswith('Swa'):
	print('Да, строка начинается на "Swa"')
if 'a' in name:
	print('Да, она содержит строку "a"')
if name.find('war')!=-1:
	print('Да, она содержит строку "war"')

delimiter='_*_'
mylist=['Бразилия','Украина','Новая Зеландия','Польша']
print(delimiter.join(mylist))

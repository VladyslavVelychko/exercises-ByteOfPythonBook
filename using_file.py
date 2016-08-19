text='Hello World!'

f=open('text.txt','w') #Открываем для записи(writing)
f.write(text) #записываем текст в файл
f.close() #закрываем файл

f=open('text.txt')

while True:
	line=f.readline()
	if len(line)==0:
		break
	print(line)

f.close()

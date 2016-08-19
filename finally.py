import time

try:
	f=open('text.txt')
	while True:
		line=f.readline()
		if len(line)==0:
			break
		print(line,end='')
		time.sleep(2)
except KeyboardInterrupt:
	print('\nВы отменили чтение файла!')
finally:
	f.close()
	print('Очистка, закрытие файла.')

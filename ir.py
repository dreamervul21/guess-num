import random
r = random.randint(1,100)
y = 0
while True:
	y += 1 # y = y+1
	x = input('輸入你猜的數字:')
	x = int(x)
	if x > r:
		print('再小一點')
	elif x < r:
		print('再大一點')
	else:
		print('你猜對了！！共猜了', y,'次')
		break

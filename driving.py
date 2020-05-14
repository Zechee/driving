country = input('Where are you come from: ')
age = input('How old are you: ')
age = int(age)

if country == 'China':
	if age >= 18:
		print('Congratulations, you can take the driving license test')
	else:
		print('Sorry, you connot take the driving license test')

elif country == 'US':
	if age >= 16:
		print('Congratulations, you can take the driving license test')
	else:
		print('Sorry, you connot take the driving license test')
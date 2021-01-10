driving = input('請問有開車經驗嗎?')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if  age >=18: 
		print('你通過驗證了')
	else:
		print('奇怪,你怎開過車')
elif driving == '沒有':
	if age >=18: 
		print('你可以考駕照了,試試看吧')
	else:
		print('再過幾年就能考駕照囉')

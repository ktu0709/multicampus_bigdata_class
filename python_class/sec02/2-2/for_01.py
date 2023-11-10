def for_test01() :
	for res in [1,2,3,4]:
		print(f'{res}',end='')

def for_test02() :
	for res in (1,2,3,4):
		print(f'{res}',end='')

def for_test03() :
	print(range(10),list(range(10)),list(range(0,100,2)))

	for x in range(10):
		print(f'{x}',end=' ')

def for_test04():
	fruit  = ['apple','watermelon','peach','pear']
	if "apple" in fruit or len(fruit) > 5 :
		for m_f in fruit:
			print(m_f)

def for_test05():
	print(list(range(0,100,5)))
	print(list(range(100, 0, -1)))

if __name__ == '__main__':
    #for_test04()
	for s in "abcd" :
		print(s,end=' ')



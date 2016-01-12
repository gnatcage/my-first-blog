print('Hello, Jack!')

print('Is 3 > 2?')
if 3>2:  
	print('Yes')
else:
	print('No')

print('Is your name notJack?')
name = 'notJack'
if name == 'Jack':
	print('Hey Jack!')
elif name == 'notJack':
	print ('Hey notJack!')
else:
	print('Hey anon!')

#define a function 'hi()'
def hi(name):
	print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Jacky']
for name in girls:
	hi(name)
	print('Next girl')
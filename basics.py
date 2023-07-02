print(''' This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond." ''')

name = 'premji'
age = 30
height = 130.1

# print('{0} was {1} years old with {2} height'.format(name, age, height))
print(name + ' is ' + str(age) + ' years old')
#print(('{} was {} years old when he wrote this book').format(name, age))
print('{prem} was {test} years old when he wrote this book'.format(prem=name, test=age))
print(f'Why is {name} playing with that python?')
print('{0:.2f}'.format(1.0/2))
print('{0:_^6}'.format('hello'))
print('This is the first line\nThis is the second line')
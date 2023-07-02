def validate_input(arg):
    if(arg > 5):
        print(f'input is valid {arg}')
    
    else:
        print(f'Please enter valid number', arg)

#validate_input(1)

x = 10
def local_vs_glob_variable(x):
    print('Global value of X is: ', x)
    x = 2
    print('Changed local x to', x)

local_vs_glob_variable(x)
print('x is still', x)


def say(message, times=1):
    print(message * times)

say('Hello')
say('World ', 5)


def total(a=5, *numbers, **phonebook):
    print('a', a)

    #iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)

    #iterate through all the items in dictionary    
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

total(10,1,2,3,Jack=1123,John=2231,Inge=1560)


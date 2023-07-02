numbers = ('one', 'two', 'three')

print('number length is: ', len(numbers))


new_numbers = 'four', 'five', numbers
print('new number length is: ', new_numbers[2][1])

print('total numebrs are', len(numbers)-1+len(new_numbers[2]))


ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])
del ab['Spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for item in ab.items():
    print('Contact {} at {}'.format(item[0], item[1]))
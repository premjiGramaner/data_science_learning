fruites = ['mango', 'orange','apple']

print('These items are:', end=' ')
for item in fruites:
    print(item, end=' ')

fruites.append('rice')

fruites.sort()

print('I have', len(fruites), 'items to purchase.', fruites[0])
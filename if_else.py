print('Guess the codded integer?/n')
number = 25
guess = int(input('Enter the Number: '))

if number == guess:
    print('Congratz you found it {}'.format(guess))
elif guess < number:
    print('No, it is a little higher than that')
else:
    print('No, it is a little lower than that')

print('Done!')


running = True
while running:
    new_guess = int(input('Enter the Number: '))

    if number == new_guess:
        print('Congratz you found it {}'.format(new_guess))
        running = False

    elif new_guess < number:
        print('No, it is a little higher than that')

    else:
        print('No, it is a little lower than that')

else:
    print('The while loop is over.')
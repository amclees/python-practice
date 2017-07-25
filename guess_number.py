import random

number = random.randint(1, 100000)

while True:
    user_input = int(raw_input(''))
    if user_input == number:
        print 'Correct'
        break
    else:
        print 'No, the number is ' + ('smaller' if number < user_input else 'larger')

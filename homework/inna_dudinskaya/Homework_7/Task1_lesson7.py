i = 5
while True:
    user_input = input('Enter a number:')
    if int(user_input) == i:
        break
    else:
        print('Попробуйте снова')
print('Поздравляю! Вы угадали!')

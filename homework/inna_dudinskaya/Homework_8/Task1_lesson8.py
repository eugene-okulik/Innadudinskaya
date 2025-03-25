import random

bonus = random.randrange(0, 3000)
print(bonus)

is_bonus_payed = random.choice([True, False])
print(is_bonus_payed)

user_input = int(input('Enter salary: '))

salaryfinal = user_input + bonus

if is_bonus_payed:
    text = f'{user_input}, {is_bonus_payed} - "${salaryfinal}"'
    print(text)
else:
    text = f'{user_input}, {is_bonus_payed} - "${user_input}"'
    print(text)

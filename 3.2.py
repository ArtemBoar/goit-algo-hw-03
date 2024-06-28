# 2

import random

def get_numbers_ticket(min, max):

    choose_number = random.randint(min, max)

    return choose_number

min = 1
max = 100
quantity = 1

lottery_numbers = get_numbers_ticket(min, max)
print("Ваші лотерейні числа:", lottery_numbers)
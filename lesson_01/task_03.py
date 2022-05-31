import random

random_digits = {}


def random_generator(min_digit, max_digit):
    random_digit = random.randint(min_digit, max_digit)
    random_digits[f'elem_{len(random_digits)}'] = random_digit


for i in range(100):
    random_generator(-17, 10)

print(random_digits)

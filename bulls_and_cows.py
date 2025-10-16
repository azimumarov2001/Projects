import random

digits = random.sample(range(10), 4)

secret_number = ''  # создаём пустую строку

for digit in digits:
    secret_number = secret_number + str(digit)

print("Секретное число:", secret_number)

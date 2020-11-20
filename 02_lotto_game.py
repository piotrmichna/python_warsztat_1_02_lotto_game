from random import randint


def generate_lotto_numbers():
    lotto_numbers = []
    while len(lotto_numbers) < 6:
        number = randint(1, 49)
        is_unique = True
        for i in lotto_numbers:
            if i == number:
                is_unique = False
                break

        if is_unique:
            lotto_numbers.append(number)

    print(lotto_numbers)

generate_lotto_numbers()


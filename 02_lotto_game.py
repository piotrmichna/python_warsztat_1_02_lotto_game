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

    return lotto_numbers

def get_player_numbers():
    player_numbers = []
    while len(player_numbers)<6:
        number=input(f"Podaj liczbę {len(player_numbers)+1}/6:")
        if not (number in player_numbers):
            player_numbers.append(number)
        else:
            print("Tą liczbę już wybrałeś")

get_player_numbers()
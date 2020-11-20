from random import randint


def generate_lotto_numbers():
    """the function generates 6 random numbers
    from range 1 to 49

    :return: list of 6 integer number
    """
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
    """the function gets the player's 6 numbers from range 1 to 49
    and checks for errors

    :return: list of integer number
    """
    player_numbers = []
    while len(player_numbers) < 6:
        if len(player_numbers):
            print(f'Twoje liczby to: {player_numbers}')
            input_str = "kolejną,"
        else:
            input_str = "liczbę"
        try:
            number = int(input(f"Podaj {input_str} {len(player_numbers) + 1} z 6:"))
        except ValueError:
            print('To nie jest liczba...')
            continue
        if number < 1 or number > 49:
            print('Wybierz liczbę z zakresu 1...49')
            continue
        if not (number in player_numbers):
            player_numbers.append(number)
        else:
            print("Tą liczbę już wybrałeś")

    return player_numbers


def lotto_game():
    """Main function LOTTO GAME"""

    print('-------|  LOTTO GAME  |-------')
    player_numbers = get_player_numbers()

    print('_----------LOSOWANIE----------_')
    lotto_numbers = generate_lotto_numbers()
    print(f'LOTTO -{lotto_numbers}-')
    print(f'GRACZ -{player_numbers}-')

    win_result = 0
    for n in player_numbers:
        if n in lotto_numbers:
            win_result += 1

    if win_result >= 3:
        print(f'\nŚwietnie! Trafiłeś {win_result}')
    else:
        print('\nMiałeś pecha, to nic.\nPróbuj dalej!')


if __name__ == '__main__':
    lotto_game()

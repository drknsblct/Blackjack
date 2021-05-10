from collections import Counter
from blackjack import Blackjack, games
from logo import logo
import re


def print_wins_and_losses(max_number):
    for _ in range(num_loops):
        Blackjack().play(max_number)

    counts = Counter(games)
    wins = counts.get('Wins')
    losses = counts.get('Losses')

    if wins is None:
        wins = 0
    elif losses is None:
        losses = 0

    print(f'Wins: {wins} | Losses: {losses}')
    print(f'Wins: {wins / num_loops * 100:.2f}% | Losses: {losses / num_loops * 100:.2f}%')

    # clear games list to run again with new card stand
    games.clear()
    print('\n\n')


if __name__ == '__main__':
    print(logo)
    try:
        while True:
            num_loops = int(input('How many times you want to play? Press Enter for 10: '))
            if num_loops > 0:
                break
    except ValueError:
        print('Entering default value (10) for times to play\n')
        num_loops = 10

    try:
        while True:
            max_number = int(input('Maximum card value to Stand? Press Enter for 17: '))
            if max_number > 0:
                break
    except ValueError:
        print('Entering default value (17) for maximum Stand\n')
        max_number = 17

    while True:
        answer = input('Want to raise card Stand with each loop? [(y)es/n(o)] ').lower().strip()
        # regular expression to catch y/yes or n/no only
        if re.search(r'^(y(es)?|n(o)?)$', answer):
            break
    print('\n\n')

    if answer == 'y':
        while max_number <= 21:
            print(f'Max Stand is currently: {max_number}')
            print_wins_and_losses(max_number)
            max_number += 1
    else:
        print_wins_and_losses(max_number)

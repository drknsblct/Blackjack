from collections import Counter
from blackjack import Blackjack, games
from logo import logo


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
        num_loops = int(input('How many times you want to play? Press Enter for 10: '))
    except ValueError:
        num_loops = 10

    try:
        max_number = int(input('Maximum card value to Stand? Press Enter for 17: '))
    except ValueError:
        max_number = 17

    answer = input('Want to raise card Stand with each loop? [y/n] ').lower().strip()
    print('\n\n')

    if answer == 'y':
        while max_number <= 21:
            print(f'Max Stand is currently: {max_number}')
            print_wins_and_losses(max_number)
            max_number += 1
    else:
        print_wins_and_losses(max_number)

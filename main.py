from collections import Counter
from blackjack import Blackjack, games

counts = Counter(games)
wins = counts.get('Wins')
losses = counts.get('Losses')


def raise_card_limit(max_number):
    global wins, losses

    for i in range(num_loops):
        Blackjack().play(max_number)


    # print(Counter(games))

    if wins is None:
        wins = 0
    elif losses is None:
        losses = 0

    print(f'Wins: {wins}')
    print(f'Wins: {(wins / num_loops) * 100:.2f}%')  # format decimal
    print('-----------')
    print(f'Losses: {losses}')
    print(f'Losses: {(losses / num_loops) * 100:.2f}%')  # format decimal

    games.clear()
    print('\n\n')


if __name__ == '__main__':
    try:
        num_loops = int(input('How many times you want to play? Press Enter for 10: '))
    except ValueError:
        num_loops = 10

    try:
        max_number = int(input('When player stops? Press Enter for 17: '))
    except ValueError:
        max_number = 17

    answer = input('Want to raise card limit with each loop? [y/n] ').lower().strip()

    if answer == 'y':
        while max_number <= 21:
            print(f'Max number is currently: {max_number}')
            raise_card_limit(max_number)
            max_number += 1
    else:
        print(f'Wins: {wins}')
        print(f'Wins: {(wins / num_loops) * 100:.2f}%')  # format decimal
        print('-----------')
        print(f'Losses: {losses}')
        print(f'Losses: {(losses / num_loops) * 100:.2f}%')  # format decimal

from collections import Counter

from blackjack import Blackjack, games

if __name__ == '__main__':
    try:
        num_loops = int(input('How many times you want to play? Press Enter for 10: '))
    except ValueError:
        num_loops = 10

    try:
        max_number = int(input('When player stops? Press Enter for 17: '))
    except ValueError:
        max_number = 17

    for i in range(num_loops):
        Blackjack().play(max_number)
    counts = Counter(games)
    print(Counter(games))

    print(f'Wins: {counts.get("Wins")}')
    print(f'Wins: {(counts.get("Wins") / num_loops) * 100:.2f}%')  # format decimal
    print('-----------')
    print(f'Losses: {counts.get("Losses")}')
    print(f'Losses: {(counts.get("Losses") / num_loops) * 100:.2f}%')  # format decimal

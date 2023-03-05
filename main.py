from ProgressBar import PBar
from Game import Game
import TrueRandom
import random


def main():
    attempts = int(1e7)
    attempts_str = "{:,}".format(attempts)

    seed = TrueRandom.randint()
    random.seed(seed)

    print(f"Computing {'{:,}'.format(attempts * 2)} games")
    progress, pbar = PBar.new(50, attempts * 2, refresh_rate=.5)

    wins_switch = 0
    wins_no_switch = 0
    for _ in range(attempts):
        wins_switch += Game(rint(), rint(), True).win()
        wins_no_switch += Game(rint(), rint(), False).win()
        progress.value += 2
    pbar.wait_complete()

    switch_str = "{:,}".format(wins_switch)
    no_switch_str = "{:,}".format(wins_no_switch)

    print(f"\nWins with switch\t\t{switch_str}/{attempts_str}\t{round(wins_switch * 100 / attempts, 2)}%")
    print(f"Wins without switch\t\t{no_switch_str}/{attempts_str}\t{round(wins_no_switch * 100 / attempts, 2)}%")


def rint():
    return random.randint(0, 2)


if __name__ == '__main__':
    main()

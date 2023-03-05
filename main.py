from dotenv import load_dotenv
from shadowbar import ProgressBar
import TrueRandom
import random


def main():
    load_dotenv()

    attempts = int(1e6)
    attempts_str = "{:,}".format(attempts)

    seed = TrueRandom.randint()
    random.seed(seed)

    print(f"Computing {'{:,}'.format(attempts * 2)} games")
    progress, pbar = ProgressBar.new(50, attempts * 2, refresh_rate=.5)

    wins_switch = 0
    wins_no_switch = 0
    for _ in range(attempts):
        wins_switch += won(True)
        wins_no_switch += won(False)
        progress.value += 2
    pbar.wait_complete()

    switch_str = "{:,}".format(wins_switch)
    no_switch_str = "{:,}".format(wins_no_switch)

    print(f"\nWins with switch\t\t{switch_str}/{attempts_str}\t{round(wins_switch * 100 / attempts, 2)}%")
    print(f"Wins without switch\t\t{no_switch_str}/{attempts_str}\t{round(wins_no_switch * 100 / attempts, 2)}%")


def rand():
    return random.randint(0, 2)


def won(switch):
    car, choice = rand(), rand()
    return (switch and car != choice) or (not switch and car == choice)


if __name__ == '__main__':
    main()

import numpy as np


def is_czy_es():
    p_kropki = 0.3

    for i in range(10):
        kropka = np.random.choice(2, 1, p=[1 - p_kropki, p_kropki])
        print(kropka)


def main():
    is_czy_es()


if __name__ == "__main__":
    main()

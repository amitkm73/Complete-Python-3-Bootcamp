# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from functions_ex import *


def main():
    # Use a breakpoint in the code line below to debug your script.
    print(has_33([1, 2, 3]))
    print(has_33([3]))
    print(has_33([1, 2, 3, 3]))
    print(has_33([3, 2, 3]))
    print(has_33([1, 3, 3]))

    print(paper_doll('a'))
    print(paper_doll('Hello'))
    print(paper_doll('Hi'))
    print(paper_doll('Mississippi'))

    print(blackjack(5, 6, 7))
    print(blackjack(9, 9, 9))
    print(blackjack(9, 9, 11))
    print(blackjack(9, 11, 11))

    print(summer_69([1, 3, 5]))
    print(summer_69([4, 5, 6, 7, 8, 9]))
    print(summer_69([2, 1, 6, 9, 11]))
    print(summer_69([2, 1, 6, 9, 1, 2, 6, 45, 67, 9, 100]))

    print(spy_games([1, 2, 3, 0, 4, 0, 6, 7, 8]))
    print(spy_games([1, 2, 4, 0, 0, 7, 5]))
    print(spy_games([1, 0, 2, 4, 0, 5, 7]))
    print(spy_games([1, 7, 2, 0, 4, 5, 0]))
    print(spy_games([0, 0, 7]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

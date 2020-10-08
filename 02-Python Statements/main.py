# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def main():
    # Use a breakpoint in the code line below to debug your script.
    secret = random.randint(1, 100)
    prev_guess = 0
    round_num = 0
    while True:
        try:
            current_guess = int(input('enter your guess: '))
        except ValueError:
            print('please enter a whole number')
            continue
        round_num += 1
        if current_guess == secret:
            print(f'CORRECT! secret was {secret}! it has taken you {round_num} rounds!')
            break
        if round_num == 1:
            if abs(secret-current_guess) <= 10:
                print('WARM!')
            else:
                print('COLD!')
        else:
            if abs(secret-current_guess) < abs(secret-prev_guess):
                print('WARMER!')
            elif abs(secret-current_guess) > abs(secret-prev_guess):
                print('COLDER')
            else:
                print('SAME DISTANCE')
        prev_guess = current_guess
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


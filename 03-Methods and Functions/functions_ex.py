def ex1():
    print('hi')
    return


def has_33(nums):
    """
    :param nums: list of ints
    :return: True if the array contains a 3 next to a 3 somewhere.
    """
    prev_number = 0
    for current_number in nums:
        if current_number == 3 and prev_number == 3:
            return True
        else:
            prev_number = current_number
    return False


def paper_doll(text):
    """
    :param text: string to stretch 3 times 
    :return: string where for every character in the original there are three characters
    """
    ext_str = ''
    for char in text:
        for i in range(0, 3):
            ext_str += char
    return ext_str


def blackjack(a, b, c):
    """
    :param a: card value - from 1 to 11
    :param b: card value - from 1 to 11
    :param c: card value - from 1 to 11
    :return: per blackjack game rules
    """
    if (a < 1) or (b < 1) or (c < 1):
        return 'Error'
    if (a > 11) or (b > 11) or (c > 11):
        return 'Error'
    card_sum = a + b + c
    if card_sum <= 21:
        return card_sum
    if a == 11 or b == 11 or c == 11:
        card_sum -= 10
    if card_sum > 21:
        return 'BUST'
    else:
        return card_sum


def summer_69(arr):
    """
    :param arr: array of integers
    :return: sum of the numbers in the array except sections of numbers starting with a 6 and extending to the next 9
    :return: 0 for no numbers
    """
    total = 0
    ignore = False
    for num in arr:
        if not ignore:
            total += num
        if num == 6:
            total -= 6
            ignore = True
        elif num == 9:
            ignore = False
    return total


def spy_games(nums):
    """
    :param nums: list of numbers
    :return: True if list contains 007 in order, False otherwise
    """
    temp_str = ''
    for number in nums:
        temp_str += str(number)
    return '007' in temp_str

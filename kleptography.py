import typing


def letter_to_number(char: str) -> int:
    """ Convert a letter to its corresponding number in 0-25 """
    number = ord(char) - 97
    return number


def number_to_letter(num: str) -> int:
    """ Convert a number to its corresponding letter in a-z """
    letter = chr(num + 97)
    return letter


def calculate_last_unknown_a(b: str, a: str, k: str, last_letters: str, n: int) -> typing.Tuple[str, str]:
    ''' Calculate the last unkown letter of a '''
    last = letter_to_number(b[-1]) - letter_to_number(last_letters[-1])
    last += 26 if last < 0 else 0
    last = number_to_letter(last)
    k += last
    a = last + a
    return k, a


def step_back_k(b: str, a: str, k: str, idx: int) -> typing.Tuple[str, str]:
    ''' Obtain the next unknown letter of k (moving backward) '''
    number = letter_to_number(b[-idx]) - letter_to_number(a[-idx])
    number += 26 if number < 0 else 0
    next = number_to_letter(number)
    k = next + k
    a = next + a
    return k, a


def create_a(b: str, last_letters: str, k: str, a: str, n: int):
    ''' Get plaintext '''
    k, a = calculate_last_unknown_a(b, a, k, last_letters, n=n)
    for idx in range(2, len(b) - n + 1):
        k, a = step_back_k(b, a, k, idx)
    return a


k = ""
n, m = list(map(int, input().rstrip().split()))
last_letters = str(input())
b = str(input())
a = last_letters

a = create_a(b=b, last_letters=last_letters, k=k, a=a, n=n)
print(a)

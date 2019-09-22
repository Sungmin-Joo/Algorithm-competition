from itertools import combinations

def solution(numbers):
    numbers = [*map(str,numbers)]
    numbers.sort(key = lambda x : x*3, reverse = True)
    return str(int(''.join(numbers)))
'''
시간초과
from itertools import permutations


def solution(numbers):
    numbers = list(map(str, numbers))
    tmp = list(map(''.join, permutations(numbers)))
    answer = max(tmp)
    return answer
'''
def solution(numbers):
    numbers = [ str(x) for x in numbers ]
    numbers.sort(key=lambda x: (x*4)[:4], reverse=True)
    answer = "".join(numbers) if numbers[0] != "0" else "0"
    return answer
'''
매우 크게 만들고, 네자리로 자른뒤 순차적으로 입힘

'''
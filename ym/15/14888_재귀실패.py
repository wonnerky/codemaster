import sys

n=int(sys.stdin.readline())#초기 숫자 개수

num_info= list(map(int,sys.stdin.readline().split())) #숫자들

symbol_info= list(map(int,sys.stdin.readline().split())) #연산자 정보
'''
index 0: +
index 1: -
index 2: *
index 3: //
'''
def symbol(symbol_info):

    symbol_total=[]

    if symbol_info[0] >=int(0):
        symbol_total.append('+'*symbol_info[0])
    if symbol_info[1] >=int(0):
        symbol_total.append('-'*symbol_info[1])
    if symbol_info[2] >=int(0):
        symbol_total.append('*'*symbol_info[1])
    if symbol_info[3] >=int(0):
        symbol_total.append('//'*symbol_info[1])

    symbol_len=len(symbol_total) #연산자 개수수

    return symbol_total, symbol_len

def all_calculate(symbol_total,num_info):

    for i in range(n):




    return


def calculate_max():

    max_num=max()

    return max_num

def calculate_min():

    min_num=min()

    return min_num
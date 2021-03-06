from itertools import permutations


def solution(numbers):
    # 소수 판별할 리스트 만들기
    num_list = []  # 전체 순열 넣어줄 리스트
    for i in range(1, len(numbers) + 1):
        test_list = permutations(numbers, i)
        for j in test_list:
            num_list.append(int("".join(j)))

    num_list = set(num_list)  # 중복과 0, 1 제외
    if 0 in num_list:
        num_list.remove(0)
    if 1 in num_list:
        num_list.remove(1)

    # 소수 판별
    answer = len(num_list)  # 모든 수가 소수라 가정하고 시작
    for i in num_list:
        if i != 2:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    answer -= 1
                    break

    return answer
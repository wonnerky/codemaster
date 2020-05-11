def solution(text):

    def compress(text, tok_len):
        words = [text[i:i + tok_len] for i in range(0, len(text), tok_len)]
        res = []
        cur_word = words[0]
        cur_cnt = 1
        for a, b in zip(words, words[1:] + ['']):
            if a == b:
                cur_cnt += 1
            else:
                res.append([cur_word, cur_cnt])
                cur_word = b
                cur_cnt = 1
        return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)
        # word length와 count의 lenght(str으로 취급) 을 모두 더한 값. words는 word를 1부터 나눈 집합

    # print([compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) +1))] + [len(text)])
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])
    # for 문을 1부터 [int(len(text)/2) +1](최대 길이의 절반까지 가능함)까지 문자열을 나눈다.
    # compress는 각 집합 값을 list로 반환한다. 아무것도 나누지 않은 text길이를 list에 더해서 min값을 찾는다.

s = "abdsafeadafebdfaerqfasfs"
print(solution(s))
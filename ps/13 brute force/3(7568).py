a = int(input())

w_list = []
h_list = []

for i in range(a):
    w, h = map(int, input().split())
    w_list.append(w)
    h_list.append(h)

wr_list = []
wh_list = []
rw = 1
rh = 1

for i in range(a):
    if w_list[i] == max(w_list):
        w_list[i] = rw
list = [[1,2,3,4,5],[10,11,12,13,14],[21,22,23,24,25]]

list_a = list[0]
list_b = list[1]
list_c = list[2]
list_d = list_a+list_b+list_c
list_e = []
list_e.append(list_d[0:3])
list_e.append(list_d[3:6])
list_e.append(list_d[6:9])
print(list_e)
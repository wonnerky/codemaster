import sys
number = int(sys.stdin.readline().strip())
i = 0
boundary = 1
while True:
    boundary += i*6
    if number <= boundary:
        print(i + 1)
        break
    i  = i + 1

# import sys
# n = int(sys.stdin.readline().strip())
# step = 1
# i = 0
# while True:
#     step += 6*i
#     if n <= step:
#         print(i + 1)
#         break
#     i += 1
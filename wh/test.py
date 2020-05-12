def rotate(key):
    return list(zip(*key[::-1]))


if __name__ == "__main__":
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]

    print(key)
    print(rotate(key))

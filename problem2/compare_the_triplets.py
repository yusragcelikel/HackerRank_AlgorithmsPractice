def compareTheScores(a, b):
    count_alice = 0
    count_bob = 0
    for i in range(3):
        if a[i] > b[i]:
            count_alice += 1
        elif b[i] > a[i]:
            count_bob += 1
    return [count_alice, count_bob]

if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    print(compareTheScores(a, b))
    # ---- or the following part instead 'print(compareTheScores(a, b))' -----
    # result = compareTheScores(a, b)
    # print(' '.join(map(str, result)))
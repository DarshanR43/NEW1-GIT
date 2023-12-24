if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    I = list((arr))
    if I[-2]!= I[-1]:
        print(I[-2])
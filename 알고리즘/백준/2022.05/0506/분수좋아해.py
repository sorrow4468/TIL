while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    print(f'{N//M} {N%M} / {M}')
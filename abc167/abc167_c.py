N, M, X = list(map(int, input().split()))
C = []
A = []
for _ in range(N):
    line = list(map(int, input().split()))
    if min(line) == 0:
        continue
    C.append(line[0])
    A.append(line[1:])
ans = 0

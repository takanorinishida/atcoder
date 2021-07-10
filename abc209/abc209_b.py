# AC
N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

cost = 0
for i in range(N):
    if i % 2 == 0:
        cost += A[i]
    else:
        cost += A[i] - 1

print(('Yes', 'No')[cost > X])

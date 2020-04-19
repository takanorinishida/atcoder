N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = N
for i in range(M):
    ans -= A[i]
print(max(-1, ans))

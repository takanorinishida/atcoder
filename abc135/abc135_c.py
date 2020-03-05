N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    dif = B[i] - A[i]
    if dif > 0:
        ans += A[i]
        ans += min(A[i + 1], dif)
        A[i + 1] = max(A[i + 1] - dif, 0)
    else:
        ans += B[i]
print(ans)

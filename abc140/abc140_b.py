N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
for i in range(N):
    ans += B[A[i]]
    if i < N - 1 and A[i + 1] == A[i] + 1:
        ans += C[A[i]]
print(ans)

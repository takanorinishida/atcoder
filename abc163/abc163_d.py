N, K = list(map(int, input().split()))
ans = 0
for k in range(K, N + 2):
    ans += - k ** 2 + (N + 1) * k + 1
print(ans % (10 ** 9 + 7))

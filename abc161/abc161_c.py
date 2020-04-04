N, K = list(map(int, input().split()))
ans1 = N % K
ans2 = abs(ans1 - K)
print(min(ans1, ans2))

K, X = map(int, input().split())
m = max(X - K + 1, -1000000)
M = min(X + K - 1, 1000000)
ans = [i for i in range(m, M + 1)]
print(' '.join(map(str, ans)))

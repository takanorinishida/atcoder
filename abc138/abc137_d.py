N, Q = map(int, input().split())
ans = [0 for _ in range(N)]
parent = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    parent[b].append(a)
for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    ans[p] += x


print(' '.join(map(str, ans)))

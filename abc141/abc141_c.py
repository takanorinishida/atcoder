N, K, Q = map(int, input().split())
p = [0 for _ in range(N)]
for i in range(Q):
    a = int(input()) - 1
    p[a] += 1
for i in range(N):
    print(('No', 'Yes')[p[i] > Q - K])

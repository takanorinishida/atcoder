N = int(input())
v = sorted(list(map(int, input().split())))
ans = 0
for i in range(N):
    if i == 0:
        ans += v[i]
        continue
    ans = (ans + v[i]) / 2
print(ans)

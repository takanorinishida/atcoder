import heapq

N, M = map(int, input().split())
a = list(map(int, input().split()))
for _ in range(M):
    m = heapq.nlargest(2, a)
    l = m[0] // 2
    ans -= m - l
    if ans == 0:
        break
    if len(a) > 1:
        a.remove(m)
        a.append(l)
print(ans)

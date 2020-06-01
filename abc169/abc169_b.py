N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
if A[-1] == 0:
    print(0)
    exit()
ans = 1
for i in range(N):
    ans *= A[i]
    if ans > 10 ** 18:
        ans = -1
        break
print(ans)

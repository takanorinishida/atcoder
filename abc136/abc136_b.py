N = int(input())
ans = 0
for i in range(len(str(N))):
    if i % 2 != 0:
        continue
    if i == len(str(N)) - 1:
        ans += N - 10 ** i + 1
    else:
        ans += 9 * 10 ** i
print(ans)
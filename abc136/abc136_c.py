N = int(input())
H = list(map(int, input().split()))
ans = 'Yes'
for i in range(1, N):
    j = N - i
    if not H[j - 1] > H[j]:
        continue
    elif H[j - 1] - H[j] == 1:
        H[j - 1] -= 1
        continue
    else:
        ans = 'No'
        break
print(ans)

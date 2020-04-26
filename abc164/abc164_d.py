S = input()
N = len(S)
ans = 0
for i in range(N - 3):
    j = i + 4
    while j <= N:
        if int(S[i: j]) % 2019 == 0:
            ans += 1
            j += 4
            continue
        j += 1
print(ans)

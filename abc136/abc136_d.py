# TLE
S = input()
N = len(S)
ans = [0 for _ in range(N)]
for i in range(N):
    print(i)
    j = 0
    if S[i] == 'R':
        while S[i + j] == 'R':
            j += 1
        if j % 2 == 0:
            ans[i + j] += 1
        else:
            ans[i + j - 1] += 1
    else:
        while S[i - j] == 'L':
            j -= 1
        if j % 2 == 0:
            ans[i - j] += 1
        else:
            ans[i - j + 1] += 1
print(' '.join(ans))

N = int(input())
ans = 0
S = {}
for i in range(N):
    s = ''.join(sorted(input()))
    if s not in S.keys():
        S[s] = 0
        continue
    S[s] += 1
    ans += S[s]
print(ans)

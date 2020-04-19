# My solution (TLE)
N = int(input())
S = input()
ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if (
                j - i == k - j
            ) or (
                S[i] == S[j] or S[j] == S[k] or S[i] == S[k]
            ):
                continue
            ans += 1
print(ans)

# Reference
# N = int(input())
# S = input()
# num_r, num_g, num_b = 0, 0, 0
# for s in S:
#     if s == 'R':
#         num_r += 1
#     elif s == 'G':
#         num_g += 1
#     else:
#         num_b += 1
# ans = num_r * num_g * num_b
# for i in range(N):
#     diff = 1

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
sumA = sum(A)
ans = ['Yes', 'No']
count = 0
for a in A:
    if not a < 1 / (4 * M) * sumA:
        count += 1
print(ans[count < M])

N = int(input())
A = list(map(int, input().split()))
Ans = [0] * N
for a in A:
    Ans[a - 1] += 1
for ans in Ans:
    print(ans)

N = int(input())
A = list(map(int, input().split()))
ans = sorted(range(N), key=lambda i: A[i])
ans = list(map(lambda x: str(x + 1), ans))
print(' '.join(ans))

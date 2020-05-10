A, B, C, K = list(map(int, input().split()))
if K <= A:
    print(K)
elif K <= A + B:
    print(A)
else:
    print(2 * A + B - K)

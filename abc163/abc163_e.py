N = int(input())
A = [a for a in enumerate(list(map(int, input().split())))]
A.sort(key=lambda x: x[1], reverse=True)
ans = 0
start = 0
end = N - 1
for i in range(N):
    d_start = abs(A[i][0] - start)
    d_end = abs(A[i][0] - end)
    if d_start > d_end:
        ans += A[i][1] * d_start
        start += 1
    elif d_start < d_end:
        ans += A[i][1] * d_end
        end -= 1
    else:
        ans += A[i][1] * d_end
        if not i < N - 1:
            continue
        _d_start = abs(A[i + 1][0] - start)
        _d_end = abs(A[i + 1][0] - end)
        if _d_start > _d_end:
            end -= 1
        else:
            start += 1
print(ans)

def gcd(m, n):
    while n:
        m, n = n, m % n
    return m

K = int(input())
ans = 0
for a in range(1, K + 1):
    for b in range(a, K + 1):
        for c in range(b, K + 1):
            _ans = gcd(gcd(a, b), c)
            if a == b and b == c:
                ans += _ans
            elif a == b or b == c:
                ans += 3 * _ans
            else:
                ans += 6 * _ans
print(ans)

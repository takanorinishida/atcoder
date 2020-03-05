A, B = map(int, input().split())
print((A + B) // 2 if abs(A - B) % 2 == 0 else 'IMPOSSIBLE')
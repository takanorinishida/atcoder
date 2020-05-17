import math

A, B, H, M = list(map(int, input().split()))
pi = 3.141592653589793
angle_M = M * pi / 30
angle_H = H * pi / 6 + angle_M / 12
angle = abs(angle_H - angle_M)
angle = min(angle, 2 * pi - angle)
print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(angle)))

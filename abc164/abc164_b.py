import math

A, B, C, D = list(map(int, input().split()))
tak = math.ceil(A / D)
aok = math.ceil(C / B)
print(('No', 'Yes')[tak - aok > -1])

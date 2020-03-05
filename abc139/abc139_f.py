import numpy as np


def dist(cood):
    cood = np.array(cood)
    cood = np.sum(cood, axis=0)
    return np.linalg.norm(cood)

N = int(input())
nw, ne, sw, se = [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]]
for _ in range(N):
    x, y = map(int, input().split())
    if x <= 0 and y >= 0:
        nw.append([x, y])
    if x >= 0 and y >= 0:
        ne.append([x, y])
    if x >= 0 and y <= 0:
        se.append([x, y])
    if x <= 0 and y <= 0:
        sw.append([x, y])
print(max([dist(nw), dist(ne), dist(sw), dist(se)]))

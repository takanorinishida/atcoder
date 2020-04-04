# Reference：https://atcoder.jp/contests/abc161/submissions/11545777

K = int(input())
table = [n + 1 for n in range(9)]
for i in table:
    if len(table) > K:
        break
    x = i % 10
    for j in range(max(0, x - 1), min(x + 2, 10)):
        table.append(i * 10 + j)
print(table[K - 1])

K = int(input())
S = input()
print((S, S[:K] + '...')[len(S) > K])

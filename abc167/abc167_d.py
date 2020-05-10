N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
visited = {'1': 0}
route = [1]
next_id = 0
count = 0
while count < K:
    count += 1
    if A[next_id] in visited.keys():
        route = route[visited[A[next_id]]:]
        K -= count
        break
    visited[A[next_id]] = count
    route.append(A[next_id])
    next_id = A[next_id] - 1
print(route[K % len(route)])

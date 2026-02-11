K, N = map(int, input().split())

# Please write your code here.
result = []

def dfs(depth):
    if depth == N:
        print(*result)
        return

    for i in range(1, K+1):
        result.append(i)
        dfs(depth+1)
        result.pop()

dfs(0)
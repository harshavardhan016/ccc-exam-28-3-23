

def dfs(node, visited, adj_list, traversal):
    visited[node] = True
    traversal.append(node)

    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, adj_list, traversal)


n, m = map(int, input().split())
adj_list = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

visited = [False] * (n+1)
traversal = []
for node in range(1, n+1):
    if not visited[node]:
        dfs(node, visited, adj_list, traversal)

traversal.sort(reverse=True)
for node in traversal:
    print(node)
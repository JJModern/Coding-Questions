import sys
sys.setrecursionlimit(10**8)
from collections import defaultdict


n = int(input())
comps = {'(': ')', '[': ']', '{': '}'}

nodes, map = input(), defaultdict(int)
for i, char in enumerate(nodes):
    map[i + 1] = char

graph = defaultdict(list)
for _ in range(n - 1):
    u, v = input().split()
    u, v = int(u), int(v)
    graph[u].append(v)
    graph[v].append(u)

paths = defaultdict(list)
def DFS(node):
    if len(path) > 6:
        paths[len(path)].append([path[0], path[1], path[2], path[-3], path[-2], path[-1]])
    else:
        paths[len(path)].append(path.copy())
    for neighbor in graph[node]:
        if neighbor not in seen:
            seen.add(neighbor)
            path.append(neighbor)
            DFS(neighbor)
    if path:
        path.pop()

for node in graph:
    seen = {node}
    path = [node]
    DFS(node)

DP = defaultdict(int)

for length in range(2, n + 1):
    if length == 2:
        for path in paths[length]:
            first, last = path[0], path[-1]
            if map[first] in comps and comps[map[first]] == map[last]:
                DP[(path[0], path[-1])] = 1
    else:
        for path in paths[length]:
            first, last = path[0], path[-1]
            if map[first] in comps and comps[map[first]] == map[last] and DP[(path[1], path[-2])]:
                DP[(path[0], path[-1])] = 1
            first, second = path[0], path[1]
            if map[first] in comps and comps[map[first]] == map[second] and DP[(path[2], path[-1])]:
                DP[(path[0], path[-1])] = 1
            second, last = path[-2], path[-1]
            if map[second] in comps and comps[map[second]] == map[last] and DP[(path[0], path[-3])]:
                DP[(path[0], path[-1])] = 1

res = 0
for element in DP:
    res += DP[element]

print(res)
from collections import deque

def bfs(graph:dict, source:str, target:str):
    visited = dict()
    visited[source] = None
    to_visit = deque([source])
    
    while to_visit:
        cur = to_visit.popleft()
        print(cur)

        if cur == target: break

        for neigh, weight in graph[cur]['edges']:
            
            if neigh in visited: continue
            visited[neigh] = (cur, weight)
            to_visit.append(neigh)

    path = [target]
    cur = target
    total_weight = 0
    while visited[cur]:
        next_node, weight = visited[cur]
        path.append(next_node)
        cur = next_node
        total_weight += weight

    return total_weight, list(reversed(path))
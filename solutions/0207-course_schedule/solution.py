from collections import defaultdict

def can_finish(numCourses, prerequisites):
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[b].append(a)

    # 0=unvisited 1=visiting 2=done
    state = [0] * numCourses

    def dfs(node):
        if state[node] == 1: return False
        if state[node] == 2: return True
        state[node] = 1
        for nb in graph[node]:
            if not dfs(nb): return False
        state[node] = 2
        return True

    return all(dfs(i) for i in range(numCourses))

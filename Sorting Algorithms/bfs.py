def bfs(graph, start):
    """
    return the set of all nodes that can be visited in the graph from start node
    """
    visited = set()
    queue = [start]
    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.add(current)
            queue.extend(graph[current] - visited)
    return visited

def bfs_path(graph, start, end):
    """
    return if there is a possible path from start node to end node in the graph
    """
    visited = set()
    queue = [start]
    while queue:
        current = queue.pop(0)
        if current not in visited:
            if current == end:
                return True
            visited.add(current)
            queue.extend(graph[current] - visited)
    return False

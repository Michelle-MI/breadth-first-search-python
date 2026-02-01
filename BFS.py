from collections import deque

def bfs(graph, start_node):
    
    # Performs Breadth-First Search and returns the traversal order.
    
    visited = set()
    queue = deque()
    traversal_order = []

    visited.add(start_node)
    queue.append(start_node)

    while queue:
        current_node = queue.popleft()
        traversal_order.append(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

result = bfs(graph, 'A')
print("BFS Traversal Order:", result)

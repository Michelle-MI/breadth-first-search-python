# Breadth-First Search (BFS) in Python

This project demonstrates a beginner-friendly implementation of the
**Breadth-First Search (BFS)** algorithm using Python.

BFS is a graph traversal algorithm that explores all neighboring nodes
before moving deeper into the graph.

---

## Features

- Graph represented using an adjacency list
- BFS traversal using a queue
- Returns traversal order as a list
- Prevents revisiting nodes using a set

---

## How BFS Works

1. Start from a selected node
2. Mark it as visited
3. Add it to a queue
4. While the queue is not empty:
   - Remove the first node
   - Visit all unvisited neighbors
   - Add them to the queue

---

## Example Graph

A -- B -- D
| |
C E
\ /
F
## How to Run the Project

1. Make sure Python is installed
2. Clone the repository or download the files
3. Run the program:

```bash
python BFS.py

## Expected Output
BFS Traversal Order: ['A', 'B', 'C', 'D', 'E', 'F']

## Future Improvements

Track distance from the start node

Return shortest path

Add user input for graph nodes

Compare BFS with DFS

Implement BFS in C or Java


# Author

Michelle Mueni

Beginner Computer Science student learning algorithms and Python.


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


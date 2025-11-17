import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    pq = []
    heapq.heappush(pq, (0, start, []))
    visited = set()
    while pq:
        cost, current, path = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            for step in path + [current]:
                print(step)
            print("Total steps:", len(path))
            return
        x, y = current
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and (nx, ny) not in visited:
                new_cost = len(path) + 1 + heuristic((nx, ny), goal)
                heapq.heappush(pq, (new_cost, (nx, ny), path + [current]))
    print("No path found")

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))
grid = []
print("Enter grid row by row (0 for free cell, 1 for obstacle):")
for _ in range(n):
    grid.append(list(map(int, input().split())))
sx, sy = map(int, input("Enter start position (row col): ").split())
gx, gy = map(int, input("Enter goal position (row col): ").split())
print("Optimal path using A* heuristic:")
astar(grid, (sx, sy), (gx, gy))
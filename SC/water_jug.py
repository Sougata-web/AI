# Function to perform DFS to solve the water jug problem
def water_jug_dfs(capacity1, capacity2, target):
    visited = set()
    path = []  

    def dfs(jug1, jug2):
        if (jug1, jug2) in visited:
            return False
        
        visited.add((jug1, jug2))

        path.append((jug1, jug2))

        if jug1 == target or jug2 == target:
            return True

        if dfs(capacity1, jug2):
            return True
        if dfs(jug1, capacity2):
            return True
        if dfs(0, jug2):
            return True
        if dfs(jug1, 0):
            return True
        if dfs(max(0, jug1 - (capacity2 - jug2)), min(capacity2, jug1 + jug2)):
            return True
        if dfs(min(capacity1, jug1 + jug2), max(0, jug2 - (capacity1 - jug1))):
            return True

        path.pop()
        return False
    dfs(0, 0)

    return path

capacity1 = 3  
capacity2 = 6  
target = 4 

solution = water_jug_dfs(capacity1, capacity2, target)

if solution:
    print("Solution steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")


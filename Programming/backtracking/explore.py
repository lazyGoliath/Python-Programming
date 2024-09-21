def knight_neighbours(coord, n, m):
    """Returns neighboring coordinates within grid boundaries."""
    x, y = coord
    neighbours = []
    knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    
    # Check all possible knight moves
    for dx, dy in knight_moves:
        nx, ny = x + dx, y + dy
        
        # Check if neighbour is within grid
        if 0 <= nx < n and 0 <= ny < m:
            neighbours.append((nx, ny))
            
    return neighbours


def explore(sx, sy, tx, ty, n, m):
    """
    Performs BFS from source (sx, sy) and returns 
    the minimum number of moves to reach target (tx, ty).
    
    Movement is restricted to knight moves in chess.
    """
    # Initialize visited matrix
    marked = [[False for _ in range(m)] for _ in range(n)]
    marked[sx][sy] = True
    
    # Initialize queue with source and move count
    queue = [(sx, sy, 0)]

    while queue:
        ax, ay, moves = queue.pop(0)
        
        # Check if target reached
        if (ax, ay) == (tx, ty):
            return moves
        
        # Explore neighbours
        for nx, ny in knight_neighbours((ax, ay), n, m):
            if not marked[nx][ny]:
                marked[nx][ny] = True
                queue.append((nx, ny, moves + 1))

    # Target unreachable
    return -1


# Test the function
n = input("enter grid row size")  # Grid size
m = input("enter grid column size")
sx = 0  # Source x
sy = 0  # Source y
tx = 1  # Target x
ty = 1  # Target y

moves = explore(sx, sy, tx, ty, n, m)
if moves != -1:
    print(f"Minimum moves to reach ({tx}, {ty}) from ({sx}, {sy}): {moves}")
else:
    print(f"Target ({tx}, {ty}) unreachable from ({sx}, {sy})")


"""
The `explore` function uses BFS to traverse the grid and marks visited cells.
It keeps track of the move count for each cell.
Once the target cell is reached, it returns the move count.
If the target cell is unreachable, it returns -1.


You can adjust the grid size `(n, m)` and the source/target coordinates 
`(sx, sy)` and `(tx, ty)` to test different scenarios.
"""
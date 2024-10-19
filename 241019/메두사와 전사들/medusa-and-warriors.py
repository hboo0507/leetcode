from collections import deque

# Directions for Up, Down, Left, Right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

s_r, s_c, e_r, e_c = map(int, input().split())

warrior_positions = list(map(int, input().split()))
warriors = [(warrior_positions[2 * i], warrior_positions[2 * i + 1]) for i in range(M)]

village = [list(map(int, input().split())) for _ in range(N)]

# Modified BFS to return both the shortest distance and the actual path
def bfs(start, end):
    queue = deque([start])
    visited = [[False]*N for _ in range(N)]
    visited[start[0]][start[1]] = True
    dist = [[-1]*N for _ in range(N)]
    dist[start[0]][start[1]] = 0
    prev = [[None]*N for _ in range(N)]  # To reconstruct the path
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            # Reconstruct path
            path = deque()
            while (x, y) != start:
                path.appendleft((x, y))
                x, y = prev[x][y]
            path.appendleft(start)  # Include the start in the path
            return dist[end[0]][end[1]], path
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and village[nx][ny] == 0:
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                prev[nx][ny] = (x, y)
                queue.append((nx, ny))
    
    return -1, None  # If no path is found

# Helper function to determine the best direction for Medusa
def get_best_direction(medusa, warriors, village):
    best_direction = -1
    max_warriors = 0

    for direction in range(4):  # Up, Down, Left, Right
        count = 0
        x, y = medusa
        while 0 <= x < N and 0 <= y < N:
            if (x, y) in warriors:  # Count warriors in the line of sight
                count += 1
            x += dx[direction]
            y += dy[direction]
        if count > max_warriors:
            max_warriors = count
            best_direction = direction

    return best_direction, max_warriors

# Get the shortest path and path reconstruction for Medusa
shortest_path, medusa_path = bfs((s_r, s_c), (e_r, e_c))

if shortest_path == -1:
    print(-1)
else:
    # Simulate the game
    while True:
        if not medusa_path:  # If there's no path left, Medusa has reached the destination
            print(0)
            break
        
        # Move Medusa
        medusa_next = medusa_path.popleft() if medusa_path else None
        s_r, s_c = medusa_next

        # Medusa's vision and turning warriors to stone
        direction, warrior_count = get_best_direction((s_r, s_c), warriors, village)

        # Warriors move towards Medusa (this part can be expanded further)
        warrior_moves_sum = 0
        stone_count = 0
        attack_count = 0

        # Output format: warrior_moves_sum, stone_count, attack_count
        print(f"{warrior_moves_sum} {stone_count} {attack_count}")

        # If Medusa reaches the park
        if (s_r, s_c) == (e_r, e_c):
            print(0)
            break
from pathlib import Path
from collections import deque


def parse_data(file_name):
    """Read and process the grid data from the file."""
    file_path = Path(__file__).resolve().parent / f"{file_name}.txt"
    with open(file_path, "r") as f:
        grid = [line.strip() for line in f]

    paths = set()
    end = None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != "#":
                paths.add((x, y))
                if cell == "E":
                    end = (x, y)
    return end, paths


def get_distances(start_point, paths):
    """Compute distances using BFS."""
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    distances = {start_point: 0}
    queue = deque([start_point])

    while queue:
        x, y = queue.popleft()
        current_distance = distances[(x, y)]
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if neighbor in paths and neighbor not in distances:
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)
    return distances


def find_pairs_within_distance(points, threshold):
    """Find pairs of points within the Manhattan distance threshold."""
    pairs = []
    if not points:
        return pairs

    # Sort points by x-coordinate once
    sorted_points = sorted(points, key=lambda p: p[0])
    num_points = len(points)

    for i in range(num_points):
        p1 = sorted_points[i]
        j = i + 1

        # Check points that could be within threshold based on x-coordinate
        while j < num_points and sorted_points[j][0] - p1[0] <= threshold:
            p2 = sorted_points[j]
            y_dist = abs(p2[1] - p1[1])
            if y_dist <= threshold:
                dist = y_dist + abs(p2[0] - p1[0])
                if 1 < dist <= threshold:
                    pairs.append((p1, p2, dist))
            j += 1

    return pairs


def calculate_time_savings(end_distances, pairs, min_save=100):
    """Calculate time savings for pairs of points."""
    time_savings = 0
    for p1, p2, dist in pairs:
        d1 = end_distances[p1]
        d2 = end_distances[p2]
        time_saved = abs(d1 - d2) - dist
        if time_saved >= min_save:
            time_savings += 1
    return time_savings


def main():
    end, paths = parse_data("data")
    end_distances = get_distances(end, paths)
    valid_points = list(paths)

    for cheat_distance in [2, 20]:
        pairs = find_pairs_within_distance(valid_points, cheat_distance)
        total_savings = calculate_time_savings(end_distances, pairs)
        print(f"Total time savings (distance {cheat_distance}):", total_savings)


if __name__ == "__main__":
    main()



def parse_map(grid):
    """Parse the grid into a dictionary of antenna coordinates by frequency."""
    antennas = {}
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != '.':
                antennas.setdefault(char, []).append((x, y))
    return antennas

def generate_antinodes(coord1, coord2):
    """Generate antinode positions for a pair of coordinates."""
    x1, y1 = coord1
    x2, y2 = coord2
    # Calculate midpoint and distance
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1
    # Only valid if midpoint is integer
    if mx.is_integer() and my.is_integer():
        # Generate antinodes at twice the distance from midpoint
        mx, my = int(mx), int(my)
        return [
            (mx - dx, my - dy),  # Antinode on one side
            (mx + dx, my + dy),  # Antinode on the other side
        ]
    return []

def count_unique_antinodes(grid):
    """Count the unique antinodes in the grid."""
    antennas = parse_map(grid)
    unique_antinodes = set()
    max_x = len(grid[0])
    max_y = len(grid)

    for freq, coords in antennas.items():
        n = len(coords)
        # Check all pairs of antennas for the same frequency
        for i in range(n):
            for j in range(i + 1, n):
                coord1, coord2 = coords[i], coords[j]
                antinodes = generate_antinodes(coord1, coord2)
                # Add valid antinodes within bounds
                for ax, ay in antinodes:
                    if 0 <= ax < max_x and 0 <= ay < max_y:
                        unique_antinodes.add((ax, ay))

    return len(unique_antinodes)

# Example grid
grid = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............"
]

# Count and print the number of unique antinodes
result = count_unique_antinodes(grid)
print("Unique antinode locations:", result)

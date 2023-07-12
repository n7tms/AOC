def calculate_total_calories(data):
    elves = data.split('\n\n')  # Split data into separate Elves' inventories

    max_calories = 0
    for elf in elves:
        items = elf.split('\n')  # Split each Elf's inventory into separate items
        total_calories = sum(map(int, items))  # Calculate the total Calories for the current Elf

        if total_calories > max_calories:
            max_calories = total_calories

    return max_calories

# Example input
# IN_FILE = "./inputs/202201.sample.txt"

def parse():
    """Parse input."""
#    return [int(line) for line in puzzle_input.split("\n\n")]
#    return [line for line in puzzle_input.split("\n\n")]
    with open("./inputs/202201.txt") as fp:
        return fp.read().strip()


result = calculate_total_calories(parse())
print("The Elf carrying the most Calories is carrying:", result, "Calories.")

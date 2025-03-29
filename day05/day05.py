from collections import defaultdict, deque
from typing import Tuple


def read_file() -> Tuple[list, list]:
    with open("input.txt") as fp:
        line = fp.readline()
        rules = []
        while line != "\n":
            line = line.rstrip()
            a, b = line.split("|")
            rules.append((int(a), int(b)))
            line = fp.readline()
        line = fp.readline()
        updates = []
        while line:
            line = line.rstrip()
            line = [int(x) for x in line.split(",")]
            updates.append(line)
            line = fp.readline()
        return rules, updates


def is_update_ordered(update: list, rules:list) -> bool:
    # Create a dictionary to store the index of each page in the update
    page_index = {page: i for i, page in enumerate(update)}

    # Check each rule against the order in the update
    for a, b in rules:
        if a in page_index and b in page_index:
            if page_index[a] > page_index[b]:
                return False
    return True


def topological_sort(nodes, edges):
    """
    Perform topological sort on a graph represented by nodes and edges.
    Returns a sorted list of nodes.
    """
    # Build a graph and in-degree counts
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for a, b in edges:
        graph[a].append(b)
        in_degree[b] += 1
        in_degree[a]  # Ensure all nodes are in in_degree

    # Collect all nodes with in-degree 0
    queue = deque([node for node in nodes if in_degree[node] == 0])
    sorted_nodes = []

    while queue:
        current = queue.popleft()
        sorted_nodes.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_nodes


def reorder_update(update: list, rules: list):
    # Filter the rules to only include pages in the current update
    relevant_rules = [(a, b) for a, b in rules if a in update and b in update]

    # Perform topological sort to reorder the update
    sorted_update = topological_sort(update, relevant_rules)
    return sorted_update


def part1(rules: list, updates: list) -> int:
    correctly_ordered_updates = []
    middle_sum = 0

    for update in updates:
        if is_update_ordered(update, rules):
            correctly_ordered_updates.append(update)
            middle_page = update[len(update) // 2]  # Find the middle page
            middle_sum += middle_page
    return middle_sum


def part2(rules: list, updates: list) -> int:
    incorrectly_ordered_updates = []
    middle_sum = 0

    for update in updates:
        if not is_update_ordered(update, rules):
            incorrectly_ordered_updates.append(update)
            corrected_update = reorder_update(update, rules)
            middle_page = corrected_update[len(corrected_update) // 2]  # Find the middle page
            middle_sum += middle_page

    return middle_sum


if __name__ == "__main__":
    rules, updates = read_file()
    print(f"Part 1: {part1(rules, updates)}")
    print(f"Part 2: {part2(rules, updates)}")

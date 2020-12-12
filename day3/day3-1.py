# counting all the trees you would encounter for the slope right 3, down 1
# map loops, so len(line) == line[0]
# continue until reach the bottom of the map
# in map # is tree, . is empty
def main():
    test_map = []
    trees_encountered = 0

    with open("day3input.txt") as map_input:
        for line in map_input:
            test_map.append(line)

    trees_encountered = count_trees_in_path(test_map)

    print("trees encountered: ", trees_encountered)


def count_trees_in_path(test_map):
    tree_count = 0
    map_width = len(test_map[0]) - 1
    horizontal_position = 0

    for vertical_position in range(len(test_map)):
        if (test_map[vertical_position][horizontal_position]) == '#':
            tree_count += 1

        if horizontal_position + 3 < map_width:
            horizontal_position += 3
        else:
            horizontal_position = horizontal_position + 3 - map_width

    return tree_count


if __name__ == "__main__":
    main()

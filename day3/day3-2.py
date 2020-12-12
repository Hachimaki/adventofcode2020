# same as last problem
# need to check 1:1, 1:3, 1:5, 1:7, 2:1 - multiply results together
# should be able to do it all at the same time
def main():
    test_map = []

    with open("day3input.txt") as map_input:
        for line in map_input:
            test_map.append(line)

    print("trees encountered: ", count_trees_in_path(test_map))


def count_trees_in_path(test_map):
    tree_count_1_to_1 = 0
    horizontal_position_1_to_1 = 0
    tree_count_1_to_3 = 0
    horizontal_position_1_to_3 = 0
    tree_count_1_to_5 = 0
    horizontal_position_1_to_5 = 0
    tree_count_1_to_7 = 0
    horizontal_position_1_to_7 = 0
    tree_count_2_to_1 = 0
    horizontal_position_2_to_1 = 0

    map_width = len(test_map[0]) - 1

    for vertical_position in range(len(test_map)):
        if (test_map[vertical_position][horizontal_position_1_to_1]) == '#':
            tree_count_1_to_1 += 1
        if (test_map[vertical_position][horizontal_position_1_to_3]) == '#':
            tree_count_1_to_3 += 1
        if (test_map[vertical_position][horizontal_position_1_to_5]) == '#':
            tree_count_1_to_5 += 1
        if (test_map[vertical_position][horizontal_position_1_to_7]) == '#':
            tree_count_1_to_7 += 1
        if vertical_position % 2 == 0 and (test_map[vertical_position][horizontal_position_2_to_1]) == '#':
            tree_count_2_to_1 += 1

        if horizontal_position_1_to_1 + 1 < map_width:
            horizontal_position_1_to_1 += 1
        else:
            horizontal_position_1_to_1 = horizontal_position_1_to_1 + 1 - map_width

        if horizontal_position_1_to_3 + 3 < map_width:
            horizontal_position_1_to_3 += 3
        else:
            horizontal_position_1_to_3 = horizontal_position_1_to_3 + 3 - map_width

        if horizontal_position_1_to_5 + 5 < map_width:
            horizontal_position_1_to_5 += 5
        else:
            horizontal_position_1_to_5 = horizontal_position_1_to_5 + 5 - map_width

        if horizontal_position_1_to_7 + 7 < map_width:
            horizontal_position_1_to_7 += 7
        else:
            horizontal_position_1_to_7 = horizontal_position_1_to_7 + 7 - map_width

        if vertical_position % 2 == 0 and horizontal_position_2_to_1 + 1 < map_width:
            horizontal_position_2_to_1 += 1
        elif vertical_position % 2 == 0 and horizontal_position_2_to_1 + 1 >= map_width:
            horizontal_position_2_to_1 = horizontal_position_2_to_1 + 1 - map_width

    return tree_count_1_to_1 * tree_count_1_to_3 * tree_count_1_to_5 * tree_count_1_to_7 * tree_count_2_to_1


if __name__ == "__main__":
    main()

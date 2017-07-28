# West-coast map
STATES_MAP = {
    'WA': ['ID', 'OR'],
    'OR': ['WA', 'ID', 'NV', 'CA'],
    'CA': ['OR', 'NV', 'AZ'],
    'ID': ['WA', 'OR', 'NV', 'MT', 'WY', 'UT'],
    'NV': ['OR', 'ID', 'CA', 'AZ', 'UT'],
    'AZ': ['CA', 'NV', 'UT'],
    'UT': ['ID', 'NV', 'AZ', 'WY'],
    'WY': ['MT', 'ID', 'UT'],
    'MT': ['ID', 'WY']
}

STATES_COLORS = ['red', 'blue', 'orange', 'purple']

PETERSEN_MAP = {
    1: [2, 3, 4],
    2: [7, 8],
    3: [1, 4, 9],
    4: [5, 8],
    5: [4, 6, 7],
    6: [1, 5, 10],
    7: [2, 5, 9],
    8: [2, 4, 10],
    9: [3, 7, 10],
    10: [6, 8, 9]
}

# Non-greedy takes 3 colors
PETERSEN_COLORS = ['red', 'blue', 'green', 'yellow']

def partioned_graph(adjacency_map, colors):
    partitions = {}
    for color in colors:
        partitions[color] = []

    for node, adjacents in adjacency_map.items():
        for color, nodes in partitions.items():
            invalid_color = False
            for adjacent in adjacents:
                if adjacent in nodes:
                    invalid_color = True
                    break
            if not invalid_color:
                partitions[color].append(node)
                break

    return partitions



print(partioned_graph(STATES_MAP, STATES_COLORS))

print(partioned_graph(PETERSEN_MAP, PETERSEN_COLORS))

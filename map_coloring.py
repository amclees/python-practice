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



print(partioned_graph(STATES_MAP, COLORS))

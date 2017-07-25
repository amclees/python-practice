# West-coast map
ADJACENCY_MAP = {
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

COLORS = ['red', 'blue', 'orange', 'purple']

partitions = {}
for color in COLORS:
    partitions[color] = []

for node, adjacents in ADJACENCY_MAP.items():
    for color, nodes in partitions.items():
        invalid_color = False
        for adjacent in adjacents:
            if adjacent in nodes:
                invalid_color = True
                break
        if not invalid_color:
            partitions[color].append(node)
            break

print(partitions)

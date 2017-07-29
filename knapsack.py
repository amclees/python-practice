class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __str__(self):
        return str(self.value) + ' value - ' + str(self.weight) + ' weight'

    def __repr__(self):
        return str(self)

def best_knapsack(knapsack_maximum, items):
    sorted_items = sorted(items, key=lambda item: item.value / item.weight)

    knapsack = []
    knapsack_weight = 0
    while sorted_items:
        item = sorted_items.pop()
        while knapsack_weight + item.weight <= knapsack_maximum:
            knapsack.append(item)
            knapsack_weight += item.weight

    return knapsack

KNAPSACK_MAXIMUM = 15
ITEMS = [
    Item(4, 12),
    Item(2, 2),
    Item(2, 1),
    Item(10, 4),
    Item(1, 1)
]

print(best_knapsack(KNAPSACK_MAXIMUM, ITEMS))

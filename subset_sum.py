# Only works on certain arrays

def has_zero_subset_forward(array):
    out_numbers = []
    in_numbers = []
    in_sum = 0
    for number in array:
        if in_sum + number == 0:
            return True
        total_popped = 0
        while in_numbers:
            popped = in_numbers.pop()
            out_numbers.append(popped)
            in_sum -= popped
            total_popped += popped
            if in_sum + number == 0:
                return True
        in_numbers = out_numbers
        out_numbers = []
        in_numbers.append(number)
        in_sum = number + total_popped
    return False

def has_zero_subset(array):
    return has_zero_subset_forward(array) or has_zero_subset_forward(reversed(array))


print(has_zero_subset([5, 4, 2, 4, 5, -1, -1, -1, -1, -1, 5, -6, 2]))

print(has_zero_subset([-7, -3, -2, 5, 8]))

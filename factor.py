import sys

composite = int(sys.argv[1])

divisor = 2
factors = []
while composite > 1:
    if composite % divisor == 0:
        composite /= divisor
        factors.append(divisor)
        divisor = 2
    else:
        divisor += 1

print(factors)

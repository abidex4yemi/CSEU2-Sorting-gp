# O(1) space complexity

# No matter how big n gets the space used will remain the same


def o_1_space(n):
    total = 0
    for i in range(n):
        total += i
    return total


def o_n_space(n):
    sums = []

    for num in range(n):
        sums.append(num)
    return sums

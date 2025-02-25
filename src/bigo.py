# O(c) / o(1)
def constant_algo(items):
    result = items[0] * items[0]
    print(result)


constant_algo([4, 5, 6, 8])

# O(n)


def linear_algo(items):
    for item in items:
        print(item)


linear_algo([4, 5, 6, 8])

# What is the big O of this ??

# O(n)


def linear_algo_2(items):
    for item in items:
        print(item)

    for item in items:
        print(item)


linear_algo_2([4, 5, 6, 8])


# O(n^2)
def quadratic_algo(items):
    for item in items:
        for item2 in items:
            print(item, ' ', item2)


quadratic_algo([4, 5, 6, 8])

# chalenge. What is the complexity of this algorithm?


def complex_algo(items):

    for _ in range(5):
        print("Python is awesome")

    for item in items:
        print(item)

    for item in items:
        print(item)

    print("Big O")
    print("Big O")
    print("Big O")


complex_algo([4, 5, 6, 8])


def fact(n):
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product


def fact_r(n):
    if n == 0:
        return 1

    return n * fact_r(n - 1)


print(fact_r(5))

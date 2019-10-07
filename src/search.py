
# basic linear search
import math


def search_phone_book(phone_book, target):
    for name in phone_book:
        if name == target:
            return 1

    return -1


# print(search_phone_book(["Yemi", "Jane", "Shola"], "Yemi"))


def search_phone_book_two(arr, target):
    high = len(arr) - 1
    low = 0

    while low <= low:
        middle = int(math.floor((high + low)) / 2)

        if target < arr[middle]:
            high = middle - 1
        elif target > arr[middle]:
            low = middle + 1
        else:
            return middle

    return -1


print(search_phone_book_two(list(range(50)), 100))

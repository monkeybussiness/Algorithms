import random


def fill_random_numbers():
    nums = [x for x in range(1, 10000)]
    numbers = []
    for i in range(10):
        numbers.append(random.choice(nums))
    return numbers


def find_smallest(arr: list):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: list) -> list:
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


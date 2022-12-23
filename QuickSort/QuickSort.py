def quick_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

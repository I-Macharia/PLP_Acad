import random


def randomized_quicksort(arr):  # type: ignore
    """Sort an array using the randomized quicksort algorithm"""
    if len(arr) <= 1: # type: ignore
        return arr # type: ignore
    pivot = random.choice(arr)  # type: ignore
    less = [x for x in arr if x < pivot]  # type: ignore
    equal = [x for x in arr if x == pivot] # type: ignore
    greater = [x for x in arr if x> pivot] # type: ignore
    return randomized_quicksort(less) + equal + randomized_quicksort(greater) # type: ignore

# Generate a random unsorted list
unsorted_array = [random.randint(1, 100) for _ in range(10)]
print("Unsorted", unsorted_array)
print("Sorted", randomized_quicksort(unsorted_array))
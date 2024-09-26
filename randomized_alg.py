import random

def randomized_quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    # Randomly select a pivot
    pivot = random.choice(arr)

    # Partitioning the array into low and high
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = arr.count(pivot)

    if k < len(low):
        return randomized_quickselect(low, k)
    elif k < len(low) + pivot_count:
        return pivot  # k is in the pivot
    else:
        return randomized_quickselect(high, k - len(low) - pivot_count)

# Example usage
arr = [3, 1, 2, 5, 4]
k = 2
print(randomized_quickselect(arr, k))  # Output: 3 (the 3rd smallest element)

def median_of_medians(arr, k):
    if len(arr) < 10:
        return sorted(arr)[k]

    # Divide arr into subarrays of size 5
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]

    # Recursive call to find the median of the medians
    pivot = median_of_medians(medians, len(medians) // 2)

    # Partitioning step
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = arr.count(pivot)

    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + pivot_count:
        return pivot  # k is in the pivot
    else:
        return median_of_medians(high, k - len(low) - pivot_count)

# Example usage
arr = [3, 1, 2, 5, 4]
k = 2
print(median_of_medians(arr, k))  # Output: 3 (the 3rd smallest element)
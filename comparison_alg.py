from deterministic_alg import median_of_medians
from randomized_alg import randomized_quickselect
import time
import random

sizes = [10, 100, 1000, 5000, 10000]
for size in sizes:
    arr = random.sample(range(1, size * 10), size)
    
    # Testing Median of Medians
    start = time.time()
    median_of_medians(arr, size // 2)
    print(f'Median of Medians for size {size}: {time.time() - start:.6f} seconds')
    
    # Testing Randomized Quickselect
    start = time.time()
    randomized_quickselect(arr, size // 2)
    print(f'Randomized Quickselect for size {size}: {time.time() - start:.6f} seconds')


<div align="center">
  <h3 align="center">MSCS532 Assignment 6</h3>
</div>

<!-- CLONING THE REPOSITORY -->
## Cloning the Repository

To get a local copy of this repository, use the following commands:
```sh
# Clone the repository
git clone https://github.com/abhattarai28547/MSCS532_Assignment6.git

# Navigate into the project directory
cd MSCS532_Assignment6
```
<!-- Running the code-->
### Selection Algorithms

To test the ** Median of Medians ** implementation, execute:
```sh
python deterministic_alg.py
```
This will run the Median of Medians algorithm on a sample array and output the 𝑘th smallest element.

To test the ** Randomized Quickselect ** implementation, execute:
```sh
python randomized_alg.py
```

This will run the Randomized Quickselect algorithm on a sample array and output the 𝑘th smallest element.


### Empirical Analysis

To compare the performance of **Randomized Quickselect** with **Deterministic Quickselect**, execute:
```sh
python comparison_alg.py
```
This script compares the running times of both algorithms on different array sizes and distributions, displaying the results for analysis.

### Elementary Data Structures

To test all ** data structures**(Dynamic Array, Stack, Queue, and Linked List) implementation, run:
```sh
python data_structures.py
```
This script will demonstrate basic operations for each data structure, including insertion, deletion, and traversal.

<!-- CUSTOMIZATION -->
Customization
You can modify the hardcoded elements, such as arrays in the implementations, directly within their respective Python files:

`randomized_alg.py`: Adjust the array and 𝑘 to explore performance variations.

`deterministic_alg.py`: Edit the sample array and the value of 𝑘 inside the script to test different scenarios.

`comparison_alg.py`: Change array sizes and distributions to see how each algorithm performs under different conditions.

`data_structures.py`: Modify the operations and input data for the dynamic array, stack, queue, and linked list as needed for your testing.

 <!-- SUMMARY OF FINDINGS -->

 
### Summary of Findings
<div>  
  <li>Randomized Quickselect: This algorithm exhibited expected \(O(n)\) performance but could degrade to \(O(n^2)\) in rare cases. Empirical tests showed faster execution times in average scenarios compared to their deterministic counterparts.</li>
  
  <li>Deterministic Quickselect: This implementation consistently achieved \(O(n)\) time complexity in the worst case, demonstrating reliability for finding the \(k^{th}\) smallest element even with diverse input distributions.</li>
  
  <li>Data Structures: The combined implementation of the dynamic array, stack, queue, and singly linked list showcased efficient operations. The dynamic array allowed for efficient insertion and access, while the stack and queue provided \(O(1)\) operations. The linked list allowed for efficient insertions but required \(O(n)\) time for deletions and traversal.</li>
</div>

### Instructions:
<ol>
  <li>
    Clone the Repository: Use the provided Git commands to clone the repository and navigate into the project directory.
  </li>
  <li>
    Run Scripts: Execute the Python scripts using the provided commands.
  </li>
  <li>
    Customize: Modify the hardcoded elements in the Python files as needed for different testing scenarios.
  </li>
  <li>
    Review Findings: Refer to the summary of findings to understand the performance characteristics observed during the implementation and testing.
  </li>
</ol>

This `README.md` now includes detailed instructions for running the implementations, customizing them, and a summary of the findings.

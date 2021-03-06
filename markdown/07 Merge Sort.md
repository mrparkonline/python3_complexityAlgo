# Merge Sort
---

A comparison-based algorithm that sorts a given dataset. 

It is classified as a **“divide and conquer”** algorithm

There are 2 approaches to implementing a merge sort:
1. Top-Down Implementation
2. Bottom-Up Implementation

**Merge Sort Demonstration:**

[Source](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

<img src='./src/merge.gif' />

**Complexity of Merge Sort:**

- $O(n log n)$ Worst Case Performance
- $O(n log n)$ Average Case Performance
- $O(n log n)$ Best Case Performance

**Merge Sort Algorithm:**
```
-- Let A be an unsorted list, n represent size of A

function: divider(A)
    Create two empty lists called Left and Right
    
    Get Midpoint at n/2 - 1, 
        - all values before and include the midpoint is Left list
        - all values after midpoint is Right list
    
    Update Left to divider(Left) ... recursive call
    Update Right to divider(Right) ... recursive call
    
    return merge(Left, Right)

-- Let X and Y be sorted List called from divider()

function: merge(X, Y)
    Create empty list called Sorted
    
    While both x and y are not empty
        if X and Y are both non empty
            compare X[0] and Y[0]
                add the smaller value to Sorted
                removed the respective
    if X is empty and Y is not empty
        add all Y values to Sorted
    
    if Y is empty and X is not empty
        add all X values to Sorted
    
    return Sorted
```

**Python Implementation:**


```python
# Recursive Merge Sort Python Implementation
# Top Down Approach


def mergeSort(array):
    if len(array) <= 1:
        return array
    # end of base case

    left = [] # Division of array : left half
    right = [] # Divsion of array : right half

    for i in range(len(array)):
        if i < (len(array) // 2):
            left.append(array[i])
        else:
            right.append(array[i])
    # end of division

    # recursive mergeSort of left and right
    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)
# end of mergeSort()

def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    # end of handling left and right

    while left:
        result.append(left[0])
        left = left[1:]

    while right:
        result.append(right[0])
        right = right[1:]

    return result
# end of merge()

test = [6, 5, 3, 1, 8, 7, 3, 4]

sorted_test = mergeSort(test) # creates a new sorted list
print('Sorted:', sorted_test)
```

    Sorted: [1, 3, 3, 4, 5, 6, 7, 8]



```python

```

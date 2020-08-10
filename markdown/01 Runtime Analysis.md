# Runtime Analysis
---

## Simple Runtime Calculation with Python 3

When we are creating a solution for a problem we can be hindered by the efficency of our solution. A more efficient and well optimized code will run and solve the problem much faster than a less efficient code.

- There are mathematical proofs / analysis you can do to your code to see the theoretical classification of your solution. _Currently this method is beyond the scope of the course, so we will only learn the classification not the proofs_
- We will use a built-in python module to help us calculate the runtime of our code.
    - This way we can compare multiple version of a solution if we have any
    - We can measure performance based on different parameters and inputs
    - This will help us test our code
    - More of the library can be found [here](https://docs.python.org/3/library/timeit.html)

### Example Problem: Most Number of Factors

We will be looking at a simple problem:
- Look at numbers from 1 to N; N being an integer greater than 1.
- Calculate the number of factors of each N<sub>i</sub> has
- Output the number that created the largest factor

#### Method 1:


```python
# Most Number of Factors; Method 1
# Running a timer once

def factor_counter(n):
    """ factor_counter() determines the number of factors N has """
    
    ctr = 0
    for divisor in range(1,n+1):
        if n % divisor == 0:
            ctr += 1
    
    return ctr
# end of factor_counter

from timeit import default_timer as timer

start_timer = timer() # Starting the Timer

# Testing Code
upper_limit = 10000
max_count = 0
result = 0

for n in range(1,upper_limit):
    n_ctr = factor_counter(n)
    
    if n_ctr > max_count:
        result = n
        max_count = n_ctr
# Testing Code Finished

end_timer = timer() # Ending the Timer

# run_time calculation
run_time = end_timer - start_timer

print('Run Time:', run_time)
```

    Run Time: 4.807014966005227


#### Method 1: Starting a timer() and ending a timer()

We are taking a function from the **timeit** module called a **default_timer** and called it **timer**.

When we are about the test the runtime of our code. We are going to section off the execution portion of the code.
- At the beginning, we will _'start'_ the timer ... timestamp of when the code started
- At the end, we will _'end'_ the timer .. timestamp of when the code ended 
- We can calculate the run time by subtracting the end time and start time

In this example, the program took abour 4.8 seconds for analyzing 1 to 10,000.

#### Method 2:


```python
# Most Number of Factors; Method 2
# Average Execution Calculation ... little more messy

testing_code = ''' 
def factor_counter(n):
    """ factor_counter() determines the number of factors N has """
    
    ctr = 0
    for divisor in range(1,n+1):
        if n % divisor == 0:
            ctr += 1
    
    return ctr
# end of factor_counter

upper_limit = 10000
max_count = 0
result = 0

for n in range(1,upper_limit):
    n_ctr = factor_counter(n)
    
    if n_ctr > max_count:
        result = n
        max_count = n_ctr
'''

import timeit as t

# run_time calculation
run_time = t.timeit(testing_code, number=10) / 10

print('Run Time:', run_time)
```

    Run Time: 4.35833643010119


#### Method 2: Using timeit()

In this method, we are using the **timeit()** function from the _timeit_ module.

To lessen the confusion, we renamed the name module as 't' like so:
```python 
import timeit as t```

- **_testing code_** ; holds the lines of code we are testing as a long string variable (hence the messiness!)
- **_number=10_** ; we are specifying how many times to test our code by setting a built-in argument called _number_
- **_/10_** ; we divide it by 10 because the result of timeit is is the total sum of the number of times we ran the code

[Source](https://pythonhow.com/measure-execution-time-python-code/)

## Refactoring

**Unit:** A segment of a program that handles a problem’s specific requirement.

**Refactoring:** The act of improving the performance and efficiency of the unit (section of a program) without affecting input and the output of the unit.

If a program is simplified to its Input → Processing → Output, then we are trying to optimize the “Processing” section of the program by Refactoring.

### Refactoring: Most Number of Factors

**Unit to Refactor:**
```python
def factor_counter(n):
    """ factor_counter() determines the number of factors N has """
    
    ctr = 0
    for divisor in range(1,n+1):
        if n % divisor == 0:
            ctr += 1
    
    return ctr
# end of factor_counter
```

- This code is not the most efficient one, and we will make some optimizations to help it run faster.
    - A product of a number is pair of factors; therefore N = A * B where A and B are factors of N
    - If A is a Factor of N, then we can calculate B by N / A. This helps us a find two factors at once.
    - This way we also need to iterate our for loop only up to the Square Root of N.
        - If N is a perfect square, we can increase our count by 1 to denote that Square Root of N is a factor.
    - Yes, there are even more optimizations that can be done...



```python
# Refactored Most Number of Factor Counter Solution
# Average Execution Calculation

testing_code = ''' 
def factor_counter(n):
    """ factor_counter() determines the number of factors N has """
    
    ctr = 0
    if n < 9:
        # difference of speed between the optimized and non-optimized is very minimial on small numbers
        for divisor in range(1,n+1):
            if n % divisor == 0:
                ctr += 1
        
        return ctr
    else:
        end_point = int(n**0.5) + 1

        for divisor in range(1, end_point):
            if n % divisor == 0 and (n // divisor) != divisor:
                ctr += 2
            elif n % divisor == 0 and (n // divisor) == divisor:
                ctr += 1
            
    return ctr
# end of factor_counter

upper_limit = 10000
max_count = 0
result = 0

for n in range(1,upper_limit):
    n_ctr = factor_counter(n)
    
    if n_ctr > max_count:
        result = n
        max_count = n_ctr
'''

import timeit as t

# run_time calculation
run_time = t.timeit(testing_code, number=10) / 10

print('Run Time:', run_time)
```

    Run Time: 0.10893374489969573


### Notes:
- Our runtime of the solution went from an average of 4.4 seconds to 0.11 seconds
- This was achieve by very minor optimization steps that made us create dramatic changes
- Please understand that the function **factor_counter()** did not changes its **inputs** nor **outputs**

**Optimized Code:**
```python
def factor_counter(n):
    """ factor_counter() determines the number of factors N has """
    
    ctr = 0
    if n < 9:
        # difference of speed between the optimized and non-optimized is very minimial on small numbers
        for divisor in range(1,n+1):
            if n % divisor == 0:
                ctr += 1
        
        return ctr
    else:
        end_point = int(n**0.5) + 1

        for divisor in range(1, end_point):
            if n % divisor == 0 and (n // divisor) != divisor:
                ctr += 2
            elif n % divisor == 0 and (n // divisor) == divisor:
                ctr += 1
            
    return ctr
```

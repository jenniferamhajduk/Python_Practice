# Overview
 - The purpose of this repository is to document my Python language learning journey

## Recursion
- Recursion is a way of solving a problem by having a function call itself
- Can be solved by iteration as well
- Recursion uses different inputs each time
- Base condition is needed to stop recursion. Either answer is found or the answer does not exist
- Can be space inefficient because each call is added to the memory stack. Can be time inefficient  because the system needs for time for pop and push
- Used when problem can be divided into sub problems

### When to use recursion
- We are fine with overhead
- Quick working solution over an efficient one
- When traversing a tree - preorder traversal

## Big O Notation
- Big O notation is the language that describes the efficiency of algorithms. Less or equal to the worst case complexity
- Big Theta is within the bounds of best and worst case complexities
- Big Omega is going to be at least more than the best case complexity
- O(1) - Constant
- O(n) - Linear
- O(LogN) - Logarithmic
- O(N^2) - Quadratic
- O(2^n) - Exponential
- Space complexity describes the amount of memory an algorithm will use
- We drop non-dominant terms when using O notation because different computers have different architectures and have different constant factors
- - O(2N) -> O(N)
- - O(N^2 + N) -> O(N^2)
- - O(2*2^N + 1000N^100) -> O(2^N)
- When do we multiply or add runtimes
- - When algorithms are separate, add
- - When algorithms are nested, multiply
- How to measure code with Big O
- - Assignments and if statements that are executed once: O(1)
- - For loops (not nested) from 0 to N: O(N)
- - Loops that are nested of the same type: O(N^2)
- - A loop in which the controlling parameter is divided in two at each step: O(Log N)
- - Add multiple if statements
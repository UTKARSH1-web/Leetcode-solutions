# LeetCode 2127: Maximum Number of Employees in a Meeting

## Problem Statement
LeetCode Problem **2127 - Maximum Number of Employees in a Meeting** requires finding the maximum number of employees that can be invited to a meeting based on a given directed graph representing a management structure.

## Solution Overview
This folder contains a Python solution for the problem, implementing an **optimized graph-based approach** using **strongly connected components (SCC)** and **cycle detection**.

### Approach:
1. **Graph Representation**: The input is treated as a directed graph where each employee points to their direct manager.
2. **Cycle Detection**: The solution identifies cycles in the graph, as cyclic dependencies determine the meeting group sizes.
3. **Longest Path Calculation**: For non-cyclic components, the longest chain leading into cycles is computed to maximize attendance.
4. **Result Computation**: The answer is determined based on the largest strongly connected component or the combination of longest chains into cycles.


## Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the number of employees (nodes in the graph), leveraging **DFS-based cycle detection** and **longest path computation**.
- **Space Complexity**: `O(N)`, due to the adjacency list representation of the graph and auxiliary structures.

## References
- [LeetCode Problem 2127](https://leetcode.com/problems/maximum-number-of-employees-in-a-meeting/)


 


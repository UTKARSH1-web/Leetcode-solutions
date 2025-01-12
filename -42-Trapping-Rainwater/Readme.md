This folder contains a Python solution to the classic "Trapping Rainwater" problem. 
<br>
The problem asks us to find the maximum amount of rainwater that can be trapped between buildings represented as a list of non-negative integers, 
where each element represents the height of a building.
<br><br>
**Problem Statement**
<br>
Given an array height of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
<br>
**Approach**
<br>
The program uses an optimized two-pointer approach to compute the amount of trapped water. By maintaining pointers at both ends of the elevation map and calculating the minimum boundary at each step, we can efficiently determine the trapped water with a time complexity of O(n).

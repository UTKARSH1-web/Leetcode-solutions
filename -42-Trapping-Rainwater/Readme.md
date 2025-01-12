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
<br><br>
**Algorithm**
<br>
Initialize two pointers: left starting from the beginning and right starting from the end of the array.
Keep track of the maximum height on both the left and right sides.
Move the pointers towards each other, calculating the water trapped at each position based on the shorter boundary.
Accumulate the total trapped water.

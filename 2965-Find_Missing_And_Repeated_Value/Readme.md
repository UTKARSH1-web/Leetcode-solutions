# 📌 Problem: 2965. Find Missing and Repeated Values
You are given a 0-indexed 2D integer matrix grid of size n x n with values in the range [1, n²]. Each integer appears exactly once except:

One number a appears twice

One number b is missing

Your task is to find the repeated and missing numbers.

# 🧾 Input
A 2D matrix of integers of size n x n

# 🎯 Output
Return an array [a, b]:

a: the number that is repeated

b: the number that is missing

# 🧠 Approach
Flatten the 2D matrix and count occurrences of each number from 1 to n² using a frequency array.

Loop through the frequency array:

If a number's count is 2, it is the repeated number a.

If a number's count is 0, it is the missing number b.

# 🔧 Time & Space Complexity
Time Complexity: O(n²)

Space Complexity: O(n²) (for the count array)


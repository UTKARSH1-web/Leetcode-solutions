# 🧮 LeetCode Problem 1695 — Maximum Erasure Value

## 🚀 Problem Statement

You are given an array of **positive integers** `nums` and you want to **erase a subarray** containing **only unique elements**.

The **score** you get by erasing the subarray is equal to the **sum of its elements**.

Return the **maximum score** you can get by erasing **exactly one subarray**.

A subarray is a **contiguous** part of an array.

---

## 🧾 Examples

### Example 1:
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray is [2,4,5,6], 
sum = 17

### Example 2:
Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray is [5,2,1] or [1,2,5], 
sum = 8.


---

## 🔒 Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

---

## 💡 Approach

This problem can be efficiently solved using the **Sliding Window** technique.

### Key Observations:
- We need the **maximum sum** of any **subarray with unique elements**.
- A **set/map** can help us ensure uniqueness in a window.
- As soon as we find a **duplicate**, we shrink the window from the left until all elements become unique.

---

## 🧠 Algorithm Steps

1. Use a `short[] nmap = new short[10001]` as a **frequency map** to track how many times an element appears in the current window.
2. Use two pointers:
   - `left`: starting index of the window.
   - `right`: expanding pointer moving forward.
3. For each element:
   - Add its value to the current total sum and increment its frequency.
   - If a duplicate is found (`nmap[nums[right]] > 1`), move the `left` pointer and reduce total sum and frequency until the duplicate is removed.
4. Track the **maximum sum (`best`)** found during the process.

---


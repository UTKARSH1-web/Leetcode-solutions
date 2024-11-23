<h2><a href="https://leetcode.com/problems/search-in-rotated-sorted-array-ii/">Search In Rotated Sorted Array II</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr>

<p>Given an array <code>nums</code> sorted in non-decreasing order (not necessarily with <b>distinct</b> values).</p>

<p> Before being passed to the function, <code>nums</code> is rotated at an unknown pivot index <code>k (0 <= k < nums.length).</code>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,5,6,0,0,1,2], target = 0
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,5,6,0,0,1,2], target = 3
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= nums.length <= 5000</code></li>
	<li><code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code></li>
    <li><code>nums</code> is guaranteed to be rotated at some pivot.</li>
    <li><code>-10<sup>4</sup> <= target <= 10<sup>4</sup></code></li>
</ul>

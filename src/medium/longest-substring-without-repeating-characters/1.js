/*
 * @lc app=leetcode id=3 lang=javascript
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let start = 0;
  let end = 0;
  let counter = {};

  if (s.length === 0) {
    return 0;
  }

  let max_length = -Infinity;

  while (end < s.length) {
    if (counter[s[end]]) {
      counter[s[start]] = 0;
      start++;
    } else {
      counter[s[end]] = 1;
      end++;
    }
    if (max_length < end - start) {
      max_length = end - start;
    }
  }
  return max_length;
};

// @lc code=end

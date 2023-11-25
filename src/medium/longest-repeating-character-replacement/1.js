/*
 * @lc app=leetcode id=424 lang=javascript
 *
 * [424] Longest Repeating Character Replacement
 */

// @lc code=start
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
  let left = 0;
  let right = 0;
  let max_length = -Infinity;
  let counter = {};
  counter[s[right]] = 1;
  while (right < s.length) {
    let arr = Object.values(counter);
    let maxFreq = Math.max(...arr);
    let subStrLength = right - left + 1;

    if (subStrLength - maxFreq <= k) {
      if (max_length < subStrLength) {
        max_length = subStrLength;
      }
      right++;
      if (counter[s[right]]) {
        counter[s[right]]++;
      } else {
        counter[s[right]] = 1;
      }
      console.log(counter);
    } else {
      // alter counter
      counter[s[left]]--;
      left++;
    }
  }

  console.log(max_length);
  return max_length;
};

// @lc code=end

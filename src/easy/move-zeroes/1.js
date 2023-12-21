/*
 * @lc app=leetcode id=283 lang=javascript
 *
 * [283] Move Zeroes
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  let p = 0;
  let j = 1;
  for (let i = 0; i < nums.length - 1; i++) {
    if (nums[p] !== 0) {
      p++;
      j++;
      continue;
    } else {
      if (nums[j] === 0) {
        j++;
        continue;
      }
      if (nums[j] !== 0) {
        [nums[p], nums[j]] = [nums[j], nums[p]];
        p++;
        j++;
        continue;
      }
    }
  }
  return nums;
};
// @lc code=end

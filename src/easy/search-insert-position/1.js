/*
 * @lc app=leetcode id=35 lang=javascript
 *
 * [35] Search Insert Position
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

var searchInsert = function (nums, target) {
  let i = 0;
  let j = nums.length - 1;
  while (j > i) {
    let mid = i + Math.ceil((j - i) / 2);
    if (target < nums[mid]) {
      j = mid - 1;
    } else if (target > nums[mid]) {
      i = mid;
    } else {
      return mid;
    }
  }
  if (i === j) {
    return i + 1;
  }
};
// @lc code=end

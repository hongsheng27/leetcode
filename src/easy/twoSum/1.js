/*
 * @lc app=leetcode id=1 lang=javascript
 *
 * [1] Two Sum
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let left = 0;
  let right = nums.length - 1;
  let result = [];
  let arr = nums.slice().sort((a, b) => a - b);

  while (right > left) {
    let sum = arr[left] + arr[right];
    if (sum > target) {
      console.log(sum);
      right--;
    } else if (sum < target) {
      left++;
    }
    if (sum === target) {
      const index1 = nums.indexOf(arr[left]);
      const index2 = nums.lastIndexOf(arr[right]);
      result = [index1, index2];
      right--;
    }
  }
};
// @lc code=end

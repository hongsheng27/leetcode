/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const counter = {};
  for (let i = 0; i < nums.length; i++) {
    if (counter[nums[i]]) {
      return true;
    } else {
      counter[nums[i]] = true;
    }
  }
  return false;
};

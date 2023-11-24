/*
 * @lc app=leetcode id=121 lang=javascript
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let left = 0;
  let right = left + 1;
  let max_profit = 0;
  while (right < prices.length) {
    if (prices[right] < prices[left]) {
      left = right;
      right++;
    } else {
      if (max_profit < prices[right] - prices[left]) {
        max_profit = prices[right] - prices[left];
      }
      right++;
    }
  }
  console.log(max_profit);
  return max_profit;
};

// @lc code=end

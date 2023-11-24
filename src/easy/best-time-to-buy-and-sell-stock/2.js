/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let min_value = Infinity;
  let max_profit = 0;
  for (let i = 0; i < prices.length; i++) {
    if (prices[i] < min_value) {
      min_value = prices[i];
    } else {
      profit = prices[i] - min_value;
      if (profit > max_profit) {
        max_profit = profit;
      }
    }
  }
  return max_profit;
};

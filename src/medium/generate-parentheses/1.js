/*
 * @lc app=leetcode id=22 lang=javascript
 *
 * [22] Generate Parentheses
 */

// @lc code=start
/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
  const res = [];
  const dfs = (open, close, str) => {
    if (str.length === n * 2) {
      res.push(str);
      return;
    }
    if (open < n) {
      dfs(open + 1, close, str + "(");
    }
    if (close < open) {
      dfs(open, close + 1, str + ")");
    }
  };
  dfs(0, 0, "");
  console.log(res);
  return res;
};

generateParenthesis(3);
// @lc code=end

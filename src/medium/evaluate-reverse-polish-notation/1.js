/*
 * @lc app=leetcode id=150 lang=javascript
 *
 * [150] Evaluate Reverse Polish Notation
 */

// @lc code=start
/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens) {
  const operators = {
    "+": function (a, b) {
      return a + b;
    },
    "-": function (a, b) {
      return a - b;
    },
    "*": function (a, b) {
      return a * b;
    },
    "/": function (a, b) {
      return a / b;
    },
  };
  const stack = [];
  for (let i = 0; i < tokens.length; i++) {
    if (!operators[tokens[i]]) {
      stack.push(tokens[i]);
    } else {
      console.log(tokens[i], stack);
      let elem2 = stack.pop();
      let elem1 = stack.pop();
      const res = Math.trunc(
        operators[tokens[i]](Number(elem1), Number(elem2))
      );
      stack.push(res);
    }
  }
  return stack.pop();
};

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let stack = [];
  const hashMap = {
    "{": "}",
    "[": "]",
    "(": ")",
  };
  for (let i = 0; i < s.length; i++) {
    if (hashMap[s[i]]) {
      stack.push(s[i]);
    } else {
      let lastElem = stack.pop();
      if (hashMap[lastElem] !== s[i]) {
        return false;
      }
    }
  }
  return stack.length === 0;
};

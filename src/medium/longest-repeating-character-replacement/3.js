// /**
//  * @param {string} s
//  * @param {number} k
//  * @return {number}
//  */
// var characterReplacement = function (s, k) {
//   let left = 0;
//   let right = 0;
//   let max_length = -Infinity;
//   let counter = {};
//   let maxFreq = 0;

//   while (right < s.length) {
//     counter[s[right]] = counter[s[right]] + 1 || 1;
//     maxFreq = Math.max(maxFreq, counter[s[right]]);

//     if (right - left + 1 - maxFreq > k) {
//       counter[s[left]]--;
//       left++;
//     }

//     max_length = Math.max(max_length, right - left + 1);
//     right++;
//   }

//   return max_length;
// };

// characterReplacement("ABAABBBB", 1);

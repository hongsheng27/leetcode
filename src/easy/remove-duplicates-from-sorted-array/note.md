## solution 1

- Use 'two pointers' i and j, where j points to the last different element found so far, and i points to current element being examined. If nums[i] === nums[j], then j++. Otherwise, we increse i and copy nums[j] to nums[i]. repeat this flow until loop finish and return the i + 1.

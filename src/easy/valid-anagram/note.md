## solution 1

- Use 'pointer' to calculate the sum. If there is no match, then move either the right pointer one position to the left or move the left pointer one position to the right to narrow the gap.
  However, this method is not the most suitable for unsorted arrays;It is better suited for handing sorted arrays.
  Nevertheless, it's still a nice attempt.

## solution 2

- Leverage 'counter' to save the complement number to a hash table, then compare the next number to check if it is the right complement

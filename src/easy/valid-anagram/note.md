## solution 1

- Use two hashtables (dictionaries) to store character frequencies of the two strings.
  First, count the frequency of each character in both strings separately.
  Then compare the two hashtables using == to check if both strings are anagrams.
  This approach is clear and correct, but contains repeated code for building each hashtable.

## solution 2

- Optimized version of Solution 1.
  Renamed variables for clarity (e.g., countS, countT).
  Used .get() to reduce repetitive if-else statements.
  Combined both string traversals into a single loop for better performance.
  Added length check at the beginning for early return.
  This approach is more Pythonic and efficient.

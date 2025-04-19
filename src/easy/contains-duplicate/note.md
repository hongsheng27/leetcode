### technique

- counter(hash table)

### python solution 1

- Use a set to track seen elements while iterating through the list.
  If a number is already in the set, return True (duplicate found).
  Since set provides O(1) average-time lookup, this approach improves time complexity to O(n).

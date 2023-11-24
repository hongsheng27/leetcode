### technique

- slide-window

## solution 1

- Use the 'two-pointer' method to set the right pointer adjacent to the left pointer. This indicates that the earliest you can sell is from tomorrow, or you can choose to sell on another day. However, if we encounter a fall in stock price, we then shift our left pointer to the right pointer's position and move the right pointer on step to the right to start a new calculation.

## solution 2

- Try to use one loop to iterate prices to calculate the max price.

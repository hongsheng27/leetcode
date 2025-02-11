### Technique  
- Depth-First Search (DFS)

### Solution  

- Iterate through the grid and start a **DFS** whenever we encounter a `'1'`. This means we've found a new island.  
- The **DFS** explores all connected land (`'1'`) in four directions (up, down, left, right) and marks them as `'0'` to prevent revisiting.  
- Keep a counter `islands` to track the number of DFS calls, which corresponds to the number of islands.  

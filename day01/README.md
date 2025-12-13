# ADVENT OF CODE 2025 - DAY 1
### Secret Entrance

You are given a dial with values ranging from 0 to 99, and it starts at position 50.
The input consists of rotation instuctions, such as: R46, L12, R3, etc...

Each instruction means:
- R -> rotate to the right (increasing the value)
- L -> rotate to the left (decreasing the value)
- The number -> how many steps to rotate

The dial wraps around:
- From 99 -> 0
- From 0 -> 99

PART 1
----------------

Apply all rotations in order and determine the amount of times the final position after one rotation is exactly 0.

My Approach:
I parsed each line of the puzzle input into a (direction, steps) tuple. Starting from dial position 50 on a circular 
range of 0–99, I updated the dial for each instruction using modulo logic to handle wrap‑around. During the 
simulation, I counted how often the dial returned to 0, which forms the final result of the puzzle.


PART 2
----------------

Count how many times the dial passes through position 0 during all rotations.

My Approach:
For Part 2, I reused the same instructions but simulated each rotation step by step instead of applying the full step 
count at once. By updating the dial one position at a time on the circular range and applying modulo when crossing 
boundaries, I could accurately track every moment the dial passed through 0.

ADVENT OF CODE 2025 - DAY 1

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
- Make a list of tuples from input data. Every tuple containing the direction "R" or "L", and the number of steps.
- Loop through through each rotation using the list.
- Update the dial using modulo, increasing if rotating right, decreasing if rotating left.
- Update the total number of "zero's" each time the dial stops at 0.

PART 2
----------------

Count how many times the dial passes through position 0 during all rotations.

My Approach:
- Using the same list;
- Using a for-loop to loop through the range of each step and updating the dial one by one.
- The dial contains numbers 0 - 99, so every time the dial reaches -1 (L) or 100 (R) updating the dial to the right
  range using modulo.
- Updating the count of "zero's" each time the dial passes 0.
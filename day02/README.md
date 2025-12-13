# ADVENT OF CODE - DAY 2
### Gift Shop

In this puzzle, you are given several ranges of ID numbers. Your task is to determine which ID's are invalid based on
specific pattern rules.

# Part 1
----------------

An ID is invalid if it only consists of two identical sequence of digits. Examples: 
* 22 or 456456 -> invalid
* 999 or 123123123 -> valid
You must check all ID's in all ranges and sum the invalid ones.

### My Approach:
I parsed the puzzle input into ID ranges and iterated through each number in those ranges. For every value, I checked 
whether the number consisted of two identical halves (e.g., 3434 → 34 and 34). Numbers matching this pattern were marked
as invalid, and I summed their values to produce the final result.

# Part 2
----------------

The rules expand:
An ID is invalid if it is made entirely of a smaller repeating pattern, repeated two or more times. Examples:
* 1212: pattern 12 -> invalid
* 123123123: pattern 123 -> invalid
* 99999: pattern 9 -> invalid
* 1234: no pattern -> valid
Again, you must sum all invalid ID's

### My Approach:
For Part 2, I reused the same ID ranges but expanded the validation logic. Instead of only checking for repeated halves, 
I evaluated each number for any repeating digit pattern of variable length. If a number could be constructed by 
repeating a smaller substring, it was marked as invalid. All invalid IDs were then summed to produce the final result.
# ADVENT OF CODE - DAY 3
### Lobby

In this puzzle, you are given multiple lines of digits. Your task is to extract specific digits under positional 
constraints and use them to construct valid numbers.

# Part 1
----------------

Each line represents a sequence of digits.
The task is to extract the highest possible two‑digit number from each line without reordering the digits.
You may only select digits in their original left‑to‑right order.
The final answer is the sum of all highest two‑digit numbers across all lines.

### My Approach:

For each line, I identified the highest digit.
If its first occurrence was also the last index, the digit could only serve as the second digit of the two‑digit result.
In that case, I removed it and selected the highest digit from the remaining list as the first digit.
Otherwise, the highest digit became the first digit, and I searched the remaining digits for the next highest value.

# Part 2
----------------

The same logic applies, but now each line must produce the highest possible 12‑digit number, again without changing the order of the digits.
You must choose 12 digits in sequence, always respecting the original left‑to‑right order.
The final answer is the sum of all highest 12‑digit numbers.

### My Approach:

For each line, I constructed the largest possible 12‑digit number.
To ensure enough digits remained, I limited each search to the part of the list that still allowed a full 12‑digit result.
Within that window, I selected the highest digit, appended it to the result, and trimmed the list so the next search started after that digit.
I repeated this process until all 12 digits were chosen, then added the resulting number to the total.

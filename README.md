# Dice Probability Problem

## Problem Statement

You are given two six-sided dice, Die A and Die B, each with faces numbered from 1 to 6. You can only roll both dice together, and your turn is guided by the obtained sum.

### Example:
- Die A = 6, Die B = 3
- Sum = 6 + 3 = 9

You may represent dice as an array or array-like structure.

- Die A = `[1, 2, 3, 4, 5, 6]` where the indices represent the 6 faces of the die & the value on each face.

### Part A (15-20 Minutes):

1. **Total Combinations**:
   - Calculate the total number of combinations possible when rolling both Die A and Die B together.
   - Show the math along with the code.

2. **Distribution of Combinations**:
   - Calculate and display the distribution of all possible combinations that can be obtained when rolling both Die A and Die B together.
   - Hint: A 6 x 6 Matrix.
   - Show the math along with the code.

3. **Probability of All Possible Sums**:
   - Calculate the probability of all possible sums occurring among the number of combinations from (2).
   - Example: P(Sum = 2) = 1/X as there is only one combination possible to obtain Sum = 2. Die A = Die B = 1.

### Part B (25-30 Minutes):

Now comes the real challenge. You were happily spending a lazy afternoon playing your board game with your dice when suddenly the mischievous Norse God Loki (you love Thor too much & Loki didn’t like that much) appeared.

Loki dooms your dice for his fun by removing all the “spots” off the dice.

No problem! You have the tools to re-attach the “spots” back on the Dice. However, Loki has doomed your dice with the following conditions:
- Die A cannot have more than 4 spots on a face.
- Die A may have multiple faces with the same number of spots.
- Die B can have as many spots on a face as necessary, i.e., even more than 6.

But in order to play your game, the probability of obtaining the sums must remain the same! So if you could only roll P(Sum = 2) = 1/X, the new dice must have the spots reattached such that those probabilities are not changed.

### Input:
- Die_A = `[1, 2, 3, 4, 5, 6]` & Die_B = `[1, 2, 3, 4, 5, 6]`

### Output:
- A transform function `undoom_dice` that takes (Die_A, Die_B) as input & outputs `New_Die_A = [?, ?, ?, ?, ?, ?]`, `New_Die_B = [?, ?, ?, ?, ?, ?]` where,
- No `New_Die_A[x] > 4`

The logic used to solve this problem is in the pdf file that has been uploaded as part of this repository.

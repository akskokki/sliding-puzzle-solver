# Week 3 progress report

This week I implemented the first iteration of the IDA* solving algorithm for the game. Unfortunately this required quite a bit of refactoring on the Pygame side of things, but I managed to work it out.

The algorithm as of now runs with only the Manhattan distance heuristic. This means most fully scrambled board states take way too long to solve, but solutions below ~45 moves are found easily.

I also added some docstring documentation to describe the functionality of the different classes and their attributes. This will be expanded to all functions in the future.

Testing is unfortunately lagging behind, refactoring the old code to support my implementation of the solving algorithm took too much time. This will be top priority for next week.

Additionally, next week I will be looking into how to improve the heuristic to have better solve times. Initially I will look into how the performance improves by solving for linear conflicts in the board state (two tiles having to pass each other on the same row/column will necessarily increase the required moves by at least two), but I might have to end up using a pattern database.

Time spent this week: ~7 hours

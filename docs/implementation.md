# Implementation Document
The application allows the user to manually or automatically solve the 15 puzzle via a GUI implemented with Pygame. The solving algorithm used is IDA*, with the heuristic of walking distance, using Manhattan distance and taking into account linear conflicts.

## The Algorithm
Iterative Deepening A*, or IDA*, is used to find the optimal path to a solved board state from the current board position. The heuristics being used is the Walking distance that each tile is from its solved position, when solving for linear conflicts.

## Time and space complexity
The absolute worst case time complexity for this algorithm is O(*b<sup>d</sup>*) with *b* being the branching factor (averaging about 2.13 for the 15-puzzle), and *d* being the depth of the solution. The real average time complexity is considerably more complicated to determine, however, as it depends so heavily on the difficult-to-analyse impact of the heuristics being utilised.

The space complexity of the algorithm is much simpler to calculate. All that is being stored is the list of moves from the start node to the current position, so the maximal space used by a solution is O(*d*).

## Effectiveness of the chosen heuristic
The heuristic being used is still a bit weak, and most of the time the algorithm cannot, in reasonable time, handle a depth much deeper than ~50 moves. It is still enough to provide us with some interesting performance data, though.

## Sources
[Iterative Deepening A*](https://en.wikipedia.org/wiki/Iterative_deepening_A*) on Wikipedia

[Looking into k-puzzle Heuristics](https://medium.com/swlh/looking-into-k-puzzle-heuristics-6189318eaca2) by Ding YuChen

[Single Agent Search Lectures](https://www.youtube.com/playlist?list=PLsgwB9-SGvkA43MDmseV701T3gTdA-2Il) by Nathan Sturtevant

[Solving the 15 Puzzle in Python with IDA*](https://youtu.be/g0phuZDM6Mg) by Michael Schrandt

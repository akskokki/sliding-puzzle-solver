# Implementation Document
The application allows users to manually or automatically solve the 15 puzzle via a GUI implemented with Pygame. The solving algorithm used is IDA*, currently with just the simple heuristic of Manhattan distance.

## Usage
The board can be manually controlled with the arrow keys. Spacebar can be used to perform a relatively weak shuffle (100 moves), and Enter runs the search algorithm. Once the search is complete, continuous presses of the Enter key will automatically run through the solution path.

## The Algorithm
Iterative Deepening A*, or IDA*, is used to find the optimal path to a solved board state from the current board position. The heuristic being used is the Manhattan distance that each tile is from its solved position. On its own this heuristic is still too weak, and the algorithm cannot, in reasonabel time, handle a depth deeper than ~45 moves. This will be improved in the future by looking into linear conflicts and pattern databases.

## Sources
[Iterative Deepening A* on Wikipedia](https://en.wikipedia.org/wiki/Iterative_deepening_A*)
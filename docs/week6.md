# Week 6 progress report

This week I wrote docstring documentation for all relevant functions in the program, and added some new logging functionality to the program to improve the user experience and allow me to do performance testing.

My plan for performance testing is to write a script that repeatedly scrambles the board and attempts to run the solving algorithm, with a cutoff point at somewhere between 60-120 seconds per solve. I will log the initial board state, whether the algorithm was able to solve the board state in the allotted time, how long the solve took, how many moves were required and how many nodes were explored during the search. I'll leave this running for a few hours, and I think it will get me some really interesting data on the performance of my program. I'm particularly curious to see what I'll find by solving the same set of board states without using the linear conflicts heuristic. Does this sound like a reasonable approach?

Time spent this week: ~9 hours

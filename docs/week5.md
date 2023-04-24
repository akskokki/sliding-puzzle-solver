# Week 5 progress report

This week I looked into optimising the search algorithm, and implemented a lot more testing for the IDAStar and Board classes, taking into account the feedback received in the peer review.

In an attempt to optimise the search algorithm, I got rid of the path-variable which was holding deepcopies of all the different board states. Additionally I implemented linear conflict resolution as an additional heuristic. These had a noticeable impact on performance and memory usage, but unfortunately the algorithm is still too weak to solve many board states.

The solutions I see from my research are to either implement pattern databases as a heuristic, or downgrade from the 15-puzzle to the 8-puzzle. Would the latter be acceptable for the course, or should I stick with the 15-puzzle? I think it would be nice to be able to keep using my current heuristics, and potentially also make some comparisons with and without linear conflict resolution to see the impact it has, but I don't think this is possible with the complexity of the 15-puzzle.

Next week I will (finally) add more docstring documentation, and try and further resolve the issue of performance.

Time spent this week: ~9 hours

# Rush Hour

## Case explanation 
The case we chose for this assignment is Rush Hour. Rush Hour is a game where the goal is to lead the red car to the exit on the right side of the board. The problem is that, the path is blocked by other cars and trucks. The boards consists of a 6x6, 9x9 or even 12x12 grid, filled with the red car, other cars and other trucks. Each car has its own orientation, either vertical or horizontal, meaning it can only move in that direction. 

## Algorithms
The goal was to write several algorithms, which optimalize the red car’s way to the exit, and to be able to find the shortest solution. The following algorithms were used: 

1.	Random algorithm: 
In the random algorithm, a random choice out of move options is chosen from a start board. This process is repeated until the solution is found. The only heuristic that was applied is that a car is not able to bounce up and down.

2.	Breadth first algorithm: 
In the breadth first algorithm, the starting board can be seen as the ‘parent’ board. This is best visualized with a tree, starting from the parent and going down in different branches. From the parent board, different moves can be made which will create different ‘children’ boards. Each of the children boards is put in the back of a queue, and this is done for all the following ‘children’ boards as well. This way, the tree is flattened out into a long queue. From this queue, the first item is being popped out of the queue, and this continues until the game is solved. 

3.	Depth first: 
In the depth first algorithm, it is very easy to compare with the breadth first. The only thing that is different, that instead of flattening out the tree, it goes deep into every ‘child’ board, before going any further. So from the parent board, one ‘child’ board is picked, and then it goes further into that ‘child’s’ children boards, etc.

3. Beam search: 
In the Beam Search algorithm, the queue is sorted based on different heuristics. The first heuristic makes an approximation of the minimum amount of steps needed for the red car to reach its destination. The second heuristic combines 'scores' attached to the x- and y-coordinates of the cars, as well as the x-coordinate of the red car, to find the fastest solution. 
As Beam Search is used, the sorted queue is pruned, by excluding any items that exceed 10.000.

## Files
- /code: contains all the code necessary for this project
    - /code/algorithms: contains all the code concerning the algorithms 
    - /code/classes: contains all the code concerning the two needed classes for this case (Board and Cars)
- /data: contains the different data files necessary to fill the grid and visualize the board

## Reproducing results 
When starting the game, different prompts are presented, in which you can choose the size of the grid, choose the game with that specific size grid and choose an algorithm. 
Our program runs with Python 3.

To run the program, run the following in the terminal: python3 main.py

This will lead to the following prompt: 
‘What size (6, 9 or 12) grid would you like?’

Then, you will be asked to choose a board (the example below considers the 6x6 grid): 
‘Choose a file number if you'd like (1, 2, 3)'

Lastly, you will be asked to choose an algorithm. 
‘Select algorithm from random, depth first, beam search, breadth first'

In case you choose Beam Search, an extra question will be asked: 
'Select heuristic: min_steps, combination'

The results from the Breadth First, Depth First, and Beam Search algorithms will be presented in a separate csv file called: output.csv. This file can be found in the output folder. 
The results from the random are only to be found in the terminal, as the csv file for this algorithm would not add any value. 

## Authors 
- Michael van Gompel
- Ahmed Moenna
- Sanne Zijlstra
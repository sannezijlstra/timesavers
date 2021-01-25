# Case explanation 
The case we chose for this assignment is Rush Hour. Rush Hour is a game where the goal is to lead the red car to the exit on the right side of the board. The problem is that, the way is dispersed by other cars and trucks, all going their own way. The boards consists of a 6x6, 9x9 or even 12x12 grid, filled with the red car, other cars and other trucks. Each car has its own orientation, either vertical or horizontal, meaning it can only move in that direction. 

# Algorithms
The goal was to write several algorithms, which optimalize the red car’s way to the exit, and to be able to find the shortest solution. The following algorithms were used: 

1.	Random algorithm: 
In the random algorithm, a random choice out of move options is chosen from a start board. This process is repeated until the solution is found. The only heuristic that was applied is that a car is not able to bounce up and down. 

2.	Breadth first algorithm: 
In the breadth first algorithm, the starting board can be seen as the ‘parent’ board. This is best visualized with a tree, starting from the parent and going down in different branches. From the parent board, different moves can be made which will create different ‘children’ boards. Each of the children boards is put in the back of a queue, and this is done for all the following ‘children’ boards as well. This way, the tree is flattened out into a long queue. From this queue, the first item is being popped out of the queue, and this continues until the game is solved. 
all possible boards going from a start/’parent’ board are put into a queue. 

3.	Depth first: 
In the depth first algorithm, it is very easy to compare with the breadth first. The only thing that is different, that instead of flattening out the tree, it goes deep into every ‘child’ board, before going any further. So from the parent board, one ‘child’ board is picked, and then it goes further into that ‘child’s’ children boards, etc.

## Files
Code folder:
Cars.py: consists of all information concerning the car objects
Board.py: consists of all 

Algorithms folder: 

## Reproducing results 
When starting the game, different prompts are presented, in which you can choose the size of the grid, choose the game with that specific size grid and choose an algorithm. 
Our program runs with Python 3.

To run the program, run the following in the terminal: python3 main.py  

This will lead to the following prompt: 
‘What board size would you like to solve?’
1.	6x6 grid
2.	9x9 grid
3.	12x12 grid 
Then, you will be asked to choose a board (the example below considers the 6x6 grid): 
‘Which board would you like to solve?’
1.	Board 1
2.	Board 2
3.	Board 3
Lastly, you will be asked to choose an algorithm. 
‘Which algorithm would you like the game to be played with?’
1.	Breadth first search
2.	Depth first search 
3.	Random search
4.	Iterative deepening (?)
The results will be presented like this: 
‘-----’ (eventjes kopieren van resultaten uit terminal) 




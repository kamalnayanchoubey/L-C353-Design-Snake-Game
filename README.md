# L-C353-Design-Snake-Game
Design Snake Game

<br>

Leet Code Medium Level Problem 353
<br>

 Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.

 <br>

 The snake is initially positioned at the top left corner (0,0) with length = 1 unit.
<br>

 You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.
<br>

 Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

 <br>

 When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.
<br>


Example:
<br>
 Given width = 3, height = 2, and food = [[1,2],[0,1]].
<br>
 Snake snake = new Snake(width, height, food);
<br>
Initially the snake appears at position (0,0) and the food at (1,2).
<br>
 |S| | |
 <br>
 | | |F|
<br>

snake.move("R"); -> Returns 0
<br>
 | |S| |
 <br>
 | | |F|
 <br>

 snake.move("D"); -> Returns 0
<br>
 | | | |
 <br>
 | |S|F|
<br>
 snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )
<br>
 | |F| |
 <br>
 | |S|S|
<br>
snake.move("U"); -> Returns 1
<br>
 | |F|S|
 <br>
 | | |S|
<br>
snake.move("L"); -> Returns 2 (Snake eats the second food)
<br>
| |S|S|
<br>
| | |S|
<br>

snake.move("U"); -> Returns -1 (Game over because snake collides with border)
<br>

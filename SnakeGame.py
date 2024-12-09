class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        #Initialize your data  struture
        #@width - screen width
        #@height - screen height 
        #@food - Alist of food position
        self.m = height
        self.n = width
        self.food = food
        self.score = 0
        self.idx = 0
        self.q = deque([(0, 0)])
        self.vis = {(0, 0)}

    def move(self, direction: str) -> int:
        #Move the snake 
        #direct - 'U' = up, 'L' =left 'R' = right 'D'= Down
        #return The game's score after the moves Return -1 if game over
        # Game over when snake cross the screen the screen boundray or bites its bodey
        i, j = self.q[0]
        x, y = i, j
        match direction:
            case "U":
                x -= 1
            case "D":
                x += 1
            case "L":
                y -= 1
            case "R":
                y += 1
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            return -1
        if (
            self.idx < len(self.food)
            and x == self.food[self.idx][0]
            and y == self.food[self.idx][1]
        ):
            self.score += 1
            self.idx += 1
        else:
            self.vis.remove(self.q.pop())
        if (x, y) in self.vis:
            return -1
        self.q.appendleft((x, y))
        self.vis.add((x, y))
        return self.score

def move(self, direction):
    if (direction == "up" and self.position[0] == "0") or (direction == "down" and self.position[0] == "4") or (direction == "right" and self.position[1] == "4") or (direction == "left" and self.position[1] == "0") or direction not in ('up', 'down', 'right', 'left'):
        raise ValueError("Invalid move, hero unable to move in that direction")
    if direction == "up":
        self.position = str(int(self.position[0]) - 1) + self.position[1]
    elif direction == "down":
        self.position = str(int(self.position[0]) + 1) + self.position[1]
    elif direction == "right":
        self.position = self.position[0] + str(int(self.position[1]) + 1)
    else:
        self.position = self.position[0] + str(int(self.position[1]) - 1)
    return self.position


Hero.move = move

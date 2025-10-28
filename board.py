class Board:

    def __init__(self, length, height):
        self.height = height
        self.length = length
        self.xCoordinates = [chr(i + 65) for i in range(length)]
        self.yCoordinates = [str(i + 1) for i in range(height)]
        self.field = [["◯" for _ in range(length)] for _ in range(height)]

    def changeSymbol(self, x, y, symbol):
        if self.field[int(y) - 1][ord(x) - 65] == "◯":
            self.field[int(y) - 1][ord(x) - 65] = symbol
            return True
        return False

    def printBoard(self):
        #print out xCoordinates
        print("    ", end="")
        for j in range(self.length):
            if j + 1 < self.length: #check if last in row --> no stupid spaces after a row.
                print(f"{self.xCoordinates[j]}  ", end=" ")
            else:
                print(self.xCoordinates[j])
                if j % 6 == 0:
                    print(" ", end="")
        print()
        
        #print out yCoordinates
        for i in range(self.height):
            print(f"{self.yCoordinates[i]}".rjust(2, " "), end=" ")
            #print field
            for k in range(self.length):
                if k + 1 < self.length: #check if last in row --> no stupid spaces after a row.
                    print(f" {self.field[i][k]}", end="  ")
                else:
                    print(f" {self.field[i][k]}")
            print()
        


    def four_in_a_row(self, symbol):
        #if four in a row return true else false
        for y in range (self.height):
            for x in range(self.length):
                if x < self.length - 3: #if to the rigth is possible
                    if self.field[y][x] == self.field[y][x + 1] == self.field[y][x + 2] == self.field[y][x + 3] == symbol:
                        return True
                if y < self.height - 3: #if downwards is possible 
                    if self.field[y][x] == self.field[y + 1][x] == self.field[y + 2][x] == self.field[y + 3][x] == symbol:
                        return True
                    if x < self.length - 3: #if downwards to the rigth is possible
                        if self.field[y][x] == self.field[y + 1][x + 1] == self.field[y + 2][x + 2] == self.field[y + 3][x + 3] == symbol:
                            return True
                    if x > 2: #if downwards to the left is possible
                        if self.field[y][x] == self.field[y + 1][x - 1] == self.field[y + 2][x - 2] == self.field[y + 3][x - 3] == symbol:
                            return True
        return False

    def isFull(self):
        #if Board is Full return True
        for row in self.field:
            for symbol in row:
                if symbol == "◯":
                    return False
        return True
    

class Player:

    def __init__(self, name):
        self.name = name
        self.symbol = None


    def getSymbol(self):
        return self.symbol


    def chooseColor(self, availableColors: list[str]):

        while True:      
            playerColor = input(f"{self.name}, choose your color {availableColors}: ").lower().strip()
                
            if playerColor in availableColors:
                availableColors.pop(availableColors.index(playerColor))
                if playerColor == "green":
                    self.name = f"\033[92m{self.name}\033[0m"
                    self.symbol = "\033[92m●\033[0m"
                elif playerColor == "blue":
                    self.name = f"\033[94m{self.name}\033[0m"
                    self.symbol = "\033[94m●\033[0m"
                elif playerColor == "yellow":
                    self.name = f"\033[93m{self.name}\033[0m"
                    self.symbol = "\033[93m●\033[0m"
                elif playerColor == "red":
                    self.name = f"\033[91m{self.name}\033[0m"
                    self.symbol = "\033[91m●\033[0m"
                break
            else:
                print("Wrong color, try again!")
        print(f"{self.name} chose {playerColor} ({self.symbol})")
                
import random

class Bot(Player):
    
    def chooseColor(self, availableColors: list[str]):

        while True:      
            playerColor = random.choice(availableColors)
                
            if playerColor in availableColors:
                availableColors.pop(availableColors.index(playerColor))
                if playerColor == "green":
                    self.name = f"\033[92m{self.name}\033[0m"
                    self.symbol = "\033[92m●\033[0m"
                elif playerColor == "blue":
                    self.name = f"\033[94m{self.name}\033[0m"
                    self.symbol = "\033[94m●\033[0m"
                elif playerColor == "yellow":
                    self.name = f"\033[93m{self.name}\033[0m"
                    self.symbol = "\033[93m●\033[0m"
                elif playerColor == "red":
                    self.name = f"\033[91m{self.name}\033[0m"
                    self.symbol = "\033[91m●\033[0m"
                break
            else:
                print("Wrong color, try again!")
        print(f"{self.name} chose {playerColor} ({self.symbol})")
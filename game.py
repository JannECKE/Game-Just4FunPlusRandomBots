from board import Board
from player import Player
from player import Bot

import time
import random

class Game:
    def __init__(self):
        self.board = None
        self.amountOfPlayers = 0
        self.amountOfBots = 0
        self.players = []

    def setup(self):
        # ---basic game rules---
        while True:

            try:
                # ---board initialization---
                length = int(input("Input Board length (4-20): "))
                height = int(input("Input Board height (4-20): "))
                if height > 20 or length > 20 or height < 4 or length < 4:
                    raise ValueError
                self.board = Board(length, height)

                # ---PlayerAmount---
                print("How many Players/Bots do you want to play?")
                self.amountOfPlayers = int(input("Input amount of total Players (0-4 total): "))
                self.amountOfBots = int(input("Input amount of total Bots (0-4 total): "))  

                if not 0 <= self.amountOfPlayers <= 4 or not 0 <= self.amountOfBots <= 4 or not 0 <= self.amountOfBots + self.amountOfPlayers <= 4:
                    raise ValueError
                
            except ValueError:
                print("ValueError, try again")
                continue
            break
        
        # ---player assignment---
        availableColors = ["red", "yellow", "blue", "green"]        
        for i in range(self.amountOfPlayers):
            player = Player(f"Player{i + 1}")
            player.chooseColor(availableColors)
            self.players.append(player)

        # ---bot assignment---
        for i in range(self.amountOfPlayers, self.amountOfBots + self.amountOfPlayers):
            player = Bot(f"Bot{i + 1 - self.amountOfPlayers}")
            player.chooseColor(availableColors)
            self.players.append(player)

        self.board.printBoard()


    def run(self):
        
        currentPlayerIndex = 0

        # ---gameloop---
        while True:

            currentPlayer: Player = self.players[currentPlayerIndex]

            if currentPlayerIndex <= self.amountOfPlayers - 1:
                # ---Player: place symbol---
                coordinates = input(f"{currentPlayer.name}: Enter coordinates (letter,number): ")
                if "," not in coordinates:
                    print("Wrong input. Don't forget the comma, try again!")
                    continue
                x,y = coordinates.split(',')
                x = x.strip().upper()
                if (len(x) != 1) or (not x in self.board.xCoordinates) or (not y in self.board.yCoordinates):
                    print("Wrong input, try again!")
                    continue
                if self.board.changeSymbol(x, y, currentPlayer.getSymbol()) == False:
                    print("Was already taken! try again!")
                    continue
            else:
                # ---Bot: place symbol---
                time.sleep(0.5)
                print(f"{currentPlayer.name}: Enter coordinates: ", end='')
                while True: #check if bot placed correctly
                    x = random.choice(self.board.xCoordinates)
                    y = int(random.choice(self.board.yCoordinates))
                    if not self.board.changeSymbol(x, y, currentPlayer.getSymbol()):
                        continue
                    break
                print(f"{x},{y}")
                
            self.board.printBoard()

            # ---check if player won---
            if self.board.four_in_a_row(currentPlayer.getSymbol()):
                print(f"{currentPlayer.name} wins!!!")
                break
            
            # ---check if board is full---
            if self.board.isFull():
                print("The board is full, it's a draw!")
                break

            # ---switchTurnplayer---
            if currentPlayerIndex + 1 < self.amountOfPlayers + self.amountOfBots:
                currentPlayerIndex += 1
            else:
                currentPlayerIndex = 0
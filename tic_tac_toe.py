#Created by: Jared Chinchilla Sanchez
#Date: 01/15/2022
import random
from termcolor import colored


numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

players = ["X", "O"]

player = random.choice(players)

def main(player):

    while True:
        writer()
        position = int(input(f"Player ({player}) please select your next position: "))

        if player.lower() in ["x"]:
            numbers[position - 1] = colored(player, "red")
            player = "O"
        else:
            numbers[position - 1] = colored(player, "yellow")
            player = "X"

def writer():
    print(f"|{numbers[0]}|{numbers[1]}|{numbers[2]}|\n|{numbers[3]}|{numbers[4]}|{numbers[5]}|\n|{numbers[6]}|{numbers[7]}|{numbers[8]}|")

if __name__ == "__main__":
    main(player)



    
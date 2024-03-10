# File: CS112_A1_T2_3_20230573.py.
# Purpose: This is a two-player mathematical game of strategy. It is played by two people with a pile of coins between them. 
# The players take turns removing coins from the pile, always removing a non-zero square number of coins. The player who removes the last coin wins.
# Author: Youssef Ahmed Fathy Eshta
# ID: 20230573

import random
#This function is where the game itself is executed
def Game3():
    while True: # This while loop gives the user choices for starting the game with a number of his choice or a randomly generated integer
        Choice2 = input("A) Choose your own number\n" "B) Use randomly generated number between 1 and 1000\n")
        Choice2Cap = Choice2.upper()
        if Choice2Cap == "A":
            while True: # This while loop is used to make sure the input of the coin balance is a positive non-zero integer
                try: 
                    Coins = int(input("Insert the number of Coins you wish to start the game with: ")) # This line takes the input of the initial coins balance the game is set to start with
                    while Coins <= 0: # This while loop is used to make sure the input of the coin balance   is a positive integer
                        print("Please Insert a positive non-zero integer value!")
                        Coins = int(input("Insert the number of Coins you wish to start the game with: ")) # This line takes the input of the initial coins balance the game is set to start with
                    break
                        
                except: 
                    print("Please Insert a valid positive integer!")
            break
        elif Choice2Cap == "B": # This condition is used to randomize the coin balance the user wishes to start with
            Coins = random.randint(1, 1000)
            print("Your current Coin balance is", Coins)
            break
        else:
            print("Please Insert valid option!")

    Player1 = input("Insert the username Player 1 wishes to use: ") # This line takes the input of the username that player 1 wishes to use
    while Player1 == '': # This while loop makes sure that player 1 username is not empty
        print("Username cannot be empty!")
        Player1 = input("Insert the username Player 1 wishes to use: ") # This line takes the input of the username that player 1 wishes to use

    Player2 = input("Insert the username Player 2 wishes to use: ") # This line takes the input of the username that player 2 wishes to use
    while Player2 == '': # This while loop makes sure that player 2 username is not empty
        print("Username cannot be empty!")
        Player2 = input("Insert the username Player 2 wishes to use: ") # This line takes the input of the username that player 2 wishes to use
    while Player2 == Player1:
        print("This username has already been chosen by Player 1")
        Player2 = input("Insert the username Player 2 wishes to use: ") # This line takes the input of the username that player 2 wishes to use


    while Coins>0: # This while loop executes the code below while the coins balance is more than zero
        while True: # This while loop is used to make sure the input of the move of player 1 is a positive non-zero integer
            try:
                Move1 = int(input(f'{Player1} Insert square number you wish to be subtracted from the Coins balance: ')) # This line takes the input of the move of the player 1
                while Move1<=0: # This while loop is used to make sure the input of the move of player 1 is a positive integer
                    print("Please insert a positive integer larger then zero!") 
                    Move1 = int(input(f'{Player1} Insert square number you wish to be subtracted from the Coins balance: ')) # This line takes the input of the move of the player 1

                while ((Move1**0.5)%1) != 0: # This while loop makes sure that the value of move of player 1 is a square of an integer
                    print("Please insert a positive square integer larger then zero!")
                    Move1 = int(input(f'{Player1} Insert square number you wish to be subtracted from the Coins balance: ')) # This line takes the input of the move of the player 1


                while (Coins - Move1) < 0: # This while loop is used to make sure the coin balance is not negative

                    print("Your Coin Balance can't be negative\n" "Insert a valid number!")
                    Move1 = int(input(f'{Player1} Insert square number you wish to be subtracted from the Coins balance: ')) # This line takes the input of the move of the player 1

                    while Move1<=0: # This while loop is used to make sure the input of the move of player 1 is a positive integer
                        print("Please insert a positive integer larger then zero!")
                        Move1 = int(input(f'{Player1} Insert square number you wish to be subtracted from the Coins balance: ')) # This line takes the input of the move of the player 1
                break        
            except ValueError:
                print("Please insert valid positive square integer value!")


        Coins = Coins - Move1 # This line updates the value of the coin balance after subtracting the move of player 1
        print("Current coin balance is ", Coins)
        if Coins==0: # This condition declares player 1 as the winner if they are the last to make a move and the coin balance has reached zero
            print(Player1, "is the Winner!")
            break

        while True: # This while loop is used to make sure the input of the move of player 2 is a positive non-zero integer
            try:
                Move2 = int(input(f'{Player2} Insert square number you wish to be subtracted from the Coins balance: ')) # This line takes the input of the move of the player 2
                
                while Move2<=0: # This while loop is used to make sure the input of the move of player 2 is a positive integer
                    print("Please insert a positive integer larger then zero!") 
                    Move2 = int(input(f'{Player2} Insert square number you wish to be subtracted from the Coins balance: ')) # This line takes the input of the move of the player 2
                
                while ((Move2**0.5)%1) != 0: # This while loop makes sure that the value of move of player 2 is a square of an integer
                    print("Please insert a positive square integer larger then zero!")
                    Move2 = int(input(f'{Player2} Insert square number you wish to be subtracted from the Coins balance: ')) # This line takes the input of the move of the player 2

                while (Coins - Move2) < 0: # This while loop is used to make sure the coin balance is not negative

                    print("Your Coin Balance can't be negative\n" "Insert a valid number!")
                    Move2 = int(input(f'{Player2} Insert square number you wish to be subtracted from the Coins balance: ')) # This line takes the input of the move of the player 2

                    while Move2<=0: # This while loop is used to make sure the input of the move of player 2 is a positive integer
                        print("Please insert a positive integer larger then zero!")
                        Move2 = int(input(f'{Player2} Insert square number you wish to be subtracted from the Coins balance: ')) # This line takes the input of the move of the player 2
                break        
            except ValueError:
                print("Please insert valid positive square integer value!")

        Coins = Coins - Move2 # This line updates the value of the coin balance after subtracting the move of player 2
        print("Current coin balance is ", Coins)
        if Coins==0:  # This condition declares player 2 as the winner if they are the last to make a move and the coin balance has reached zero
            print(Player2, "is the Winner!")
            break

while True: # This while loop acts as the menu of the game
    print("Welcome to 'Subtract-A-Square'")
    Choice1 = input("A) Start New Game\n" "B) Exit\n") # This line takes the user's choice in the menu
    Choice1Cap = Choice1.upper() # This line the input of the user and makes it upper case
    if Choice1Cap == "A": # This condition executes the function of the game when the user chooses the first option in the menu
        Game3()
    
    elif Choice1Cap == "B": # This condition exits the game when user chooses the second option in the menu
        break

    else: # This condition asks the user to input to input a valid choice for the menu
        print("Please Insert a Valid Choice")
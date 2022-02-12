#Python libraries
import turtle
import random
import time

#Function files
import turtle_functions
import dice_functions

#Variable_File
import variable_file

#Check which version should use
def game_version():

    while True: #pick which version should be used in the game

        try: #small try - catch block to prevent from thrownig error when something else is typed

            choose = int(input("Which version do You want to play? [ 1 - default version ; 2 - extended game version ; 3 - quit from the game! ] "))

        except ValueError:
            print("Oops! That is not a valid number ! Try again!")
            continue

        if choose == 1 or choose == 2:
            variable_file.game_verson = int(choose)
            break
        elif choose == 3:
            quit()

######################EXTENDED VERSION FUNCTIONS######################

#Button fucntion for handling exiting from the game
def ExitGame(x,y): #Exit game
    exit(0)

#Button fucntion for rolling the dice
def rollADice(x, y):  # Additional module for handling buttons click

    variable_file.roll_a_dice.shape("images/roll_button_unable.gif")

    if (variable_file.is_cr_runn == True):
        return
    else:
        variable_file.is_cr_runn = True

    if (variable_file.isFirstPlayer):
        dice_functions.setdiceAnimation(variable_file.dice)
        value = random.randrange(1, 7)
        dice_functions.setDiceValue(variable_file.dice, value)
        print("Player one rolled: ", value)

        variable_file.last_roll_text.clear()
        variable_file.last_roll_text.write("Last roll: " + str(value), align="center", font=("Arial", 18, "italic"))

        variable_file.next_roll_text.clear()
        variable_file.next_roll_text.write("Player two will roll a dice now !", align="center",
                                           font=("Arial", 18, "italic"))

        movePlayer(1, value)

    else:
        dice_functions.setdiceAnimation(variable_file.dice)
        value = random.randrange(1, 7)
        dice_functions.setDiceValue(variable_file.dice, value)
        print("Player two rolled: ", value)

        variable_file.last_roll_text.clear()
        variable_file.last_roll_text.write("Last roll: " + str(value), align="center", font=("Arial", 18, "italic"))

        variable_file.next_roll_text.clear()
        variable_file.next_roll_text.write("Player one will roll a dice now !", align="center",
                                           font=("Arial", 18, "italic"))
        movePlayer(2, value)


    variable_file.isFirstPlayer = not variable_file.isFirstPlayer

    variable_file.is_cr_runn = False
    variable_file.roll_a_dice.shape("images/roll_button.gif")

######################END OF EXTENDED VERSION FUNCTIONS######################

def playerWin(whichPlayer):  #Which player won , show the winning screen.

    turtle_functions.playerWin(whichPlayer)

    #If it is "extended" version we don't neeed a loop to detect next pick
    if(variable_file.game_verson == 2):
        variable_file.button_yes.onclick(turtle_functions.RestartTheGame, 1)
        variable_file.button_no.onclick(ExitGame, 1)
        return

    print("Player " , whichPlayer , " won the game ! ")

    #Detect if player want to play again?

    while True:
        player_input = input("Play next game ? [y/n]")
        if player_input == "n" : #don't need try catch as it is string
            exit(0)
        elif player_input == "y" :
            break

    variable_file.isFirstPlayer = False

    turtle_functions.hidePlayerWin()

#Main function for moving the player
def movePlayer(whichPlayer , howLong):

    move_backwards = False

#bullPlayer = 1 , cowPlayer = 2

    if(whichPlayer == 1):

        player_object = variable_file.bull_object
        player_next_direction = variable_file.bull_next_direction
        player_number = variable_file.bull_number
    else:

        player_object = variable_file.cow_object
        player_next_direction = variable_file.cow_next_direction
        player_number = variable_file.cow_number

    player_object.speed(2)

    for i in range(howLong):

        time.sleep(0.2)
        howLong -= 1

        if (player_number % 5 == 0):

            if (player_next_direction == False):
                player_object.left(90)
                player_object.forward(160)
                player_object.left(90)
                player_next_direction = True
                turtle_functions.swapGif(player_object)

            else:
                player_object.right(90)
                player_object.forward(160)
                player_object.right(90)
                player_next_direction = False
                turtle_functions.swapGif(player_object)
        else:
            player_object.forward(160)

        player_number += 1

        if (player_number >= 25 and howLong > 0):
            break

    if((variable_file.game_verson == 2) and (player_number >= 25 and howLong == 0)): #If extended version , player need to exacly "stay" on 25 field , if it is more , it need to go back
        playerWin(whichPlayer)
        return
    elif(variable_file.game_verson == 1 and (player_number >= 25 and howLong >= 0)): #Default version of the game
        playerWin(whichPlayer)
        return

    if(variable_file.game_verson == 2 and howLong > 0): #Mocing backwards when it is extended version

        turtle_functions.swapGif(player_object)

        for x in range(howLong):
            howLong -= 1
            player_object.forward(-160)
            player_number -= 1
            time.sleep(0.2)

        else:
            turtle_functions.swapGif(player_object)




    for x in variable_file.ladders: #Check if player is on field with ladder / snake
        if(x[0] == player_number):

            if x[2] % 2 != 0 :
                player_object.goto(player_object.xcor() , player_object.ycor() + x[2] * 160)
                player_object.left(180)
                turtle_functions.swapGif(player_object)

                if(player_next_direction == 0):
                    player_next_direction = 1

                else:
                    player_next_direction = 0

                player_number = x[1]
            else:

                player_object.goto(player_object.xcor() , player_object.ycor() + x[2] * 160)
                player_number = x[1]


    #Store data
    if(whichPlayer == 1):

        variable_file.bull_object = player_object
        variable_file.bull_next_direction = player_next_direction
        variable_file.bull_number = player_number

    else:

        variable_file.cow_object = player_object
        variable_file.cow_next_direction = player_next_direction
        variable_file.cow_number = player_number

#Set dice object "Last roll: "
def setDice():
    variable_file.last_roll_text = dice_functions.extendedDiceFunctionality(variable_file.last_roll_text)

def mainLoop():
    #check if game is extended version - if yes , we don't need a loop to play it
    if(variable_file.game_verson == 2):

        variable_file.roll_a_dice , variable_file.next_roll_text = turtle_functions.drawExtendedItems(variable_file.roll_a_dice, variable_file.next_roll_text)
        variable_file.roll_a_dice.onclick(rollADice, 1)
        return


    
    #main loop of moving / rolling a divce in default version
    while True:

        if(variable_file.isFirstPlayer): #decide which player should move
            input("Player one will now roll a dice! Click anything to do this! ")
            dice_functions.setdiceAnimation(variable_file.dice) #fake "animation" of dice
            value = random.randrange(1, 7) #pick random number
            dice_functions.setDiceValue(variable_file.dice , value) #set value of the dice
            print("Player one rolled: " , value)
            movePlayer(1, value) #actual move of player's one sprite

        else: #player two move
            input("Player two will now roll a dice! Click anything to do this! ")
            dice_functions.setdiceAnimation(variable_file.dice)
            value = random.randrange(1, 7)
            dice_functions.setDiceValue(variable_file.dice, value)
            print("Player two rolled: ", value)
            movePlayer(2, value)

        #negate value to enable for player switch
        variable_file.isFirstPlayer = not variable_file.isFirstPlayer


def main():

    game_version() #pick version - "1" - normal game , "2" - extended of some of the functions

    setDice() #set dice object

    variable_file.bull_object, variable_file.cow_object = turtle_functions.drawBoard(variable_file.bull_object,variable_file.cow_object)  # draw board and draw player1, player2 objects - bull , cow
    variable_file.dice = dice_functions.drawDice(variable_file.dice) #draw dice which is located on the left side

    mainLoop() #main loop of the game


    turtle.done() #turtle done drawning , stop blocking thread


main()


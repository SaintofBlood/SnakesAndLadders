import turtle
import random
import time

def drawDice(dice): 

    #Draw dice object , and set default to "1"
    
    dice = turtle.Turtle()
    dice.penup()

    dice.shape("images/dice1.gif")
    dice.goto(-500,200)

    return dice

def setDiceValue(dice , value):

    #set desired dice look based on value


    dice.shape("images/dice" + str(value) + ".gif")

def setdiceAnimation(dice):

    #fake animation of the dice "rolling" effect

    for x in range(1, random.randrange(8, 15)) :
        time.sleep(0.1)
        setDiceValue(dice , random.randrange(1, 6))


######################EXTENDED VERSION FUNCTIONS######################

def extendedDiceFunctionality(last_dice_value_turtle):

    #last dice value after the dice gif itself

    last_dice_value_turtle = turtle.Turtle()

    last_dice_value_turtle.penup()

    last_dice_value_turtle.speed(0)

    last_dice_value_turtle.goto(-500, 130)

    last_dice_value_turtle.hideturtle()

    return last_dice_value_turtle
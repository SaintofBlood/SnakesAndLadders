import turtle

import variable_file

def loadSprites(): #load all sprites to the turtle library
    turtle.addshape("images/win.gif")
    turtle.addshape("images/ladder3.gif")
    turtle.addshape("images/ladder2.gif")
    turtle.addshape("images/ladder.gif")
    turtle.addshape("images/snake2.gif")
    turtle.addshape("images/snake3.gif")
    turtle.addshape("images/snake.gif")
    turtle.addshape("images/bull.gif")
    turtle.addshape("images/cow.gif")

    turtle.addshape("images/bull_rot.gif")
    turtle.addshape("images/cow_rot.gif")

    for x in range(1, 7):
        turtle.addshape("images/dice" + str(x) + ".gif"); #load all dice parts eg. dice1 , dice2 etc.

    #EXTENDED VERSION FILES

    turtle.addshape("images/roll_button.gif")
    turtle.addshape("images/button_no.gif")
    turtle.addshape("images/button_yes.gif")
    turtle.addshape("images/roll_button_unable.gif")


def drawGridNumber(drawBoardTurtle):

    #Draw numbers on the grid

    field_number = 0
    swap = False

    for x in range(0, 5):

        drawBoardTurtle.goto(-380, -280 + 160 * x)

        if (swap == True): #If swap , start from descending - used for detecting in which row we are . If the row is odd number , swap number and start from descending
            field_number += 5
            actual_v = field_number
            for i in range(1, 6): #draw one row
                drawBoardTurtle.write(field_number, align="center", font=("Arial", 25, "italic"))
                drawBoardTurtle.forward(160)
                field_number -= 1

            field_number = actual_v
            swap = False
        else:
            for i in range(1, 6):
                field_number += 1
                drawBoardTurtle.write(field_number, align="center", font=("Arial", 25, "italic"))
                drawBoardTurtle.forward(160)
            swap = True

    drawBoardTurtle.hideturtle()

def drawSprites(cow_object , bull_object):
    
    #draw players objects also including snakes and ladders
    
    ladder1 = turtle.Turtle();
    ladder1.penup()
    ladder1.shape("images/ladder.gif")
    ladder1.goto(0, 240)


    ladder2 = turtle.Turtle();
    ladder2.penup()
    ladder2.shape("images/ladder2.gif")
    ladder2.goto(-160, -80)

    ladder3 = turtle.Turtle();
    ladder3.penup()
    ladder3.shape("images/ladder3.gif")
    ladder3.goto(320 , -160)


    snake1 = turtle.Turtle();
    snake1.penup()

    snake1.shape("images/snake2.gif")
    snake1.goto(60, -240)

    snake2 = turtle.Turtle();
    snake2.penup()

    snake2.shape("images/snake3.gif")
    snake2.goto(-320, -80)

    snake3 = turtle.Turtle();
    snake3.penup()

    snake3.shape("images/snake.gif")
    snake3.goto(160 , 160)

    #player_one

    bull_object = turtle.Turtle();
    bull_object.penup()

    bull_object.shape("images/bull.gif")
    bull_object.goto(-320 , -350)

    #player_two

    cow_object = turtle.Turtle();
    cow_object.penup()


    cow_object.shape("images/cow.gif")
    cow_object.goto(-320 , -290)


    return cow_object , bull_object

BoardTest = 0

def drawBoard(cow_object , bull_object):

    #Draw all items inlcuding board itself

    loadSprites() #load .gif files

    screen_t = turtle.Screen()

    global BoardTest

    BoardTest = screen_t

    screen_t.title("Snakes and Ledders Board game [michal2010]")
    screen_t.setup(variable_file.screensize_x , variable_file.screensize_y , 0, 0)


    drawBoardTurtle = turtle.Turtle()
    drawBoardTurtle.speed(0)
    drawBoardTurtle.penup()

    drawBoardTurtle.goto(-400,-400)
    drawBoardTurtle.pendown()

    for i in range(4): #draw square
        drawBoardTurtle.forward(800)
        drawBoardTurtle.left(90)


    for i in range(1,5): #draw horizontal lines
        drawBoardTurtle.penup()
        drawBoardTurtle.goto(-400 , - 400 + 160 * i)
        drawBoardTurtle.pendown()
        drawBoardTurtle.forward(800)

    drawBoardTurtle.penup()
    drawBoardTurtle.goto(-240 , -400)
    drawBoardTurtle.left(90)
    drawBoardTurtle.pendown()

    for i in range(1,5): #draw vertical lines
        drawBoardTurtle.penup()
        drawBoardTurtle.goto(- 400 + 160 * i , - 400)
        drawBoardTurtle.pendown()
        drawBoardTurtle.forward(800)

    drawBoardTurtle.penup()
    drawBoardTurtle.goto(-400,-400)
    drawBoardTurtle.right(90)

    drawGridNumber(drawBoardTurtle)

    cow_object , bull_object = drawSprites(cow_object , bull_object) #draw snakes, ladders , bull and cow - players objects 


    return bull_object , cow_object

def End():
    BoardTest.mainloop()

def playerWin(whichPlayer):

    #Draw all objects which are shown after player won

    rectCors = ((-variable_file.screensize_y/2, -variable_file.screensize_x/2), (variable_file.screensize_y/2, -variable_file.screensize_x/2), (variable_file.screensize_y/2, variable_file.screensize_x/2) , (-variable_file.screensize_y/2, variable_file.screensize_x/2));
    turtle.register_shape('rectangle1', rectCors);

    variable_file.background_winBanner = turtle.Turtle()

    variable_file.background_winBanner.shape('rectangle1')
    variable_file.background_winBanner.fillcolor('white') #Create white rectangle which will hide all the object


    variable_file.is_cr_runn = True

    variable_file.winBanner = turtle.Turtle()
    variable_file.winBanner.shape("win.gif")
    variable_file.winBanner.penup()
    variable_file.winBanner.goto(0,150)

    if(variable_file.game_verson == 2): #If extended version , show buttons

        variable_file.which_player_won_text = turtle.Turtle()
        variable_file.which_player_won_text.penup()
        variable_file.which_player_won_text.hideturtle()
        variable_file.which_player_won_text.goto(0,400)
        variable_file.which_player_won_text.color("Green")

        if(whichPlayer == 1):
            variable_file.which_player_won_text.write("Player one won the game!", align="center",font=("Arial", 24, "bold"))
        else:
            variable_file.which_player_won_text.write("Player two won the game!", align="center",font=("Arial", 24, "bold"))

        variable_file.button_yes = turtle.Turtle()
        variable_file.button_yes.shape("images/button_yes.gif")
        variable_file.button_yes.penup()
        variable_file.button_yes.goto(128 ,-270)

        #variable_file.button_yes.onclick(RestartTheGame, 1)

        variable_file.button_no = turtle.Turtle()
        variable_file.button_no.shape("images/button_no.gif")
        variable_file.button_no.penup()
        variable_file.button_no.goto(-128 ,-270)

        #variable_file.button_no.onclick(ExitGame, 1)

        variable_file.button_nextgame = turtle.Turtle()
        variable_file.button_nextgame.penup()
        turtle.addshape("images/button_next.gif")
        variable_file.button_nextgame.shape("images/button_next.gif")
        variable_file.button_nextgame.goto(0 ,-200)

        variable_file.next_roll_text.clear()

        return

def hidePlayerWin():
    #Hide/reset fields/controls to default

    variable_file.winBanner.hideturtle()
    variable_file.background_winBanner.hideturtle()

    variable_file.bull_number = 1
    variable_file.cow_number = 1

    if variable_file.bull_next_direction == True:
        variable_file.bull_next_direction = False
        variable_file.bull_object.left(180)

    if variable_file.cow_next_direction == True:
        variable_file.cow_next_direction = False
        variable_file.cow_object.left(180)

    variable_file.bull_object.goto(-320, -350)
    variable_file.cow_object.goto(-320, -290)



######################EXTENDED VERSION FUNCTIONS######################


def RestartTheGame(x, y):

    # Button fucntion for reseting the game
    # Reset game to start state
    variable_file.is_cr_runn = False

    variable_file.background_winBanner.hideturtle()
    variable_file.button_no.hideturtle()
    variable_file.button_yes.hideturtle()
    variable_file.button_nextgame.hideturtle()
    variable_file.winBanner.hideturtle()
    variable_file.which_player_won_text.clear()

    variable_file.bull_number = 1
    variable_file.cow_number = 1

    if variable_file.bull_next_direction == True:
        variable_file.bull_next_direction = False
        variable_file.bull_object.left(180)

    if variable_file.cow_next_direction == True:
        variable_file.cow_next_direction = False
        variable_file.cow_object.left(180)

    variable_file.bull_object.goto(-320, -350)
    variable_file.cow_object.goto(-320, -290)

    variable_file.isFirstPlayer = True
    variable_file.last_roll_text.clear()

    variable_file.next_roll_text.clear()
    variable_file.next_roll_text.write("Player one will roll a dice now !", align="center",
                                       font=("Arial", 18, "italic"))

    variable_file.bull_object.shape("images/bull.gif")
    variable_file.cow_object.shape("images/cow.gif")

def drawExtendedItems(roll_button , who_will_roll_now ):

    #Draw all text and other items

    roll_button = turtle.Turtle()

    roll_button.penup()

    roll_button.shape("images/roll_button.gif")
    roll_button.goto(-500, 270)

    who_will_roll_now = turtle.Turtle()

    who_will_roll_now.penup()
    who_will_roll_now.goto(0, 420)

    who_will_roll_now.write("Player one will roll a dice now !", align="center", font=("Arial", 18, "italic"))

    who_will_roll_now.hideturtle()

    return roll_button , who_will_roll_now

def swapGif(playerObject):

    if(variable_file.game_verson != 2): #Don't rotate when it is not an extended version of the game
        return

    #swap gifs for the "rotated" version (_rot)

    if("_rot" in playerObject.shape()):
        playerObject.shape(playerObject.shape().replace("_rot" , ""))
    else:
        playerObject.shape(playerObject.shape().replace(".gif", "") + "_rot.gif")

    return  playerObject
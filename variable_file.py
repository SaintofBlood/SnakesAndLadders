#file stores all the variables used in the game

#snakes and ladder table
ladders = [ [5,15, 2] , [9,12 , 1] , [18,23 , 1] , [8 , 3 , -1] , [20 , 1 , -3 ] , [24, 14 , -2]] #[x,y,z] x <- starting field , y <- target field , z <- how many rows should it move (e.g top or bottom)

#Bull (Player One)

bull_number = 1 #Actual field number on which player is standing
bull_object = "" #Turtle object
bull_next_direction = False #False - don't swap values, True - rotate player's object . Use to move between rows

#Cow (Player Two)
cow_number = 1 #Same as abowe with bull
cow_object = "" #Same as abowe with bull
cow_next_direction = False #Same as abowe with bull

#Dice object
dice = 0



isFirstPlayer = True  #Which player should move now ?


winBanner = 0 #WinnBanner
background_winBanner = 0

screensize_x = 1200
screensize_y = 1000

######################EXTENDED VERSION VAIRABLES######################

game_verson = 0 #If 1 - normal game , if 2 - extended version

#Extended buttons
button_yes = 0 #Turtle's button object (Image)
button_no = 0 #Turtle's button object (Image)
button_nextgame = 0 #Turtle's button object (Image)
roll_a_dice = 0 #Turtle's button object (Image)

#Extended text objects
next_roll_text = 0 #Turtle's button object (Text)
last_roll_text = 0 #Turtle's button object (Text)
which_player_won_text = 0 #Turtle's text object (Text)

#CheckIfFucntionIsExecuting
is_cr_runn  = False #Used to disable / enable roll button

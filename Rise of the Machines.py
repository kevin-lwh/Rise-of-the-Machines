##################################
##    RISE OF THE MACHINES      ##
##                              ##
##       BY: KEVIN HUANG        ##
##################################

#imports
from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
s = Canvas(root, width=1000, height=1000, background="white")


#set initial values
def setInitialValues():
    #global variables
    global playerA, playerA_x, playerA_y, playerA_xSpeed, playerA_ySpeed, playerB_ySpeed, playerB, playerB_x, playerB_y, playerB_xSpeed, playerB_ySpeed
    global currentScore_A, currentScore_B, playerA_currentDirection, playerA_front, playerA_left, playerA_right, playerA_back
    global playerA_size, playerB_currentDirection, playerB_front, playerB_left, playerB_right, playerB_back, playerB_size, coinA, coinA_x, coinA_y
    global coin_size, coinA_num, coinA_speed, coin, coinA_yGap, coinA_yGapMultiplier, coinA_yCurrent, floor_image, coinB, coinB_x, coinB_y
    global coinB_num, coinB_speed, coinB_yGap, coinB_yGapMultiplier, coinB_yCurrent, currentLive_A, currentLive_B, playerA_fired, playerA_hit
    global bulletA ,bulletB, bulletA_xspeed, bulletB_xspeed, bulletB_yspeed, bulletA_x, bulletA_y, bulletB_x, bulletB_y,currentAmmo_A
    global bulletA_yspeed, currentAmmo_B, bullet_up, bullet_down, bullet_left, bullet_right,bulletA_direction, bulletB_direction, playerB_fired
    global rock1, rock_size, rockA, rockA_x, rockA_y, rockA_num, rockA_speed, rockA_yGap, rockA_yCurrent, liveB, liveA, playerB_hit
    global rockA_yGapMultiplier, floor_speed, floor_x, floor_y, rockB, rockB_x, rockB_y, rockB_num, rockB_speed, rockB_yGap
    global rockB_yGapMultiplier, rockB_yCurrent,  border_image, border_y, border_speed, rock2, rock3, rock4, rockA_type, rockB_type
    global enemyA, enemyA_x, enemyA_y, enemyA_num, enemyA_speed, enemyA_yGap, enemyA_yGapMultiplier, enemyA_yCurrent, enemy1, enemy_sizeVer, enemy_sizeHor
    global enemyB, enemyB_x, enemyB_y, enemyB_num, enemyB_speed, enemyB_yGap, enemyB_yGapMultiplier, enemyB_yCurrent, enemy2, enemyA_type, enemyB_type
    global enemyContact_A, enemyContact_B, gameTime, timeStart,timer,gameLength,e, playerA_victory_img, playerB_victory_img, draw_img
    global ammosA, ammosA_x, ammosA_y, ammos_size, ammosA_num, ammosA_speed, ammosA_yGap, ammosA_yGapMultiplier, cammosA_yCurrent
    global ammosB, ammosB_x, ammosB_y, ammosB_num, ammosB_speed, ammosB_yGap, ammosB_yGapMultiplier, cammosB_yCurrent, ammoCrate
    global playerA_frontHit, playerA_backHit, playerA_leftHit, playerA_rightHit, playerB_frontHit, playerB_backHit, playerB_leftHit, playerB_rightHit
   

    ### PLAYER A INITIAL VALUES ###
    playerA = 0
    playerA_x = 250
    playerA_y = 800
    playerA_xSpeed = 0
    playerA_ySpeed = 0
    currentScore_A = 0
    playerA_currentDirection = "front"
    playerA_front = PhotoImage(file = "pic/playerA_front.gif")
    playerA_left = PhotoImage(file = "pic/playerA_left.gif")
    playerA_right = PhotoImage(file = "pic/playerA_right.gif")
    playerA_back = PhotoImage(file = "pic/playerA_back.gif")
    playerA_frontHit = PhotoImage(file = "pic/playerA_frontHit.gif")
    playerA_leftHit = PhotoImage(file = "pic/playerA_leftHit.gif")
    playerA_rightHit = PhotoImage(file = "pic/playerA_rightHit.gif")
    playerA_backHit = PhotoImage(file = "pic/playerA_backHit.gif")
    playerA_size = 32
    bullet_up = PhotoImage(file = "pic/bullet_up.gif")
    bullet_down = PhotoImage(file = "pic/bullet_down.gif")
    bullet_left = PhotoImage(file = "pic/bullet_left.gif")
    bullet_right = PhotoImage(file = "pic/bullet_right.gif")
    bulletA_direction = []
    bulletA = []
    bulletA_xspeed = []
    bulletA_yspeed = []
    bulletA_x = []
    bulletA_y = []
    playerA_fired = 0
    playerA_hit = 0
    if gameDif == "easy":
        currentLive_A = 4
        currentAmmo_A = 25
    elif gameDif == "normal":
        currentLive_A = 3
        currentAmmo_A = 15
    elif gameDif == "hard":
        currentLive_A = 2
        currentAmmo_A = 5
    enemyContact_A = False

    ### PLAYER B INITIAL VALUES ###
    playerB = 0
    playerB_x = 750
    playerB_y = 800
    playerB_xSpeed = 0
    playerB_ySpeed = 0
    currentScore_B = 0
    playerB_currentDirection = "front"
    playerB_front = PhotoImage(file = "pic/playerB_front.gif")
    playerB_left = PhotoImage(file = "pic/playerB_left.gif")
    playerB_right = PhotoImage(file = "pic/playerB_right.gif")
    playerB_back = PhotoImage(file = "pic/playerB_back.gif")
    playerB_frontHit = PhotoImage(file = "pic/playerB_frontHit.gif")
    playerB_leftHit = PhotoImage(file = "pic/playerB_leftHit.gif")
    playerB_rightHit = PhotoImage(file = "pic/playerB_rightHit.gif")
    playerB_backHit = PhotoImage(file = "pic/playerB_backHit.gif")
    playerB_size = 32
    bulletB_direction = []
    bulletB = []
    bulletB_xspeed = []
    bulletB_yspeed = []
    bulletB_x = []
    bulletB_y = []
    playerB_fired = 0
    playerB_hit = 0 
    if gameDif == "easy":
        currentLive_B = 4
        currentAmmo_B = 25
    elif gameDif == "normal":
        currentLive_B = 3
        currentAmmo_B = 15
    elif gameDif == "hard":
        currentLive_B = 2
        currentAmmo_B = 5
    enemyContact_B = False

    ### ENEMY ###
    enemy1 = PhotoImage(file = "pic/enemy1.gif")
    enemy2 = PhotoImage(file = "pic/enemy2.gif")
    enemy_sizeVer = 39
    enemy_sizeHor = 30

    #enemy for player A
    enemyA = []
    enemyA_x = []
    enemyA_y = []
    enemyA_num = 15
    if gameDif == "easy":
        enemyA_speed = 5
    elif gameDif == "normal":
        enemyA_speed = 6
    elif gameDif == "hard":
        enemyA_speed = 7
    enemyA_yGap = 0
    enemyA_yCurrent = 0
    for i in range(enemyA_num):
        enemyA_x.append(randint(15,475))
        enemyA_yGaoMultiplier = choice([2,3])
        enemyA_yGap = -100 * enemyA_yGaoMultiplier #always 200,300 pixels gap between each enemy
        enemyA_yCurrent += enemyA_yGap #the latest enemy y position
        enemyA_y.append(enemyA_yCurrent)
        enemyA.append(0)


    #enemy for player B
    enemyB = []
    enemyB_x = []
    enemyB_y = []
    enemyB_num = 15
    if gameDif == "easy":
        enemyB_speed = 5
    elif gameDif == "normal":
        enemyB_speed = 6
    elif gameDif == "hard":
        enemyB_speed = 7
    enemyB_yGap = 0
    enemyB_yCurrent = 0
    for i in range(enemyB_num):
        enemyB_x.append(randint(545,985))
        enemyB_yGaoMultiplier = choice([2,3])
        enemyB_yGap = -100 * enemyB_yGaoMultiplier #always 200,300 pixels gap between each enemy
        enemyB_yCurrent += enemyB_yGap #the latest enemy y position
        enemyB_y.append(enemyB_yCurrent)
        enemyB.append(0)
    

    ### ROCKS ###
    rock1 = PhotoImage(file = "pic/rock1.gif")
    rock2 = PhotoImage(file = "pic/rock2.gif")
    rock3 = PhotoImage(file = "pic/rock3.gif")
    rock4 = PhotoImage(file = "pic/rock4.gif")
    
    rock_size = 25

    #rocks for player A
    rockA = []
    rockA_x = []
    rockA_y = []
    rockA_num = 15
    if gameDif == "easy":
        rockA_speed = 4
    elif gameDif == "normal":
        rockA_speed = 5
    elif gameDif == "hard":
        rockA_speed = 6
    rockA_yGap = 0
    rockA_yCurrent = 0
    rockA_type = []
    for i in range(rockA_num):
        rockA_x.append(randint(15,475))
        rockA_yGapMultiplier = choice([1,1,1,2]) 
        rockA_yGap = -100 * rockA_yGapMultiplier #always 100,200 pixels gap between each rock
        rockA_yCurrent += rockA_yGap #the latest rock y position
        rockA_y.append(rockA_yCurrent)
        rockA.append(0)
        rockA_type.append(choice(["rock1","rock1","rock1","rock1","rock2","rock2","rock2","rock3","rock3","rock4"]))

    #rocks for player B
    rockB = []
    rockB_x = []
    rockB_y = []
    rockB_num = 15
    if gameDif == "easy":
        rockB_speed = 4
    elif gameDif == "normal":
        rockB_speed = 5
    elif gameDif == "hard":
        rockB_speed = 6
    rockB_yGap = 0
    rockB_yCurrent = 0
    rockB_type = []
    for i in range(rockB_num):
        rockB_x.append(randint(525,985))
        rockB_yGapMultiplier = choice([1,1,1,2])
        rockB_yGap = -100 * rockB_yGapMultiplier #always 100,200 pixels gap between each rock
        rockB_yCurrent += rockB_yGap #the latest rock y position
        rockB_y.append(rockB_yCurrent)
        rockB.append(0)
        rockB_type.append(choice(["rock1","rock1","rock1","rock1","rock2","rock2","rock2","rock3","rock3","rock4"]))

        
    ### COINS ###
    coin = PhotoImage(file = "pic/coin.gif")
    coin_size = 15

    #coin for player A
    coinA = []
    coinA_x = []
    coinA_y = []
    coinA_num = 15
    if gameDif == "easy":
        coinA_speed = 4
    elif gameDif == "normal":
        coinA_speed = 5
    elif gameDif == "hard":
        coinA_speed = 6
    coinA_yGap = 0
    coinA_yCurrent = -450
    for i in range(coinA_num):
        coinA_x.append(randint(15,475))
        coinA_yGapMultiplier = choice([1,1,2,3]) 
        coinA_yGap = -100 * coinA_yGapMultiplier #always 100,200,300 pixels gap between each coin
        coinA_yCurrent += coinA_yGap #the latest coin y position
        coinA_y.append(coinA_yCurrent)
        coinA.append(0)

    #coin for player B
    coinB = []
    coinB_x = []
    coinB_y = []
    coinB_num = 15
    if gameDif == "easy":
        coinB_speed = 4
    elif gameDif == "normal":
        coinB_speed = 5
    elif gameDif == "hard":
        coinB_speed = 6
    coinB_yGap = 0
    coinB_yCurrent = -450
    for i in range(coinB_num):
        coinB_x.append(randint(525,985))
        coinB_yGapMultiplier = choice([1,1,2,3])
        coinB_yGap = -100 * coinB_yGapMultiplier #always 100,200,300 pixels gap between each coin
        coinB_yCurrent += coinB_yGap #the latest coin y position
        coinB_y.append(coinB_yCurrent)
        coinB.append(0)

    ### AMMOS ###
    ammos_size = 25
    ammoCrate = PhotoImage(file = "pic/ammoCrate.gif")
    
    #ammos for player A
    ammosA = []
    ammosA_x = []
    ammosA_y = []
    ammosA_num = 3
    if gameDif == "easy":
        ammosA_speed = 4
    elif gameDif == "normal":
        ammosA_speed = 5
    elif gameDif == "hard":
        ammosA_speed = 6
    ammosA_yGap = 0
    ammosA_yCurrent = -1500
    for i in range(ammosA_num):
        ammosA_x.append(randint(15,475))
        ammosA_yGapMultiplier = choice([5,6])
        ammosA_yGap = -500 * ammosA_yGapMultiplier #always 2500,3000 pixels gap between each ammo crate
        ammosA_yCurrent += ammosA_yGap #the latest ammo crate y position
        ammosA_y.append(ammosA_yCurrent)
        ammosA.append(0)

    #ammos for player B
    ammosB = []
    ammosB_x = []
    ammosB_y = []
    ammosB_num = 3
    if gameDif == "easy":
        ammosB_speed = 4
    elif gameDif == "normal":
        ammosB_speed = 5
    elif gameDif == "hard":
        ammosB_speed = 6
    ammosB_yGap = 0
    ammosB_yCurrent = -1500
    for i in range(ammosA_num):
        ammosB_x.append(randint(525,985))
        ammosB_yGapMultiplier = choice([5,6])
        ammosB_yGap = -500 * ammosB_yGapMultiplier #always 2500,3000 pixels gap between each ammo crate
        ammosB_yCurrent += ammosB_yGap #the latest ammo crate y position
        ammosB_y.append(ammosB_yCurrent)
        ammosB.append(0)
    
        
    ### GAME INFORMATION ###
    scoreA = 0
    scoreB = 0
    timer = 0
    liveA = 0
    liveB = 0
    gameTime = 0
    timeStart = time()
    gameLength = 60
    playerA_victory_img = PhotoImage(file = "pic/PLAYERAWINS.gif")
    playerB_victory_img = PhotoImage(file = "pic/PLAYERBWINS.gif")
    draw_img = PhotoImage(file = "pic/DRAW.gif")
        
    
    ### FLOOR ###
    floor_image = PhotoImage(file = "pic/floor2.gif")
    if gameDif == "easy":
        floor_speed = 4
    elif gameDif == "normal":
        floor_speed = 5
    elif gameDif == "hard":
        floor_speed = 6
    floor_x = 500
    floor_y = 500

    ### BORDER ###
    border_image = PhotoImage(file = "pic/border.gif")
    border_y = 500
    if gameDif == "easy":
        border_speed = 4
    elif gameDif == "normal":
        border_speed = 5
    elif gameDif == "hard":
        border_speed = 6


#update game information
def updateInformation():
    global scoreA, scoreB, timer, ammoA, ammoB, liveA, liveB,currentTime1,currentTime2
    
    #score
    scoreA = s.create_text(50,50, text = "score = " + str(currentScore_A), fill = "white", font = "times 16")
    scoreB = s.create_text(580,50, text = "score = " + str(currentScore_B), fill = "white", font = "times 16")

    #TIMER
    currentTime1 = int((gameLength - gameTime)/60)
    currentTime2 = (gameLength-gameTime)%60
    if currentTime2 == 0:
        timer = s.create_text(495,50, text =  str(currentTime1)+" : "+str(currentTime2)+"0", fill = "white", font = "times 20")
    elif currentTime2 < 10:
        timer = s.create_text(495,50, text =  str(currentTime1)+" : "+"0"+str(currentTime2), fill = "white", font = "times 20")
    else:
        timer = s.create_text(495,50, text =  str(currentTime1)+" : "+str(currentTime2), fill = "white", font = "times 20")

    #ammo
    ammoA = s.create_text(245,50, text =  "AMMO: " + str(currentAmmo_A), fill = "white", font = "times 16")
    ammoB = s.create_text(765,50, text =  "AMMO: " + str(currentAmmo_B), fill = "white", font = "times 16")

    #lives
    liveA = s.create_text(400,50, text =  "LIVES: " + str(currentLive_A), fill = "white", font = "times 16")
    liveB = s.create_text(900,50, text =  "LIVES: " + str(currentLive_B), fill = "white", font = "times 16")
    
def drawObjects():
    global playerA,playerB, coin, floor, border

    #FLOOR
    floor = s.create_image(floor_x, floor_y, image = floor_image)

    #BORDER
    border = s.create_image(500,border_y,image = border_image)
   
    #PLAYER A
    if enemyContact_A == True: #if the player touched the enemy

        #four different directions
        if playerA_currentDirection == "front": 
            if t % 6 == 0 or t % 6 == 1 or t % 6 == 2: #every 3 frames it switch between two pictures to create flash effect
                playerA = s.create_image(playerA_x, playerA_y, image = playerA_front)
            elif t % 6 == 3 or t % 6 == 4 or t % 6 == 5:
                playerA = s.create_image(playerA_x, playerA_y, image = playerA_frontHit)

        elif playerA_currentDirection == "back":
            if t % 6 == 0 or t % 6 == 1 or t % 6 == 2:
                playerA = s.create_image(playerA_x, playerA_y, image = playerA_back)
            elif t % 6 == 3 or t % 6 == 4 or t % 6 == 5:
                playerA = s.create_image(playerA_x, playerA_y, image = playerA_backHit)

        elif playerA_currentDirection == "left":
            if t % 6 == 0 or t % 6 == 1 or t % 6 == 2:
                playerA = s.create_image(playerA_x, playerA_y, image = playerA_left)
            elif t % 6 == 3 or t % 6 == 4 or t % 6 == 5:
                playerA = s.create_image(playerA_x, playerA_y, image = playerA_leftHit)

        elif playerA_currentDirection == "right":
            if t % 6 == 0 or t % 6 == 1 or t % 6 == 2:
                playerA = s.create_image(playerA_x, playerA_y, image = playerA_right)
            elif t % 6 == 3 or t % 6 == 4 or t % 6 == 5:
                playerA = s.create_image(playerA_x, playerA_y, image = playerA_rightHit)

    #the player is not touching enemy
    else:
        if playerA_currentDirection == "front":
            playerA = s.create_image(playerA_x, playerA_y, image = playerA_front)
        elif playerA_currentDirection == "left":
            playerA = s.create_image(playerA_x, playerA_y, image = playerA_left)
        elif playerA_currentDirection == "right":
            playerA = s.create_image(playerA_x, playerA_y, image = playerA_right)
        elif playerA_currentDirection == "back":
            playerA = s.create_image(playerA_x, playerA_y, image = playerA_back)
   
   #PLAYER B
    if enemyContact_B == True:#if the player touched the enemy

        #four different directions
        if playerB_currentDirection == "front":
            if t % 6 == 0 or t % 6 == 1 or t % 6 == 2: #every 3 frames it switch between two pictures to create flash effect
                playerB = s.create_image(playerB_x, playerB_y, image = playerB_front)
            elif t % 6 == 3 or t % 6 == 4 or t % 6 == 5:
                playerB = s.create_image(playerB_x, playerB_y, image = playerB_frontHit)

        elif playerB_currentDirection == "back":
            if t % 6 == 0 or t % 6 == 1 or t % 6 == 2:
                playerB = s.create_image(playerB_x, playerB_y, image = playerB_back)
            elif t % 6 == 3 or t % 6 == 4 or t % 6 == 5:
                playerB = s.create_image(playerB_x, playerB_y, image = playerB_backHit)

        elif playerB_currentDirection == "left":
            if t % 6 == 0 or t % 6 == 1 or t % 6 == 2:
                playerB = s.create_image(playerB_x, playerB_y, image = playerB_left)
            elif t % 6 == 3 or t % 6 == 4 or t % 6 == 5:
                playerB = s.create_image(playerB_x, playerB_y, image = playerB_leftHit)

        elif playerB_currentDirection == "right":
            if t % 6 == 0 or t % 6 == 1 or t % 6 == 2:
                playerB = s.create_image(playerB_x, playerB_y, image = playerB_right)
            elif t % 6 == 3 or t % 6 == 4 or t % 6 == 5:
                playerB = s.create_image(playerB_x, playerB_y, image = playerB_rightHit)
                
    #the player is not touching enemy
    else:     
        if playerB_currentDirection == "front":
            playerB = s.create_image(playerB_x, playerB_y, image = playerB_front)
        elif playerB_currentDirection == "left":
            playerB = s.create_image(playerB_x, playerB_y, image = playerB_left)
        elif playerB_currentDirection == "right":
            playerB = s.create_image(playerB_x, playerB_y, image = playerB_right)
        elif playerB_currentDirection == "back":
            playerB = s.create_image(playerB_x, playerB_y, image = playerB_back)


    #COIN
    for i in range(coinA_num):
        coinA[i] = s.create_image(coinA_x[i], coinA_y[i], image = coin)
    for i in range(coinB_num):
        coinB[i] = s.create_image(coinB_x[i], coinB_y[i], image = coin)

    #AMMOS
    for i in range(ammosA_num):
        for z in range(rockA_num):
            while sqrt((ammosA_x[i] - rockA_x[z])**2 + (ammosA_y[i] - rockA_y[z])**2) <= ammos_size + rock_size:
                  
                #if the ammo crate is on top of the rock, move it to the side
                if ammosA_x[i] <= rockA_x[z]:
                    ammosA_x[i] -= 1   
                elif ammosA_x[i] >= rockA_x[z]:
                    ammosA_x[i] += 1
                    
        ammosA[i] = s.create_image(ammosA_x[i],ammosA_y[i], image = ammoCrate)
        
    for i in range(ammosB_num):
        for z in range(rockB_num):
            while sqrt((ammosB_x[i] - rockB_x[z])**2 + (ammosB_y[i] - rockB_y[z])**2) <= ammos_size + rock_size:
                  
                #if the ammo crate is on top of the rock, move it to the side
                if ammosB_x[i] <= rockB_x[z]:
                    ammosB_x[i] -= 1   
                elif ammosB_x[i] >= rockB_x[z]:
                    ammosB_x[i] += 1
                    
        ammosB[i] = s.create_image(ammosB_x[i],ammosB_y[i], image = ammoCrate)
        
    #ROCKS
    for i in range(rockA_num):
        if rockA_type[i] == "rock1":
            rockA[i] = s.create_image(rockA_x[i], rockA_y[i], image = rock1)
        elif rockA_type[i] == "rock2":
            rockA[i] = s.create_image(rockA_x[i], rockA_y[i], image = rock2)
        elif rockA_type[i] == "rock3":
            rockA[i] = s.create_image(rockA_x[i], rockA_y[i], image = rock3)
        elif rockA_type[i] == "rock4":
            rockA[i] = s.create_image(rockA_x[i], rockA_y[i], image = rock4)
        
    for i in range(rockB_num):
        if rockB_type[i] == "rock1":
            rockB[i] = s.create_image(rockB_x[i], rockB_y[i], image = rock1)
        elif rockB_type[i] == "rock2":
            rockB[i] = s.create_image(rockB_x[i], rockB_y[i], image = rock2)
        elif rockB_type[i] == "rock3":
            rockB[i] = s.create_image(rockB_x[i], rockB_y[i], image = rock3)
        elif rockB_type[i] == "rock4":
            rockB[i] = s.create_image(rockB_x[i], rockB_y[i], image = rock4)

    #ENEMY
    for i in range(len(enemyA_x)):

        #make sure it doesn't collide with the rock
        for z in range(rockA_num):
            while sqrt((enemyA_x[i] - rockA_x[z])**2 + (enemyA_y[i] - rockA_y[z])**2) <= enemy_sizeHor + rock_size:
                  
                #if the enemy is on top of the rock, move it to the side
                if enemyA_x[i] <= rockA_x[z]:
                    enemyA_x[i] -= 1   
                elif enemyA_x[i] >= rockA_x[z]:
                    enemyA_x[i] += 1
                            
        enemyA[i] = s.create_image(enemyA_x[i], enemyA_y[i], image = enemy1)

        
    for i in range(enemyB_num):

        #make sure it doesn't collide with the rock
        for z in range(rockB_num):
            while sqrt((enemyB_x[i] - rockB_x[z])**2 + (enemyB_y[i] - rockB_y[z])**2) <= enemy_sizeHor + rock_size:

                #if the enemy is on top of the rock, move it to the side
                if enemyB_x[i] <= rockB_x[z]:
                    enemyB_x[i] -= 1  
                elif enemyB_x[i] >= rockB_x[z]:
                    enemyB_x[i] += 1
                
        enemyB[i] = s.create_image(enemyB_x[i], enemyB_y[i], image = enemy2)


    #BULLETS
    for i in range(len(bulletA_y)):
        
        #four directions
        if bulletA_direction[i] == "U":
            bulletA[i] = s.create_image(bulletA_x[i],bulletA_y[i],image = bullet_up)
        elif bulletA_direction[i] == "D":
            bulletA[i] = s.create_image(bulletA_x[i],bulletA_y[i],image = bullet_down)
        elif bulletA_direction[i] == "L":
            bulletA[i] = s.create_image(bulletA_x[i],bulletA_y[i],image = bullet_left)
        elif bulletA_direction[i] == "R":
            bulletA[i] = s.create_image(bulletA_x[i],bulletA_y[i],image = bullet_right)
        
    for i in range(len(bulletB_y)):
        
        #four directions
        if bulletB_direction[i] == "U":
            bulletB[i] = s.create_image(bulletB_x[i],bulletB_y[i],image = bullet_up)
        elif bulletB_direction[i] == "D":
            bulletB[i] = s.create_image(bulletB_x[i],bulletB_y[i],image = bullet_down)
        elif bulletB_direction[i] == "L":
            bulletB[i] = s.create_image(bulletB_x[i],bulletB_y[i],image = bullet_left)
        elif bulletB_direction[i] == "R":
            bulletB[i] = s.create_image(bulletB_x[i],bulletB_y[i],image = bullet_right)

    
#spawn player A bullets
def spawnBulletA():
    global bulletA_x, bulletA_y, bulletA, bulletA_yspeed, bulletA_xspeed,bulletA_direction,playerA_fired
    
    bulletA_x.append(playerA_x)
    bulletA_y.append(playerA_y)
    bulletA.append(0)
    playerA_fired += 1
    
    #bullet has different speed depending on the direction the player is facing
    if playerA_currentDirection == "back":
        bulletA_yspeed.append(-15)
        bulletA_xspeed.append(0)
        bulletA_direction.append("U")
    elif playerA_currentDirection == "front":
        bulletA_yspeed.append(15)
        bulletA_xspeed.append(0)
        bulletA_direction.append("D")
    elif playerA_currentDirection == "left":
        bulletA_yspeed.append(0)
        bulletA_xspeed.append(-15)
        bulletA_direction.append("L")
    elif playerA_currentDirection == "right":
        bulletA_yspeed.append(0)
        bulletA_xspeed.append(15)
        bulletA_direction.append("R")

#spawn player B bullets
def spawnBulletB():
    global bulletB_x, bulletB_y, bulletB, bulletB_yspeed, bulletB_xspeed,playerB_fired
    
    bulletB_x.append(playerB_x)
    bulletB_y.append(playerB_y)
    bulletB.append(0)
    playerB_fired += 1

    #bullet has different speed depending on the direction the player is facing
    if playerB_currentDirection == "back":
        bulletB_yspeed.append(-15)
        bulletB_xspeed.append(0)
        bulletB_direction.append("U")
    elif playerB_currentDirection == "front":
        bulletB_yspeed.append(15)
        bulletB_xspeed.append(0)
        bulletB_direction.append("D")
    elif playerB_currentDirection == "left":
        bulletB_yspeed.append(0)
        bulletB_xspeed.append(-15)
        bulletB_direction.append("L")
    elif playerB_currentDirection == "right":
        bulletB_yspeed.append(0)
        bulletB_xspeed.append(15)
        bulletB_direction.append("R")
        

def updateObjects():
    global playerA_x, playerA_y, playerB_x, playerB_y, playerA_xSpeed, coinA_y, bulletA_y, bulletA_x
    global bulletB_x, bulletB_y, floor_y, rockA_y, rockB_y, border_y, enemyA_y, enemyB_y, ammosA_y, ammosB_y

    #update player A
    playerA_x += playerA_xSpeed
    playerA_y += playerA_ySpeed

    #player A bullets
    for i in range(len(bulletA_y)):
        bulletA_y[i] += bulletA_yspeed[i]
        bulletA_x[i] += bulletA_xspeed[i]
        
    #update player B
    playerB_x += playerB_xSpeed
    playerB_y += playerB_ySpeed

    #player B bullets
    for i in range(len(bulletB_y)):
        bulletB_y[i] += bulletB_yspeed[i]
        bulletB_x[i] += bulletB_xspeed[i]

    #floor
    floor_y += floor_speed

    #border
    border_y += border_speed

    #update coins
    for i in range(coinA_num):
        coinA_y[i] += coinA_speed
    for i in range(coinB_num):
        coinB_y[i] += coinB_speed
        
    #update ammos
    for i in range(ammosA_num):
        ammosA_y[i] += ammosA_speed
    for i in range(ammosB_num):
        ammosB_y[i] += ammosB_speed

    #update rocks
    for i in range(rockA_num):
        rockA_y[i] += rockA_speed
    for i in range(rockB_num):
        rockB_y[i] += rockB_speed

    #update enemy
    for i in range(len(enemyA_x)):
        enemyA_y[i] += enemyA_speed
    for i in range(len(enemyB_x)):
        enemyB_y[i] += enemyB_speed
        
    
### DELETE FUNCTIONS ###
    
def deleteCoin():
    for i in range(coinA_num):
        s.delete(coinA[i])
    for i in range(coinB_num):
        s.delete(coinB[i])
        
def deleteAmmos():
    for i in range(ammosA_num):
        s.delete(ammosA[i])
    for i in range(ammosB_num):
        s.delete(ammosB[i])

def deleteRock():
    for i in range(rockA_num):
        s.delete(rockA[i])
    for i in range(rockB_num):
        s.delete(rockB[i])

def deleteEnemy():
    for i in range(enemyA_num):
        s.delete(enemyA[i])
    for i in range(enemyB_num):
        s.delete(enemyB[i])

def deleteBulletA():
    for i in range(len(bulletA)):
        s.delete(bulletA[i])
    for i in range(len(bulletB)):
        s.delete(bulletB[i])

def deleteBulletB():
    for i in range(len(bulletB)):
        s.delete(bulletB[i])


#check for collision between player and items
def checkForCollisions():
    global playerA_x, playerA_y, playerB_x, playerB_y, currentScore_A, coinA_x, coinA_y, coinA_num, coinA_yGapMultiplier, coinA_yGap
    global coinA_yCurrent, coinB_x, coinB_y, coinB_num, coinB_yGapMultiplier, coinB_yGap, coinB_yCurrent, currentScore_B, coinA_rotationCounter
    global coinB_rotationCounter, bulletA_x, bulletA_y, bulletA, bulletA_xspeed, bulletA_yspeed,floor_y, rockA_x, rockA_y,rockA_num, rockA_yGapMultiplier
    global rockA_yGap, rockA_yCurrent, rockB_x, rockB_y,rockB_num, rockB_yGapMultiplier, rockA_type, rockB_type, playerA_hit, playerB_hit
    global rockB_yGap, rockB_yCurrent, border_y, currentLive_A, currentLive_B , enemyContact_A, enemyContact_B
    global enemyA_x, enemyA_y,enemyA_num, enemyA_yGapMultiplier, enemyA_yGap, enemyA_yCurrent, enemyA_type, enemyA
    global enemyB_x, enemyB_y,enemyB_num, enemyB_yGapMultiplier, enemyB_yGap, enemyB_yCurrent, enemyB_type
    global ammosA_x, ammosA_y,ammosA_num, ammosA_yGapMultiplier, ammosA_yGap, ammosA_yCurrent,ammosA,currentAmmo_A
    global ammosB_x, ammosB_y,ammosB_num, ammosB_yGapMultiplier, ammosB_yGap, ammosB_yCurrent,ammosB,currentAmmo_B

    #keeps floor going
    if floor_y >= 928:
        floor_y = 500

    #keeps border going
    if border_y >= 945:
        border_y = 500

    #checks player A collisions, makes sure it doesn't leave its own side
    if playerA_x + playerA_size >= 490:
        playerA_x = 490 - playerA_size
        
    elif playerA_x - playerA_size <= 0:
        playerA_x = 0 + playerA_size

    if playerA_y + playerA_size >= 1000:
        playerA_y = 1000 - playerA_size

    elif playerA_y - playerA_size <= 0:
        playerA_y = 0 +playerA_size

    #checks player B collisions, makes sure it doesn't leave its own side
    if playerB_x - playerB_size <= 510:
        playerB_x = 510 + playerB_size

    elif playerB_x + playerB_size >= 1000:
        playerB_x = 1000 - playerB_size

    if playerB_y + playerB_size >= 1000:
        playerB_y = 1000 - playerB_size

    elif playerB_y - playerB_size <= 0:
        playerB_y = 0 +playerB_size

    #checks player A enemy collisions, makes sure it stays in screen
    for i in range(len(enemyA_x)):
        if enemyA_x[i] + enemy_sizeHor >= 490:
            enemyA_x[i] = 490 - enemy_sizeHor
            
        elif enemyA_x[i] - enemy_sizeHor <= 0:
            enemyA_x[i] = 0 + enemy_sizeHor

    #checks player B enemy collisions, makes sure it stays in screen
    for i in range(len(enemyB_x)):
        if enemyB_x[i] + enemy_sizeHor <= 510:
            enemyB_x[i] = 510 + enemy_sizeHor
            
        elif enemyB_x[i] - enemy_sizeHor >= 1000:
            enemyB_x[i] = 1000 - enemy_sizeHor

        

    #player A and coins
    i = 0
    while i < len(coinA_x):

        #delete the coin if player A touches the coin
        if sqrt((playerA_x - coinA_x[i])**2 + (playerA_y - coinA_y[i])**2) <= playerA_size + coin_size:
            currentScore_A += 5
            coinA_x.remove(coinA_x[i])
            coinA_y.remove(coinA_y[i])

            #adding new coins on top
            coinA_x.append(randint(15,475))
            coinA_yGapMultiplier = choice([1,1,2,3])
            coinA_yGap = -100 * coinA_yGapMultiplier #alwyas 100,200,300 pixel gap between each coin
            coinA_y.append(coinA_y[-1]+coinA_yGap) #the last coin y position plus the gap
            
            
            
        #delete the coin if the coin leaves the screen
        elif coinA_y[i] - coin_size >= 1000:
            coinA_x.remove(coinA_x[i])
            coinA_y.remove(coinA_y[i])

            #adding new coins on top
            coinA_x.append(randint(15,475))
            coinA_yGapMultiplier = choice([1,1,2,3])
            coinA_yGap = -100 * coinA_yGapMultiplier #alwyas 100,200,300 pixel gap between each coin
            coinA_y.append(coinA_y[-1]+coinA_yGap) #the last coin y position plus the gap
            
            
            
        else:
            i += 1

    #player A and ammo crate
    i = 0
    while i < len(ammosA_x):

        #delete the ammo crate if player A touches the ammo crate
        if sqrt((playerA_x - ammosA_x[i])**2 + (playerA_y - ammosA_y[i])**2) <= playerA_size + ammos_size:
            currentAmmo_A += 5
            ammosA_x.remove(ammosA_x[i])
            ammosA_y.remove(ammosA_y[i])

            #adding new ammo crate on top
            ammosA_x.append(randint(15,475))
            ammosA_yGapMultiplier = choice([5,6])
            ammosA_yGap = -500 * ammosA_yGapMultiplier #always 2500,3000, pixel gap between each ammo crate
            ammosA_y.append(ammosA_y[-1]+ammosA_yGap) #the last ammo crate y position plus the gap
            
            
            
        #delete the ammo crate if the ammo crate leaves the screen
        elif ammosA_y[i] - ammos_size >= 1000:
            ammosA_x.remove(ammosA_x[i])
            ammosA_y.remove(ammosA_y[i])

            #adding new ammo crate on top
            ammosA_x.append(randint(15,475))
            ammosA_yGapMultiplier = choice([5,6])
            ammosA_yGap = -500 * ammosA_yGapMultiplier #always 2500,3000, pixel gap between each ammo crate
            ammosA_y.append(ammosA_y[-1]+ammosA_yGap) #the last ammo crate y position plus the gap
            
            
            
        else:
            i += 1

    #player A and rocks
    i = 0
    while i <len(rockA_x):

        #delete the rock if it leaves the screen
        if rockA_y[i] - rock_size>= 1000:
            rockA_x.remove(rockA_x[i])
            rockA_y.remove(rockA_y[i])
            rockA_type.remove(rockA_type[i])

            #adding new rocks on top
            rockA_x.append(randint(15,475))
            rockA_yGapMultiplier = choice([1,1,1,2])
            rockA_yGap = -100 * rockA_yGapMultiplier #always 100,200 pixel gap between each rock
            rockA_y.append(rockA_y[-1]+rockA_yGap) #the last rock y position plus the gap
            rockA_type.append(choice(["rock1","rock1","rock1","rock1","rock2","rock2","rock2","rock3","rock3","rock4"]))
        

        #if player A touches the rock
        elif sqrt((playerA_x - rockA_x[i])**2 + (playerA_y - rockA_y[i])**2) <= playerA_size + rock_size:
            
            while sqrt((playerA_x - rockA_x[i])**2 + (playerA_y - rockA_y[i])**2) <= playerA_size + rock_size:
                if rockA_x[i] >= playerA_x:
                    playerA_x -= 1
                elif rockA_x[i] <= playerA_x:
                    playerA_x += 1
                    
        else:
            i += 1


    #player B and coins
    i = 0
    while i < len(coinB_x):

        #delete the coin if player B touches the coin
        if sqrt((playerB_x - coinB_x[i])**2 + (playerB_y - coinB_y[i])**2) <= playerB_size + coin_size:
            currentScore_B += 5
            coinB_x.remove(coinB_x[i])
            coinB_y.remove(coinB_y[i])
            


            #adding new coins on top
            coinB_x.append(randint(525,985))
            coinB_yGapMultiplier = choice([1,1,2,3])
            coinB_yGap = -100 * coinB_yGapMultiplier #alwyas 100,200,300 pixel gap between each coin
            coinB_y.append(coinB_y[-1]+coinB_yGap) #the last coin y position plus the gap
            

        #delete the coin if the coin leaves the screen
        elif coinB_y[i] - coin_size>= 1000:
            coinB_x.remove(coinB_x[i])
            coinB_y.remove(coinB_y[i])

            #adding new coins on top
            coinB_x.append(randint(525,985))
            coinB_yGapMultiplier = choice([1,1,2,3])
            coinB_yGap = -100 * coinB_yGapMultiplier #alwyas 100,200,300 pixel gap between each coin
            coinB_y.append(coinB_y[-1]+coinB_yGap) #the last coin y position plus the gap
            
        else:
            i += 1

    #player B and rocks
    i = 0
    while i <len(rockB_x):

        #delete the rock if the coin leaves the screen
        if rockB_y[i] - rock_size>= 1000:
            rockB_x.remove(rockB_x[i])
            rockB_y.remove(rockB_y[i])
            rockB_type.remove(rockB_type[i])

            #adding new rocks on top
            rockB_x.append(randint(525,985))
            rockB_yGapMultiplier = choice([1,1,1,2])
            rockB_yGap = -100 * rockB_yGapMultiplier #always 100,200 pixel gap between each rock
            rockB_y.append(rockB_y[-1]+rockB_yGap) #the last rock y position plus the gap
            rockB_type.append(choice(["rock1","rock1","rock1","rock1","rock2","rock2","rock2","rock3","rock3","rock4"]))
            

        #if player B touches the rock
        elif sqrt((playerB_x - rockB_x[i])**2 + (playerB_y - rockB_y[i])**2) <= playerB_size + rock_size:
            
            while sqrt((playerB_x - rockB_x[i])**2 + (playerB_y - rockB_y[i])**2) <= playerB_size + rock_size:
                if rockB_x[i] >= playerB_x:
                    playerB_x -= 1
                elif rockB_x[i] <= playerB_x:
                    playerB_x += 1
                    
        else:
            i += 1

    #player B and ammo crate
    i = 0
    while i < len(ammosB_x):

        #delete the ammo crate if player B touches the ammo crate
        if sqrt((playerB_x - ammosB_x[i])**2 + (playerB_y - ammosB_y[i])**2) <= playerB_size + ammos_size:
            currentAmmo_B += 5
            ammosB_x.remove(ammosB_x[i])
            ammosB_y.remove(ammosB_y[i])

            #adding new ammo crate on top
            ammosB_x.append(randint(525,985))
            ammosB_yGapMultiplier = choice([5,6])
            ammosB_yGap = -500 * ammosB_yGapMultiplier #always 2500,3000 pixel gap between each ammo crate
            ammosB_y.append(ammosB_y[-1]+ammosB_yGap) #the last ammo crate y postion plus the gap
            
            
            
        #delete the ammo crate if the ammo crate leaves the screen
        elif ammosB_y[i] - ammos_size >= 1000:
            ammosB_x.remove(ammosB_x[i])
            ammosB_y.remove(ammosB_y[i])

            #adding new ammo crate on top
            ammosB_x.append(randint(525,985))
            ammosB_yGapMultiplier = choice([5,6])
            ammosB_yGap = -500 * ammosB_yGapMultiplier #always 2500,3000 pixel gap between each ammo crate
            ammosB_y.append(ammosB_y[-1]+ammosB_yGap) #the last ammo crate y postion plus the gap
            
            
            
        else:
            i += 1

            

    ### PLAYER A BULLETS ###
    i = 0
    while i < len(bulletA_x):

        #remove the bullet if the bullet leaves the screen
        if bulletA_x[i] <= 0 or bulletA_x[i] >= 490 or bulletA_y[i] <= 0 or bulletA_y[i] >= 1000:
            bulletA_x.remove(bulletA_x[i])
            bulletA_y.remove(bulletA_y[i])
            bulletA.remove(bulletA[i])
            bulletA_xspeed.remove(bulletA_xspeed[i])
            bulletA_yspeed.remove(bulletA_yspeed[i])
            bulletA_direction.remove(bulletA_direction[i])

        else:
            i += 1

    #player A bullet and rocks
    i = 0
    while i < len(bulletA_x):
        
        #remove the bullet if it hits the rock
        for z in range(len(rockA_x)):
            if bulletA_direction[i] == "U" or bulletA_direction[i] == "D":
                if sqrt((bulletA_x[i] - rockA_x[z])**2 + (bulletA_y[i] - rockA_y[z])**2) <= 18 + rock_size:
                    bulletA_x.remove(bulletA_x[i])
                    bulletA_y.remove(bulletA_y[i])
                    bulletA.remove(bulletA[i])
                    bulletA_xspeed.remove(bulletA_xspeed[i])
                    bulletA_yspeed.remove(bulletA_yspeed[i])
                    bulletA_direction.remove(bulletA_direction[i])
                    break
            elif bulletA_direction[i] == "L" or bulletA_direction[i] == "R":
                if sqrt((bulletA_x[i] - rockA_x[z])**2 + (bulletA_y[i] - rockA_y[z])**2) <= 5 + rock_size:
                    bulletA_x.remove(bulletA_x[i])
                    bulletA_y.remove(bulletA_y[i])
                    bulletA.remove(bulletA[i])
                    bulletA_xspeed.remove(bulletA_xspeed[i])
                    bulletA_yspeed.remove(bulletA_yspeed[i])
                    bulletA_direction.remove(bulletA_direction[i])
                    break
        
        i += 1

    #player A bullet and enemy
    i = 0
    while i < len(bulletA_x):
        
        for z in range(len(enemyA_x)):
            if bulletA_direction[i] == "U" or bulletA_direction[i] == "D":
                if sqrt((bulletA_x[i] - enemyA_x[z])**2 + (bulletA_y[i] - enemyA_y[z])**2) <= 18 + enemy_sizeVer:

                    currentScore_A += 10
                    playerA_hit += 1

                    #remove the bullet
                    bulletA_x.remove(bulletA_x[i])
                    bulletA_y.remove(bulletA_y[i])
                    bulletA.remove(bulletA[i])
                    bulletA_xspeed.remove(bulletA_xspeed[i])
                    bulletA_yspeed.remove(bulletA_yspeed[i])
                    bulletA_direction.remove(bulletA_direction[i])
                    
                    #remove the enemy
                    enemyA_x.remove(enemyA_x[z])
                    enemyA_y.remove(enemyA_y[z])
            
                    #adding new enemy on top
                    enemyA_x.append(randint(15,475))
                    enemyA_yGapMultiplier = choice([2,3])
                    enemyA_yGap = -100 * enemyA_yGapMultiplier
                    enemyA_y.append(enemyA_y[-1]+enemyA_yGap)
   
                    
                    break
                
            elif bulletA_direction[i] == "L" or bulletA_direction[i] == "R":
                if sqrt((bulletA_x[i] - enemyA_x[z])**2 + (bulletA_y[i] - enemyA_y[z])**2) <= 5 + enemy_sizeHor:

                    currentScore_A += 10
                    playerA_hit += 1

                    #remove the bullet
                    bulletA_x.remove(bulletA_x[i])
                    bulletA_y.remove(bulletA_y[i])
                    bulletA.remove(bulletA[i])
                    bulletA_xspeed.remove(bulletA_xspeed[i])
                    bulletA_yspeed.remove(bulletA_yspeed[i])
                    bulletA_direction.remove(bulletA_direction[i])
                        
                    #remove the enemy
                    enemyA_x.remove(enemyA_x[z])
                    enemyA_y.remove(enemyA_y[z])
                    
                    #adding new enemy on top
                    enemyA_x.append(randint(15,475))
                    enemyA_yGapMultiplier = choice([2,3])
                    enemyA_yGap = -100 * enemyA_yGapMultiplier
                    enemyA_y.append(enemyA_y[-1]+enemyA_yGap)
                
                    
                    break
        
        i += 1
            

        

    ### PLAYER B BULLETS ###
    i = 0
    while i < len(bulletB_x):

        #if the bullet leaves the screen
        if bulletB_x[i] <= 510 or bulletB_x[i] >= 1000 or bulletB_y[i] <= 0 or bulletB_y[i] >= 1000:
            bulletB_x.remove(bulletB_x[i])
            bulletB_y.remove(bulletB_y[i])
            bulletB.remove(bulletB[i])
            bulletB_xspeed.remove(bulletB_xspeed[i])
            bulletB_yspeed.remove(bulletB_yspeed[i])
            bulletB_direction.remove(bulletB_direction[i])
        else:
            i += 1

    #player B bullet and rocks
    i = 0
    while i < len(bulletB_x):

        #remove the bullet if it hits the rock
        for z in range(len(rockB_x)):
            if bulletB_direction[i] == "U" or bulletB_direction[i] == "D":
                if sqrt((bulletB_x[i] - rockB_x[z])**2 + (bulletB_y[i] - rockB_y[z])**2) <= 18 + rock_size:
                    bulletB_x.remove(bulletB_x[i])
                    bulletB_y.remove(bulletB_y[i])
                    bulletB.remove(bulletB[i])
                    bulletB_xspeed.remove(bulletB_xspeed[i])
                    bulletB_yspeed.remove(bulletB_yspeed[i])
                    bulletB_direction.remove(bulletB_direction[i])
                    break
            elif bulletB_direction[i] == "L" or bulletB_direction[i] == "R":
                if sqrt((bulletB_x[i] - rockB_x[z])**2 + (bulletB_y[i] - rockB_y[z])**2) <= 5 + rock_size:
                    bulletB_x.remove(bulletB_x[i])
                    bulletB_y.remove(bulletB_y[i])
                    bulletB.remove(bulletB[i])
                    bulletB_xspeed.remove(bulletB_xspeed[i])
                    bulletB_yspeed.remove(bulletB_yspeed[i])
                    bulletB_direction.remove(bulletB_direction[i])
                    break
        i += 1

    #player B bullet and enemy
    i = 0
    while i < len(bulletB_x):
        
        for z in range(len(enemyB_x)):
            if bulletB_direction[i] == "U" or bulletB_direction[i] == "D":
                if sqrt((bulletB_x[i] - enemyB_x[z])**2 + (bulletB_y[i] - enemyB_y[z])**2) <= 18 + enemy_sizeVer:

                    currentScore_B += 10
                    playerB_hit += 1

                    #remove the bullet
                    bulletB_x.remove(bulletB_x[i])
                    bulletB_y.remove(bulletB_y[i])
                    bulletB.remove(bulletB[i])
                    bulletB_xspeed.remove(bulletB_xspeed[i])
                    bulletB_yspeed.remove(bulletB_yspeed[i])
                    bulletB_direction.remove(bulletB_direction[i])

                    #remove the enmey
                    enemyB_x.remove(enemyB_x[z])
                    enemyB_y.remove(enemyB_y[z])
            
                    #adding new enemy on top
                    enemyB_x.append(randint(545,985))
                    enemyB_yGapMultiplier = choice([2,3])
                    enemyB_yGap = -100 * enemyB_yGapMultiplier
                    enemyB_y.append(enemyB_y[-1]+enemyB_yGap)
                    
                    break
                
            elif bulletB_direction[i] == "L" or bulletB_direction[i] == "R":
                if sqrt((bulletB_x[i] - enemyB_x[z])**2 + (bulletB_y[i] - enemyB_y[z])**2) <= 5 + enemy_sizeHor:

                    currentScore_B += 10
                    playerB_hit += 1

                    #remove the bullet
                    bulletB_x.remove(bulletB_x[i])
                    bulletB_y.remove(bulletB_y[i])
                    bulletB.remove(bulletB[i])
                    bulletB_xspeed.remove(bulletB_xspeed[i])
                    bulletB_yspeed.remove(bulletB_yspeed[i])
                    bulletB_direction.remove(bulletB_direction[i])

                    #remove the enemy
                    enemyB_x.remove(enemyB_x[z])
                    enemyB_y.remove(enemyB_y[z])
            
                    #adding new enemy on top
                    enemyB_x.append(randint(545,985))
                    enemyB_yGapMultiplier = choice([2,3])
                    enemyB_yGap = -100 * enemyB_yGapMultiplier
                    enemyB_y.append(enemyB_y[-1]+enemyB_yGap)
                    
                    break
        i += 1

    #player A enemy
    i = 0
    while i <len(enemyA_x):

        #delete the enemy if it leaves the screen
        if enemyA_y[i] - enemy_sizeVer >= 1000:
            enemyA_x.remove(enemyA_x[i])
            enemyA_y.remove(enemyA_y[i])

            #adding new enemy on top
            enemyA_x.append(randint(15,475))
            enemyA_yGapMultiplier = choice([2,3])
            enemyA_yGap = -100 * enemyA_yGapMultiplier
            enemyA_y.append(enemyA_y[-1]+enemyA_yGap)
        else:
            i += 1

        

    #if player A touches the enemy
    if enemyContact_A == False:
        for i in range(enemyA_num):
            if sqrt((playerA_x - enemyA_x[i])**2 + (playerA_y - enemyA_y[i])**2) <= playerA_size + enemy_sizeHor and enemyContact_A == False:
                
                currentLive_A -= 1
                enemyContact_A = True
                break

    else:
        enemyContact_ANum = 0 #to keep track whether the player touched the enemy or not
        for i in range(enemyA_num):
            if sqrt((playerA_x - enemyA_x[i])**2 + (playerA_y - enemyA_y[i])**2) <= playerA_size + enemy_sizeHor:
                enemyContact_ANum += 1
        if enemyContact_ANum ==0:
            enemyContact_A = False
            

    #player B enemy
    i = 0
    while i <len(enemyB_x):

        #delete the enemy if it leaves the screen
        if enemyB_y[i] - enemy_sizeVer >= 1000:
            enemyB_x.remove(enemyB_x[i])
            enemyB_y.remove(enemyB_y[i])

            #adding new enemy on top
            enemyB_x.append(randint(545,985))
            enemyB_yGapMultiplier = choice([2,3])
            enemyB_yGap = -100 * enemyB_yGapMultiplier
            enemyB_y.append(enemyB_y[-1]+enemyB_yGap)
        else:
            i += 1
        

    #if player B touches the enemy

    if enemyContact_B == False:
        for i in range(enemyB_num):
            if sqrt((playerB_x - enemyB_x[i])**2 + (playerB_y - enemyB_y[i])**2) <= playerB_size + enemy_sizeHor and enemyContact_B == False:
 
                currentLive_B -= 1
                enemyContact_B = True
            
                break

    else:
        enemyContact_BNum = 0 #to keep track whether the player touched the enemy or not
        for i in range(enemyB_num):
            if sqrt((playerB_x - enemyB_x[i])**2 + (playerB_y - enemyB_y[i])**2) <= playerB_size + enemy_sizeHor:
                enemyContact_BNum += 1
        if enemyContact_BNum ==0:
            enemyContact_B = False
          
       
            
    
      
     
            

#key down handler
def keyDownHandler( event ):
    global playerA_xSpeed, playerA_ySpeed, playerB_xSpeed, playerB_ySpeed, playerA_currentDirection, playerB_currentDirection
    global playerA_fire, playerB_fire, bulletA_y, currentAmmo_A, currentAmmo_B

    ### PLAYER A CONTROL ###    
    if event.keysym == "a" or event.keysym == "A":   
        playerA_xSpeed = -5
        playerA_currentDirection = "left"
        
    elif event.keysym == "d" or event.keysym == "D":   
        playerA_xSpeed = 5
        playerA_currentDirection = "right"

    elif event.keysym == "w" or event.keysym == "W":   
        playerA_ySpeed = -5
        playerA_currentDirection = "back"

    elif event.keysym == "s" or event.keysym == "S":   
        playerA_ySpeed = 8
        playerA_currentDirection = "front"

    elif event.keysym == "f" or event.keysym == "F":
        if currentAmmo_A > 0:
            spawnBulletA()
            currentAmmo_A -= 1
        


    ### PLAYER B SPEED ###
    elif event.keysym == "Left":   
        playerB_xSpeed = -5
        playerB_currentDirection = "left"
            
    elif event.keysym == "Right":   
        playerB_xSpeed = 5
        playerB_currentDirection = "right"

    elif event.keysym == "Up":   
        playerB_ySpeed = -5
        playerB_currentDirection = "back"

    elif event.keysym == "Down":   
        playerB_ySpeed = 8
        playerB_currentDirection = "front"

    elif event.keysym == "slash":
        if currentAmmo_B > 0:
            spawnBulletB()
            currentAmmo_B -= 1
        

    
#individual key up handler to make the player control smoother
        
def keyUpHandler_W( event ):
    global playerA_ySpeed
    playerA_ySpeed = 0

def keyUpHandler_A( event ):
    global playerA_xSpeed
    playerA_xSpeed = 0

def keyUpHandler_S( event ):
    global playerA_ySpeed
    playerA_ySpeed = 0

def keyUpHandler_D( event ):
    global playerA_xSpeed
    playerA_xSpeed = 0

def keyUpHandler_Up( event ):
    global playerB_ySpeed
    playerB_ySpeed = 0

def keyUpHandler_Left( event ):
    global playerB_xSpeed
    playerB_xSpeed = 0

def keyUpHandler_Down( event ):
    global playerB_ySpeed
    playerB_ySpeed = 0

def keyUpHandler_Right( event ):
    global playerB_xSpeed
    playerB_xSpeed = 0

#mose click handler for intro screen and end game screen
def mouseClickHandler( event ):
    global xMouse, yMouse, gameMode, gameDif

    xMouse = event.x
    yMouse = event.y

    #intro screen
    if gameMode == "Intro":
        #play button
        if 378 <= xMouse <= 621:
            if 311 <=yMouse <= 354:
                gameMode = "Play"
                runGame()

        #difficulty button
        if 243 <= xMouse <= 757:
            if 478 <= yMouse <= 521:
                gameMode = "Difficulty"
                difficulty()

        #how to play button
        if 189 <= xMouse <= 811:
            if 644 <= yMouse <= 687:
                gameMode = "Instruction"
                instruction()

        #exist button
        if 62 <= xMouse <= 937:
            if 811 <= yMouse <= 854:
                root.destroy()

    #difficulty selection screen
    elif gameMode == "Difficulty":

        #normal button
        if 310 <= xMouse <= 690:
            if 478 <= yMouse <= 521:
                gameMode == "Intro"
                gameDif = "normal"
                introScreen()

        #easy button
        if 378 <= xMouse <= 621:
            if 228 <= yMouse <= 271:
                gameMode == "Intro"
                gameDif = "easy"
                introScreen()

        #hard button
        if 378 <= xMouse <= 621:
            if 728 <= yMouse <= 771:
                gameMode == "Intro"
                gameDif = "hard"
                introScreen()

    #how to play screen
    elif gameMode == "Instruction":

        #back button
        if 378 <= xMouse <= 621:
            if 878 <= yMouse <= 921:
                gameMode == "Intro"
                introScreen()

    #end game screen
    elif gameMode == "End":

        #retry button
        if 347 <= xMouse <= 652:
            if 378 <= yMouse <= 421:
                gameMode == "Play"
                runGame()

        #menu button
        if 372 <= xMouse <= 628:
            if 578 <= yMouse <= 621:
                gameMode == "Intro"
                introScreen()

        #exist button
        if 62 <= xMouse <= 937:
            if 778 <= yMouse <= 821:
                root.destroy()
                
        
         
### INTRO SCREEN INITIAL VALUES ###
playButton_img = PhotoImage(file = "pic/PLAY.gif")
difficultyButton_img = PhotoImage(file = "pic/DIFFICULTY.gif")
normalButton_img = PhotoImage(file = "pic/NORMAL.gif")
easyButton_img = PhotoImage(file = "pic/EASY.gif")
hardButton_img = PhotoImage(file = "pic/HARD.gif")
instructionButton_img = PhotoImage(file = "pic/INSTRUCTION.gif")
floor_image = PhotoImage(file = "pic/floor2.gif")
backButton_img = PhotoImage(file = "pic/BACK.gif")
retryButton_img = PhotoImage(file = "pic/RETRY.gif")
menuButton_img = PhotoImage(file = "pic/MENU.gif")
existButton_img = PhotoImage(file = "pic/EXIT.gif")
keyboardLayout_img = PhotoImage(file = "pic/keyboard.gif")
playerA_img = PhotoImage(file = "pic/playerA_front.gif")
playerB_img = PhotoImage(file = "pic/playerB_front.gif")
enemy1_img = PhotoImage(file = "pic/enemy1.gif")
enemy2_img = PhotoImage(file = "pic/enemy2.gif")
rock1_img = PhotoImage(file = "pic/rock1.gif")
coin_img = PhotoImage(file = "pic/coin.gif")
ammoCrate_img = PhotoImage(file = "pic/ammoCrate.gif")
clock_img = PhotoImage(file = "pic/clock.gif")
title_img = PhotoImage(file = "pic/TITLE.gif")
gameDif = "normal"
                

### INTRO SCREEN ###
def introScreen():
    global gameMode,playButton,difficultyButton,floor_intro,instructionButton,difficultyText,exitButton,title
    gameMode = "Intro"
    floor_intro = s.create_image(500,500,image = floor_image)
    playButton = s.create_image(500,333,image = playButton_img)
    difficultyButton = s.create_image(500,500,image = difficultyButton_img)
    difficultyText = s.create_text(500,550,text = "DIFFICULTY = " + gameDif, fill = "white", font = "times 16" )
    instructionButton = s.create_image(500,666,image = instructionButton_img)
    exitButton = s.create_image(500,833,image = existButton_img)
    title = s.create_image(500,166,image = title_img)


### DIFFICULTY SCREEN ###
def difficulty():
    s.delete(playButton,difficultyButton,instructionButton,difficultyText,exitButton,title)
    normalButton = s.create_image(500,500,image = normalButton_img)
    easyButton = s.create_image(500,250,image = easyButton_img)
    hardButton = s.create_image(500,750,image = hardButton_img)

    
### INSTRUCTION SCREEN ###
def instruction():
    s.delete(playButton,difficultyButton,instructionButton,difficultyText,exitButton,title)
    backButton = s.create_image(500,900,image = backButton_img)
    keyboardLayout = s.create_image(500,300,image = keyboardLayout_img)
    playerA_ins = s.create_image(250,50,image = playerA_img)
    playerA_text = s.create_text(250,100, text = "PLAYER A", fill = "white",font = "time 16")
    playerB_ins = s.create_image(750,50,image = playerB_img)
    playerB_text = s.create_text(750,100, text = "PLAYER B", fill = "white",font = "time 16")
    enemy1_ins = s.create_image(215,500,image = enemy1_img)
    enemy2_ins = s.create_image(285,500,image = enemy2_img)
    enemy_text1 = s.create_text(250,550, text = "Contact with enemy costs 1 life", fill = "white",font = "time 16")
    enemy_text2 = s.create_text(250,600, text = "Gain 10 points on each enemy kill", fill = "white",font = "time 16")
    coin_ins = s.create_image(250,650,image = coin_img)
    coin_text = s.create_text(250,700, text = "Each coin contains 5 points" , fill = "white",font = "time 16")
    rock_ins = s.create_image(750,500,image = rock1_img)
    rock_text = s.create_text(750,550, text = "Rock will push you to the side", fill = "white",font = "time 16")
    ammoCrate_ins = s.create_image(750,650, image = ammoCrate_img)
    ammoCrate_text = s.create_text(750,700, text = "Ammo Crate provides 5 ammos", fill = "white",font = "time 16")
    clock_ins = s.create_image(500,750,image = clock_img)
    clock_text = s.create_text(500,800, text = "You have 1 minute, try to get a higher score than the other player without dying!",fill = "white",font = "time 16")
    

### ENDGAME ###
def endGame():
    global gameMode, retryButton,menuButton
    gameMode = "End"

    #when the timer runs out
    if gameTime == 60:

        #compare score
        if currentScore_A > currentScore_B:
            s.create_image(500,200,image = playerA_victory_img)

        elif currentScore_A < currentScore_B:
            s.create_image(500,200,image = playerB_victory_img)

        elif currentScore_A == currentScore_B:
            s.create_image(500,200,image = draw_img)
        s.create_text(495,100, text = "TIME'S UP!", fill = "white", font = "times 20")

    #when player A loses all lives
    if currentLive_A == 0:
        s.create_image(500,200,image = playerB_victory_img)
        if currentTime2 < 10:
            s.create_text(495,50, text =  str(currentTime1)+" : "+"0"+str(currentTime2), fill = "white", font = "times 20")
        else:
            s.create_text(495,50, text =  str(currentTime1)+" : "+str(currentTime2), fill = "white", font = "times 20")

    #when player B loses all lives
    elif currentLive_B == 0:
        s.create_image(500,200,image = playerA_victory_img)
        if currentTime2 < 10:
            s.create_text(495,50, text =  str(currentTime1)+" : "+"0"+str(currentTime2), fill = "white", font = "times 20")
        else:
            s.create_text(495,50, text =  str(currentTime1)+" : "+str(currentTime2), fill = "white", font = "times 20")


    #print game information on the top
    s.create_text(50,50, text = "score = " + str(currentScore_A), fill = "white", font = "times 16")
    s.create_text(570,50, text = "score = " + str(currentScore_B), fill = "white", font = "times 16")
    s.create_text(570,50, text = "score = " + str(currentScore_B), fill = "white", font = "times 16")
    s.create_text(245,50, text =  "AMMO: " + str(currentAmmo_A), fill = "white", font = "times 16")
    s.create_text(765,50, text =  "AMMO: " + str(currentAmmo_B), fill = "white", font = "times 16")
    s.create_text(400,50, text =  "LIVES: " + str(currentLive_A), fill = "white", font = "times 16")
    s.create_text(900,50, text =  "LIVES: " + str(currentLive_B), fill = "white", font = "times 16")

    #accuracy calculation
    if playerA_fired == 0:
        s.create_text(250,120, text = "ACCURACY: %0.0", fill = "white", font = "times 16")
    else:
        s.create_text(250,120, text = "ACCURACY: %" + str(round((playerA_hit/playerA_fired)*100,2)), fill = "white", font = "times 16")
    if playerB_fired == 0:
        s.create_text(750,120, text = "ACCURACY: %0.0", fill = "white", font = "times 16")
    else:
        s.create_text(750,120, text = "ACCURACY: %" + str(round((playerB_hit/playerB_fired)*100,2)), fill = "white", font = "times 16")

    #endGame buttons
    retryButton = s.create_image(500,400,image = retryButton_img)
    menuButton = s.create_image(500,600,image = menuButton_img)
    exitButton = s.create_image(500,800,image = existButton_img)
    

    
### RUNGAME ###
def runGame():
    global gameTime, timeStart, t
    s.delete(playButton)
    setInitialValues()

    t = 0
    while True:
    
        #timer
        t += 1
        
        timeNow = time()
        timeElapsedSinceLastCheck = timeNow - timeStart
        if timeElapsedSinceLastCheck >= 1:  
                  gameTime = gameTime + 1
                  timeStart = time()
        
        drawObjects()
        
        #when the timer runs out
        if gameTime == 60:
            break
        
        #when player A dies
        if currentLive_A == 0:
            break
        
        #when player B dies
        elif currentLive_B == 0:
            break

        
        updateInformation()

        s.update()
        sleep(0.02)
        s.delete(playerA,playerB,scoreA,scoreB,bulletA,bulletB,ammoA,ammoB,floor,border,liveA,liveB,timer)
        
        deleteCoin()
        deleteAmmos()
        deleteRock()
        deleteEnemy()
        deleteBulletA()
        deleteBulletB()

        updateObjects()
        checkForCollisions()
        
    endGame()



root.after( 500, introScreen )
s.bind( "<Button-1>", mouseClickHandler )
s.bind( "<Key>", keyDownHandler )
s.bind( "<KeyRelease - w>", keyUpHandler_W)
s.bind( "<KeyRelease - W>", keyUpHandler_W)
s.bind( "<KeyRelease - a>", keyUpHandler_A)
s.bind( "<KeyRelease - A>", keyUpHandler_A)
s.bind( "<KeyRelease - s>", keyUpHandler_S)
s.bind( "<KeyRelease - S>", keyUpHandler_S)
s.bind( "<KeyRelease - d>", keyUpHandler_D)
s.bind( "<KeyRelease - D>", keyUpHandler_D)
s.bind( "<KeyRelease - Up>", keyUpHandler_Up)
s.bind( "<KeyRelease - Left>", keyUpHandler_Left)
s.bind( "<KeyRelease - Down>", keyUpHandler_Down)
s.bind( "<KeyRelease - Right>", keyUpHandler_Right)


s.pack()
s.focus_set()
root.mainloop()

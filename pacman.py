#############################################################################
##     _____                _____           _                _             ##
##    |  __ \              / ____|         | |              | |            ##
##    | |__) |___  _ __   | (___   __ _  __| | _____   _____| | ___   _    ##
##    |  _  // _ \| '_ \   \___ \ / _` |/ _` |/ _ \ \ / / __| |/ / | | |   ##
##    | | \ \ (_) | | | |  ____) | (_| | (_| | (_) \ V /\__ \   <| |_| |   ##
##    |_|  \_\___/|_| |_| |_____/ \__,_|\__,_|\___/ \_/ |___/_|\_\\__, |   ##
##                                                                __/ |    ##
##                                                               |___/     ##
## Description: Final Project - Pacman                                     ##
## Due Date: Wednesday, January 25, 2017                                   ##
##                                                                         ##
#############################################################################

import pygame
from random import randint
from pacman_classes import *

pygame.init()

screen = pygame.display.set_mode([32*19,32*23])

#----------------------IMAGES/FONT/SOUND----------------------------#

font = pygame.font.Font("font.otf",20)
startText = font.render("PRESS SPACE TO START",1,(255,255,255))
endText = font.render("GAME OVER",1,(255,0,0))
instructions = font.render("USE ARROW KEYS TO CONTROL PACMAN",1,(255,255,255))
instructions2 = font.render("COLLECT ALL THE DOTS",1,(255,255,255))

intro = pygame.mixer.Sound('pacmanintro.wav')
intro.set_volume(0.5)

siren = pygame.mixer.music.load('siren.wav')
pygame.mixer.music.set_volume(1.0)

death = pygame.mixer.Sound('pacmandeath.wav')
death.set_volume(0.5)

startscreen = pygame.image.load("startscreen.jpg")

life = pygame.image.load("life.png")
life = pygame.transform.scale(life,(25,25))

pacmanDies = [0]*18
pacmanDiesFrame = 1

for i in range(len(pacmanDies)):
    imageName = "dieframe"+str(i)+".png"
    pacmanDies[i] = pygame.image.load(imageName)
    pacmanDies[i] = pygame.transform.scale(pacmanDies[i],(25,25))

#-------------------------FUNCTIONS----------------------------------#

def start_screen(): #function to draw all the components of the start screen
    screen.fill((0,0,0))
    screen.blit(startscreen,(50,100))
    screen.blit(startText,(130,450))
    screen.blit(instructions,(35,525))
    screen.blit(instructions2,(130,575))
    pygame.display.update()
    
def redraw_screen(): #function for continuously redrawing the screen
    screen.fill((0,0,0))
    wall.draw(screen)
    
    if roundOver==False and dotCount!=188: #displays pacman and ghosts if the round is ongoing
        pacman.draw(screen)
        for i in range(len(ghost)):
            ghost[i].draw(screen,i+1)

    #life images drawn based on how many lives are remaining  
    if lives>=3: 
        screen.blit(life,(50,707))
    if lives>=2:
        screen.blit(life,(70,707))
    if lives>=1:
        screen.blit(life,(90,707))
            
    text = font.render(str(score),1,(255,255,255))
    screen.blit(text,(500,707))
    
    if roundOver:                                                               #display pacman dying sprite upon contact with a ghost
        screen.blit(pacmanDies[pacmanDiesFrame],(pacman.x-11,pacman.y-11))

    if gameOver:                                                                #displays game over text upon end of game
        screen.blit(endText,(229,387))

    pygame.display.update()

def restart():                                                                  #function to reset pacman and ghosts after pacman dies
    global pacman
    global ghost
    global pacmanDiesFrame

    pacman = Pacman(304,400)
    ghost = [Ghost(325,350),Ghost(325,350),Ghost(325,350),Ghost(325,350)]
    pacmanDiesFrame = 1

def new_round():                                                                #function to reset all the objects in a new round
    global pacman
    global ghost
    global wall

    pacman = Pacman(304,400)
    ghost = [Ghost(325,350),Ghost(325,350),Ghost(325,350),Ghost(325,350)]
    wall = Wall()

def ghost_movement():                                                            #function to coordinate all the ghost movements
    
    for i in range(len(ghost)):                                                  #loop to account for all ghosts in the game 

        ghost[i].glitchOutOfTheWall()                                            #prevents ghosts from getting stuck in the wall
        
        if not wall.collides(Block(ghost[i].x+ghost[i].speedX*2,ghost[i].y+ghost[i].speedY*2)): #controls the ghost movements
            pass
        elif not wall.collides(Block(ghost[i].x+32,ghost[i].y)) and ghost[i].speedX >= 0:
            ghost[i].moveRight()
        elif not wall.collides(Block(ghost[i].x-32,ghost[i].y)) and ghost[i].speedX <= 0:
            ghost[i].moveLeft()
        elif not wall.collides(Block(ghost[i].x,ghost[i].y-32)) and ghost[i].speedY <= 0:
            ghost[i].moveUp()
        elif not wall.collides(Block(ghost[i].x,ghost[i].y+32)) and ghost[i].speedY >= 0:
            ghost[i].moveDown()
        else:
            ghost[i].speedY *= -1
            ghost[i].speedX *= -1

        waysToMove = []                                                                 #list for all possible directions to move
        if not wall.collides(Block(ghost[i].x+32,ghost[i].y)) and ghost[i].speedX >= 0: #if there is a space open adjacent to a ghost, a way to move is added
            waysToMove.append(0)
        if not wall.collides(Block(ghost[i].x-32,ghost[i].y)) and ghost[i].speedX <= 0:
            waysToMove.append(1)
        if not wall.collides(Block(ghost[i].x,ghost[i].y-32)) and ghost[i].speedY <= 0:
            waysToMove.append(2)
        if not wall.collides(Block(ghost[i].x,ghost[i].y+32)) and ghost[i].speedY >= 0:
            waysToMove.append(3)

        if len(waysToMove)>1 and frameCount-ghost[i].okTurnTime>7:                 #based on the available ways to move, a random direction is chosen
            ghost[i].okTurnTime = frameCount
            r = randint(0,len(waysToMove)-1)
            if waysToMove[r]==0:
                ghost[i].moveRight()
            elif waysToMove[r]==1:
                ghost[i].moveLeft()
            elif waysToMove[r]==2:
                ghost[i].moveUp()
            elif waysToMove[r]==3:
                ghost[i].moveDown()

        if wall.collides(ghost[i]):                                                #stops collisions between wall and ghost
            ghost[i].stop()
            ghost[i].glitchOutOfTheWall()
                
#-----------------------VARIABLES/OBJECTS------------------------------#

wall = Wall()
pacman = Pacman(304,400)
ghost = [Ghost(325,350),Ghost(325,350),Ghost(325,350),Ghost(325,350)]

roundOver = False
gameOver = False
gameStart = False

frameCount = 0
time = 0                                                                            #variable to make a pause between rounds
score = 0 
dotCount = 0                                                                        #counts how many dots have been eaten by the pacman
lives = 3

#---------------------------MAIN LOOP-----------------------------------#

mainLoop = True

while mainLoop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False

    keys = pygame.key.get_pressed()

    if not gameStart:                                                                #displays the start screen if the game has not began 
        start_screen()

    if keys[pygame.K_SPACE] and not gameStart:                                       #if the space bar is pressed game begins
        gameStart = True
        intro.play()
        pygame.mixer.music.play(-1)
        
    if gameStart: 

        frameCount += 1

        pacman.glitchOutOfTheWall()                                                   #prevents pacman from getting stuck in the wall

        if wall.gameMap[int(abs(((pacman.y)//32)))][int(abs(((pacman.x)//32)))] == 0: #collects score
            wall.gameMap[int(abs(((pacman.y)//32)))][int(abs(((pacman.x)//32)))] = 7
            score += 10
            dotCount += 1
            
        if wall.collides(pacman):                                                     #pacman stops if collision with wall occurs
            pacman.speedX = 7
            pacman.speedY = 7
            pacman.glitchOutOfTheWall()
            pacman.stop()

        #arrow keys are used to control the pacman 
        if keys[pygame.K_RIGHT] and not wall.collides(Block(pacman.x+32,pacman.y)):
            pacman.moveRight()
        if keys[pygame.K_LEFT] and not wall.collides(Block(pacman.x-32,pacman.y)):
            pacman.moveLeft()
        if keys[pygame.K_UP] and not wall.collides(Block(pacman.x,pacman.y-32)):
            pacman.moveUp()
        if keys[pygame.K_DOWN] and not wall.collides(Block(pacman.x,pacman.y+32)):
            pacman.moveDown()

        ghost_movement()    
       
        for i in range(len(ghost)):
           
           if pacman.x > ghost[i].x-16 and pacman.x < ghost[i].x+16 and pacman.y > ghost[i].y-16 and pacman.y < ghost[i].y + 16: #checks for collision between pacman and ghosts
                roundOver = True                                                      #if collision occurs, the round is over and a life is lost
                ghost[i].x = 0
                ghost[i].y = 0
                death.play()
                lives -= 1

        if dotCount==188:                                                             #checks if all the dots in the playing field are eaten; if so, a new round begins
            pygame.mixer.music.stop()
            time+=1
            if time>50:                                                               #a few seconds delay is added before the new round begins
                new_round()
                pygame.mixer.music.play(-1)
                dotCount = 0
                time = 0
            
        if roundOver:
            pacmanDiesFrame+=1
            pygame.mixer.music.stop()
            time+=1                                                                   #a few seconds delay is added before the round restarts
            if time>100 and not gameOver:                                             #if the round is over but not the game, the pacman and ghosts reset
                roundOver = False
                restart()
                pygame.mixer.music.play(-1)
                time = 0
        
        if pacmanDiesFrame >= len(pacmanDies):                                        #pacman death sprite
            pacmanDiesFrame = 17

        if roundOver and lives==0:                                                    #if the round is over and no lives are remaining, the game is over
            gameOver = True

        redraw_screen()
        
    pygame.time.delay(10)
    
pygame.quit()

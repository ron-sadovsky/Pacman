import pygame

pacmanSpriteRight = [0]*12
pacmanSpriteUp = [0]*12
pacmanSpriteLeft = [0]*12
pacmanSpriteDown = [0]*12

for i in range(len(pacmanSpriteRight)):
    imageName = "frame_"+str(i)+"_delay-0.04s.gif"
    pacmanSpriteRight[i] = pygame.image.load(imageName)
    pacmanSpriteRight[i] = pygame.transform.scale(pacmanSpriteRight[i],(25,25))
    pacmanSpriteUp[i] = pygame.transform.rotate(pacmanSpriteRight[i],90)
    pacmanSpriteLeft[i] = pygame.transform.rotate(pacmanSpriteRight[i],180)
    pacmanSpriteDown[i] = pygame.transform.rotate(pacmanSpriteRight[i],270)

ghostSpriteUp = [0]*4
ghostSpriteDown = [0]*4
ghostSpriteLeft = [0]*4
ghostSpriteRight = [0]*4

for i in range(4):
    imageName = "RG-U"+str(i+1)+".png"
    ghostSpriteUp[i] = pygame.image.load(imageName)
    ghostSpriteUp[i] = pygame.transform.scale(ghostSpriteUp[i],(25,25))
    imageName2 = "RG-D"+str(i+1)+".png"
    ghostSpriteDown[i] = pygame.image.load(imageName2)
    ghostSpriteDown[i] = pygame.transform.scale(ghostSpriteDown[i],(25,25))
    imageName3 = "RG-R"+str(i+1)+".png"
    ghostSpriteRight[i] = pygame.image.load(imageName3)
    ghostSpriteRight[i] = pygame.transform.scale(ghostSpriteRight[i],(25,25))
    imageName4 = "RG-L"+str(i+1)+".png"
    ghostSpriteLeft[i] = pygame.image.load(imageName4)
    ghostSpriteLeft[i] = pygame.transform.scale(ghostSpriteLeft[i],(25,25))

ghost2SpriteUp = [0]*4
ghost2SpriteDown = [0]*4
ghost2SpriteLeft = [0]*4
ghost2SpriteRight = [0]*4

for i in range(4):
    imageName = "YG-U"+str(i+1)+".png"
    ghost2SpriteUp[i] = pygame.image.load(imageName)
    ghost2SpriteUp[i] = pygame.transform.scale(ghost2SpriteUp[i],(25,25))
    imageName2 = "YG-R"+str(i+1)+".png"
    ghost2SpriteRight[i] = pygame.image.load(imageName2)
    ghost2SpriteRight[i] = pygame.transform.scale(ghost2SpriteRight[i],(25,25))
    imageName3 = "YG-L"+str(i+1)+".png"
    ghost2SpriteLeft[i] = pygame.image.load(imageName3)
    ghost2SpriteLeft[i] = pygame.transform.scale(ghost2SpriteLeft[i],(25,25))
    imageName4 = "YG-D"+str(i+1)+".png"
    ghost2SpriteDown[i] = pygame.image.load(imageName4)
    ghost2SpriteDown[i] = pygame.transform.scale(ghost2SpriteDown[i],(25,25))

ghost3SpriteUp = [0]*4
ghost3SpriteDown = [0]*4
ghost3SpriteLeft = [0]*4
ghost3SpriteRight = [0]*4

for i in range(4):
    imageName = "PG-U"+str(i+1)+".png"
    ghost3SpriteUp[i] = pygame.image.load(imageName)
    ghost3SpriteUp[i] = pygame.transform.scale(ghost3SpriteUp[i],(25,25))
    imageName2 = "PG-R"+str(i+1)+".png"
    ghost3SpriteRight[i] = pygame.image.load(imageName2)
    ghost3SpriteRight[i] = pygame.transform.scale(ghost3SpriteRight[i],(25,25))
    imageName3 = "PG-L"+str(i+1)+".png"
    ghost3SpriteLeft[i] = pygame.image.load(imageName3)
    ghost3SpriteLeft[i] = pygame.transform.scale(ghost3SpriteLeft[i],(25,25))
    imageName4 = "PG-D"+str(i+1)+".png"
    ghost3SpriteDown[i] = pygame.image.load(imageName4)
    ghost3SpriteDown[i] = pygame.transform.scale(ghost3SpriteDown[i],(25,25))

ghost4SpriteUp = [0]*4
ghost4SpriteDown = [0]*4
ghost4SpriteLeft = [0]*4
ghost4SpriteRight = [0]*4

for i in range(4):
    imageName = "CG-U"+str(i+1)+".png"
    ghost4SpriteUp[i] = pygame.image.load(imageName)
    ghost4SpriteUp[i] = pygame.transform.scale(ghost4SpriteUp[i],(25,25))
    imageName2 = "CG-R"+str(i+1)+".png"
    ghost4SpriteRight[i] = pygame.image.load(imageName2)
    ghost4SpriteRight[i] = pygame.transform.scale(ghost4SpriteRight[i],(25,25))
    imageName3 = "CG-L"+str(i+1)+".png"
    ghost4SpriteLeft[i] = pygame.image.load(imageName3)
    ghost4SpriteLeft[i] = pygame.transform.scale(ghost4SpriteLeft[i],(25,25))
    imageName4 = "CG-D"+str(i+1)+".png"
    ghost4SpriteDown[i] = pygame.image.load(imageName4)
    ghost4SpriteDown[i] = pygame.transform.scale(ghost4SpriteDown[i],(25,25))

#---------------------------CLASSES--------------------------------------#
    
class Block(object):
    
    def __init__(self,x=1,y=1):
        self.x = x
        self.y = y

class Wall(object):

    def __init__(self):
        self.gameMap =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
                         [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
                         [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
                         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                         [1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1],
                         [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
                         [1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1],
                         [1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1],
                         [1,1,1,1,0,1,0,1,1,7,1,1,0,1,0,1,1,1,1],
                         [1,0,0,0,0,0,0,1,7,7,7,1,0,0,0,0,0,0,1],
                         [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],
                         [1,1,1,1,0,1,0,0,0,7,0,0,0,1,0,1,1,1,1],
                         [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],
                         [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
                         [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
                         [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
                         [1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1],
                         [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
                         [1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1],
                         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

    def draw(self, screen):

        for y in range(22):
            for x in range(19):
                if self.gameMap[y][x]==1:
                    pygame.draw.rect(screen,(0,0,255),(x*32,y*32,32,32),0)
                elif self.gameMap[y][x]==0:
                    pygame.draw.circle(screen,(255,255,150),(x*32+16,y*32+16),3)

    def collides(self, other):
        for y in range(22):
            for x in range(19):
                if x == (other.x-10)//32 and y == (other.y+10)//32 and self.gameMap[y][x]==1:
                    return True
                if x == (other.x-10)//32 and y == (other.y-10)//32 and self.gameMap[y][x]==1:
                    return True
                if x == (other.x+10)//32 and y == (other.y+10)//32 and self.gameMap[y][x]==1:
                    return True
                if x == (other.x+10)//32 and y == (other.y-10)//32 and self.gameMap[y][x]==1:
                    return True
        return False
            
class Pacman(object):

    def __init__(self, x=1, y=1,speedX=3,speedY=3,currentFrame=1,rotation=1):
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY
        self.currentFrame = currentFrame
        self.rotation = rotation

    def draw(self, screen):
        
        x = self.x
        y = self.y
        
        currentFrame = self.currentFrame

        if self.rotation==1:
            screen.blit(pacmanSpriteRight[self.currentFrame],(int(x)-11,int(y)-11))
        if self.rotation==2:
            screen.blit(pacmanSpriteLeft[self.currentFrame],(int(x)-11,int(y)-11))
        if self.rotation==3:
            screen.blit(pacmanSpriteUp[self.currentFrame],(int(x)-11,int(y)-11))
        if self.rotation==4:
            screen.blit(pacmanSpriteDown[self.currentFrame],(int(x)-11,int(y)-11))

        self.currentFrame+=1

        if self.currentFrame >= len(pacmanSpriteRight):
            self.currentFrame = 1

        self.x = self.x + self.speedX
        self.y = self.y + self.speedY
        
    def moveRight(self):
        self.speedY = 0
        self.speedX = 3
        self.rotation = 1

    def moveLeft(self):
        self.speedY = 0
        self.speedX = -3
        self.rotation = 2

    def moveUp(self):
        self.speedY = -3
        self.speedX = 0
        self.rotation = 3

    def moveDown(self):
        self.speedY = 3
        self.speedX = 0
        self.rotation = 4

    def glitchOutOfTheWall(self):
        if self.speedY!=0:
            self.x = abs(round((self.x-16)/32)*32+16)
        if self.speedX!=0:
            self.y = abs(round((self.y-16)/32)*32+16)

    def stop(self):
        self.speedY = 0
        self.speedX = 0

class Ghost(object):

    def __init__(self, x=1, y=1, speedX = 3, speedY = 3, currentFrame=1, rotation=1):
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY
        self.currentFrame = currentFrame
        self.rotation = rotation
        self.okTurnTime = 0

    def draw(self, screen, ghostType):
        x = self.x
        y = self.y

        currentFrame = self.currentFrame

        if ghostType==1:
            if self.rotation==1:
                screen.blit(ghostSpriteRight[self.currentFrame],(int(x)-11,int(y)-11))
            if self.rotation==2:
                screen.blit(ghostSpriteLeft[self.currentFrame],(int(x)-11,int(y)-11))
            if self.rotation==3:
                screen.blit(ghostSpriteUp[self.currentFrame],(int(x)-11,int(y)-11))
            if self.rotation==4:
                screen.blit(ghostSpriteDown[self.currentFrame],(int(x)-11,int(y)-11))

        if ghostType==2:
            if self.rotation==1:
                screen.blit(ghost2SpriteRight[self.currentFrame],(int(x)-11,int(y)-11))
            if self.rotation==2:
                screen.blit(ghost2SpriteLeft[self.currentFrame],(int(x)-11,int(y)-11))
            if self.rotation==3:
                screen.blit(ghost2SpriteUp[self.currentFrame],(int(x)-11,int(y)-11))
            if self.rotation==4:
                screen.blit(ghost2SpriteDown[self.currentFrame],(int(x)-11,int(y)-11))
           
        if ghostType==3:
            if self.rotation==1:
                screen.blit(ghost3SpriteRight[self.currentFrame],(int(x)-11,int(y)-11))
            if self.rotation==2:
                screen.blit(ghost3SpriteLeft[self.currentFrame],(int(x)-11,int(y)-11))
            if self.rotation==3:
                screen.blit(ghost3SpriteUp[self.currentFrame],(int(x)-11,int(y)-11))
            if self.rotation==4:
                screen.blit(ghost3SpriteDown[self.currentFrame],(int(x)-11,int(y)-11))
                
        if ghostType==4:
            if self.rotation==1:
                screen.blit(ghost4SpriteRight[self.currentFrame],(int(x)-11,int(y)-11))
            if self.rotation==2:
                screen.blit(ghost4SpriteLeft[self.currentFrame],(int(x)-11,int(y)-11))
            if self.rotation==3:
                screen.blit(ghost4SpriteUp[self.currentFrame],(int(x)-11,int(y)-11))
            if self.rotation==4:
                screen.blit(ghost4SpriteDown[self.currentFrame],(int(x)-11,int(y)-11))

        self.currentFrame += 1

        if self.currentFrame >= 4:
            self.currentFrame = 1
            

        self.x = self.x + self.speedX
        self.y = self.y + self.speedY

    def moveRight(self):
        self.speedY = 0
        self.speedX = 3.5
        self.rotation = 1

    def moveLeft(self):
        self.speedY = 0
        self.speedX = -3.5
        self.rotation = 2

    def moveUp(self):
        self.speedY = -3.5
        self.speedX = 0
        self.rotation = 3

    def moveDown(self):
        self.speedY = 3.5
        self.speedX = 0
        self.rotation = 4

    def stop(self):
        self.speedY = 0
        self.speedX = 0

    def glitchOutOfTheWall(self):
        if self.speedY!=0:
            self.x = abs(round((self.x-16)/32)*32+16)
        if self.speedX!=0:
            self.y = abs(round((self.y-16)/32)*32+16)
       

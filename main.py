import pygame
import time
import random

pygame.init()

windowWidth =  800
windowHeight = 600
FPS = 14
clock = pygame.time.Clock()
invaders_list = []                #list containing each object of an alien
scoreTrack =  0                    #keeping track of the score
alienMouvement = 0
spaceX = 0                                  #x coordiantes of the player
spaceY = 0                                  #y coordinattes of the player
lifeList = []                   #list containing the imgs of the player
life = 3                         # lives of the player
alive  = True
countdown =  200
count = 500
specialAlienList = []
bulletDrop = 0
topbulletDrop = 0
shootingAlien = [5,11,17,23,29]
topshootingAlien = [0,6,12,18,24]
hitnum = 0
Win = False

black =  (0,0,0)
white =  (255,255,255)
#nice color
color1 =  (255,25,77)
color2 = (255,150,220)
color3 = (130,100, 220)
color4 = (130,150,220)
gameExit = False



gameWindow = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption("Space Invaders In Python")

#Custom Font
font = pygame.font.Font("assets/font.ttf", 15)
myFont = pygame.font.SysFont("comicsansms",50)

spaceCraft = pygame.image.load("assets/player.png")
shotIcon = pygame.image.load("assets/tir 1.png")

def score():
    global countdown
    global count
    global hitnum
    count -= 1
    if count % 10 == 0:
        countdown -= 1
    txt = font.render("Score: "+str(scoreTrack),True,(255,255,255))
    aliensNum = font.render("Aliens:" +str(len(invaders_list)),True,(255,255,255))
    countDown = font.render("Time Left: " + str(countdown)+"  seconds",True,(255,255,255))
    hitnum_text = font.render("Boss hit : " + str(hitnum)+ " times",True,(255,0,0))
    gameWindow.blit(txt,(0,0))
    gameWindow.blit(aliensNum,(710,0))
    gameWindow.blit(countDown,(200,0))
    gameWindow.blit(hitnum_text,(630,580))


class Invaders:
    global_id = 0
    def __init__(self,x,y):
        self.id = Invaders.global_id
        self.posx = x
        self.posy = y
        self.life = 0
        self.alive = True
        self.shooting_capacity = True
        self.invader = pygame.image.load("assets/alien 1 2.png")
        Invaders.global_id += 1

    def birth(self, alienModulus):
        if self.id == 0 or  self.id == 1 or self.id == 6 or self.id ==7 or self.id == 12  or self.id == 13 or self.id == 18 or self.id == 19 or  self.id ==24 or self.id == 25 :
            if alienModulus % 2 == 0:
                self.invader = pygame.image.load("assets/alien 1 2.png")
            else:
                self.invader = pygame.image.load("assets/alien 1 1.png")
        if self.id == 2 or  self.id == 3 or self.id == 8 or self.id == 9 or self.id == 14  or self.id == 15 or self.id == 20 or self.id == 21 or  self.id ==26 or self.id == 27 :
            if alienModulus % 2 == 0:
                self.invader = pygame.image.load("assets/alien 2 1.png")
            else:
                self.invader = pygame.image.load("assets/alien 2 2.png")
        if self.id == 4 or  self.id == 5 or self.id == 10 or self.id == 11 or self.id == 16  or self.id == 17 or self.id == 22 or self.id == 23 or  self.id ==28 or self.id == 29:
            if alienModulus % 2 == 0:
                self.invader = pygame.image.load("assets/alien 3 1.png")
            else:
                self.invader = pygame.image.load("assets/alien 3 2.png")
        if self.id == 9999:
                self.invader = pygame.image.load("assets/ufo.png")
        gameWindow.blit(self.invader,(self.posx,self.posy))


def explosion(x,y):
    explode= pygame.image.load("assets/explosion.png")
    gameWindow.blit(explode,(x,y))

def fruit():
    fruitIcon = pygame.image.load("assets/img1.jpg")
    move = 0
    for i in range( 0,life):
        lifeList.append(gameWindow.blit(fruitIcon,(windowWidth/2+100+ move, 0)))
        move += 42
        if len(lifeList) > 3:
            lifeList.pop()  #removes the last item of the list

def shoot(shootX,shootY):
        pygame.draw.line(gameWindow,(255,255,255),(shootX,shootY-2),(shootX,shootY-20))

def alienShot():
    global bulletDrop
    global topbulletDrop
    global life
    global alive
    rand1 = random.randrange(0,30)
    downwardShot = pygame.image.load("assets/tir 3.png")

    #enables the shooting capacity of the bottom row aliens
    for invader in invaders_list:
        if invader.id == shootingAlien[0] or invader.id == shootingAlien[1] or invader.id == shootingAlien[2] or invader.id == shootingAlien[3]  or invader.id == shootingAlien[4]:
                if invader.posy+17 +bulletDrop > 600:
                    bulletDrop = 0
                #print( invader.posy+17 +bulletDrop)
                gameWindow.blit(downwardShot,(invader.posx+11, invader.posy+17 +bulletDrop))
                if invader.posy+17 +bulletDrop > 300:
                    if invader.posx+11 > spaceX and   invader.posx+11 < spaceX + 26:
                        if invader.posy+17 +bulletDrop > spaceY and invader.posy+17 +bulletDrop< spaceY + 8:
                            alive = False
                            bulletDrop = 0

    # enables the shooting capacity to the top row aliens
    for invader in invaders_list:
        if invader.id == topshootingAlien[0] or invader.id == topshootingAlien[1] or invader.id == topshootingAlien[2] or invader.id == topshootingAlien[3]  or invader.id == topshootingAlien[4]:
                if invader.posy+17 + topbulletDrop > 600:
                    topbulletDrop = 0
                #print( invader.posy+17 + topbulletDrop)
                gameWindow.blit(downwardShot,(invader.posx+11, invader.posy+17 + topbulletDrop))
                if invader.posy+17 + topbulletDrop > 300:
                    if invader.posx+11 > spaceX and   invader.posx+11 < spaceX + 26:
                        if invader.posy+17 + topbulletDrop > spaceY and invader.posy+17 + topbulletDrop< spaceY + 8:
                            alive = False
                            topbulletDrop = 0

    #Shooting capacity for the special Alien
    for  invader in specialAlienList:
        if invader.posy+17 + topbulletDrop > 600:
            topbulletDrop = 0
        downwardShot = pygame.image.load("assets/tir 3.png")
        gameWindow.blit(downwardShot,(invader.posx+11, invader.posy+17 + topbulletDrop))
        if invader.posy+17 + topbulletDrop > 300:
            if invader.posx+11 > spaceX and   invader.posx+11 < spaceX + 26:
                if invader.posy+17 + topbulletDrop > spaceY and invader.posy+17 + topbulletDrop< spaceY + 8:
                    alive = False
                    topbulletDrop = 0

    if alive == False:
        life  -= 1
        alive = True

def game_Intro():
    intro = True
    introText = "Press 'S' To Start OR 'Q' to quit"
    introIcon = pygame.image.load("assets/python.png")
    introIcon2 = pygame.image.load("assets/space_img1.png")
    while intro:
        intro_txt = font.render(introText,True,(255,255,255))
        gameWindow.blit(intro_txt,(windowWidth/2-140,20))
        gameWindow.blit(introIcon,(0,0))
        gameWindow.blit(introIcon2,(0,140))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    intro = False
                if event.key == pygame.K_a:
                    pygame.quit()
                    quit()

def gameLoop():
    global scoreTrack
    global alienMouvement
    global spaceX
    global spaceY
    global countdown
    global bulletDrop
    global topbulletDrop
    global hitnum
    global Win
    special_alien_move = 0
    spaceX = 400
    spaceY= 580
    moveX = 0
    moveY = 0
    incrementVar = 1
    global gameExit

    #For the motion of the bullet
    p = 0
    pp = 0
    #dd = True              For normalizing the shooting capacity of the player

    #coordiantes of the bulltet
    shootX = spaceX+13   #shootX = spaceX+13
    shootY = spaceY - 20
    moveShootY =  0
    shotFired = False
    bulletProof = True
    speciealBulletProof = True

    #creating instance of the aliens and putting them into arrays
    movealienX =  4
    movealienY =  5
    for invaderx in range(30 ,500,100):
        for invadery in range(20,300,50):
            invader_1 = Invaders(invaderx,invadery)
            invaders_list.append(invader_1)
    farRightAlien = invaders_list[len(invaders_list)-1].posx

    #instatiating an instace of the specieal alien
    pop = Invaders(400,10)
    pop.id = 9999
    specialAlienList.append(pop)

    #pygame.time.wait(999)
    shotAbsX = 0
    shotAbsY = 0

    #aliens shot
    gameOver = False

    while not gameExit:

        while gameOver == True:
            if Win == False:
                gameOverText = "Press 'Q' to quit"
                gameOverIcon = pygame.image.load("assets/game_over2.png")
                gameOver_txt = font.render(gameOverText,True,(255,255,255))
                gameWindow.blit(gameOverIcon,(windowWidth/2-200,230))
                gameWindow.blit(gameOver_txt,(windowWidth/2-80,240))
            else:
                gameWindow.fill(color3)
                gameOverText = "You WoN, BraVo !!!!!!!!!!!!!!!!!!!!!!!!!!!"
                gameOver_txt = font.render(gameOverText,True,(255,255,0))
                gameOverIcon = pygame.image.load("assets/space_image3.png")
                gameWindow.blit(gameOverIcon,(100,100))
                gameWindow.blit(gameOver_txt,(windowWidth/2-120,380))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        gameOver = False
                    if event.key == pygame.K_r:
                        pass



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_RIGHT:
                    moveX = 10
                if event.key == pygame.K_LEFT:
                    moveX = -10
                if event.key == pygame.K_SPACE:
                    #if dd == True: for normalizing the shooting capacity of the player
                        #shootX = spaceX +13   # for normalizing the shooting capacity of the player
                    moveShootY = -10
                    shotFired = True
                    bulletProof = False
                    speciealBulletProof = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT :
                    moveX = 0
                if event.key == pygame.K_p:
                    gameOver = True

        gameWindow.fill(color3)
        spaceX += moveX
        gameWindow.blit(spaceCraft,(spaceX,spaceY))   #blitting the player on to the screen

        p = spaceX +13
        pp = spaceY -20
        shootX = p
        shooY = pp

        shootY +=  moveShootY
        if shotFired == True:
            #dd = False
            gameWindow.blit(shotIcon,(shootX,shootY))
            shotAbsX = shootX
            shotAbsY = shootY
        if shootY-20 < 0:
            shotFired = False
            shootX = spaceX+10
            shootY =  spaceY
            #dd = True            for normalizing the shooting capicity of the player

        #moving aliens rightwads, leftwards and downwards
        for alien in invaders_list:
            if farRightAlien < 785:
                alien.posx += movealienX
                if invaders_list[len(invaders_list)-1].posx > 775:
                    for alieny in invaders_list:
                        alieny.posy += movealienY
                    farRightAlien =888
            else:
                alien.posx += movealienX*-1
                if invaders_list[len(invaders_list)-len(invaders_list)].posx < 2:
                    for alieny in invaders_list:
                        alieny.posy += movealienY
                    farRightAlien = 730

        #for the special alien
        for alien in specialAlienList:
            if special_alien_move < 785:
                alien.posx += movealienX
                if alien.posx > 783:
                    special_alien_move = 999
            else:
                alien.posx +=movealienX*-1   #moving the aliens leftwards
                if alien.posx < 4:
                    special_alien_move = alien.posx

        #collision between the shot and the aliens
        for alien in invaders_list:
            for shotx in range(shotAbsX,shotAbsX+6):
                if shotx > alien.posx  and    shotx < alien.posx +24:
                    for shoty in range(shotAbsY,shotAbsY+10):
                        if shoty > alien.posy and shoty <alien.posy+16:
                                if bulletProof == False:
                                    alien.alive = False
                                    bulletProof = True
                                    explosion(alien.posx,alien.posy)

        # removing the aliens from the alien list once there are hit
        for alien in invaders_list:
            if alien.alive == False:
                pygame.time.wait(5)
                invaders_list.remove(alien)
                scoreTrack += 10
                shotFired = False
                shootX = spaceX+10
                shootY =  spaceY
                for i in range(0,5):       #enabling the shooting capacity of  top aliens awhen bottom aliens are shot
                    if alien.id == shootingAlien[i]:
                        for invaders in invaders_list:
                            if invaders.id == alien.id - 1:
                                if invader.alive == True:
                                    shootingAlien[i] = alien.id -1
                #dd = True          for normalizing the shooting capacity of the player

        #Collision between the splayer's shot and the special alien
        for alien in specialAlienList:
            for shotx in range(shotAbsX,shotAbsX+6):
                if shotx > alien.posx  and    shotx < alien.posx +24:
                    for shoty in range(shotAbsY,shotAbsY+10):
                        if shoty > alien.posy and shoty <alien.posy+16:
                                    if  speciealBulletProof == False:
                                        alien.alive  = False
                                        explosion(alien.posx,alien.posy)
                                        speciealBulletProof = True

        for alien in specialAlienList:
            if alien.alive == False:
                pygame.time.wait(5)
                hitnum += 1
                alien.alive = True
                if hitnum == 10:
                    specialAlienList.remove(alien)

        alienMouvement +=1
        bulletDrop += 6
        topbulletDrop += 6

        #blitting the aliens
        #print("This is the length: "+str(len(invaders_list)))
        for  invader in invaders_list:
            invader.birth(alienMouvement)

        #special alien
        if len(invaders_list) != 0:
            if countdown > 155 and countdown < 180 or  countdown > 110 and countdown < 135  or  countdown > 85 and countdown < 100 or  countdown > 55 and countdown < 80 or  countdown > 10 and countdown < 30 :
                for invader in specialAlienList:
                    invader.birth(alienMouvement)
        else:
            for invader in specialAlienList:
                invader.birth(alienMouvement)

        #End Of the Game
        if life < 1:
            gameOver = True
        for invader in invaders_list:
            if invader.posy > 575:
                gameOver = True
        if len(invaders_list) == 0 and len(specialAlienList) == 0:
            Win = True
            gameOver  = True
        if countdown == 0:
            gameOver = True

        alienShot()           #setting the bullets of the aliens
        fruit()
        score()                     #printing out the score
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()



game_Intro()
gameLoop()

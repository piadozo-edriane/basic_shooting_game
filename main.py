import pygame
import random
import math
from pygame import mixer

pygame.init() # initialize the pygame

#function for the player image
def player (x, y):
    screen.blit(player_image, (x, y))

#function for the enemy image
def enemy (x, y, num):
    screen.blit(enemy_image[num], (x, y))

def fire_bullet (x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit (bullet_image, (x + 16, y + 10)) # 32 pixel / 2 so that it can be in the middle, 10 so that it can shoot above the space ship

def collision_buillet (enemy_x, enemy_y, bullet_x, bullet_y): # enemy and bullet variable are use for collision
    #calculates the distance of enemy and bullet points to midpoint
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow (bullet_y - enemy_y, 2)))

    if distance < 27: # if the distance of the bullet is < 27 pixel thent it's a collision
        return True
    else:
        return False

def show_score (x, y):
    score_show = font.render("Score: " + str(scores), True, (255,255,255 ))
    screen.blit(score_show, (x, y))
    
def game_over ():
    over_show = over_font.render("GAME OVER ", True, (255,255,255 ))
    screen.blit(over_show, (270, 250))

screen = pygame.display.set_mode((800, 600 )) # 800 width 600 height display the screen

#Change the caption and the icon of the game
pygame.display.set_caption("Space game ")
icon = pygame.image.load ("space.png")
pygame.display.set_icon(icon)


#Player Image
player_image = pygame.image.load ("player.png")
player_x = 370
player_y = 500
player_change  = 0


#Enemy Image
# use empty list so that it can increment base on the number of the enemies initialez to a variable
enemy_image = [] 
enemy_x = []
enemy_y = []
enemy_changeX = []
enemy_changeY = []
num_of_enemies = 5


for num in range (num_of_enemies):
    enemy_image.append (pygame.image.load ("space enemy.png"))
    enemy_x.append (random.randint (0, 735))
    enemy_y.append (random.randint (50, 150))
    enemy_changeX.append(0.2) # movement of enemy
    enemy_changeY.append(10) # from 10 pixel

#Bullet image
# ready - you cant see the bullet on the screen
# fire - the bullet is getting fired
bullet_image = pygame.image.load ("bullet.png")
bullet_x = 0
bullet_y = 500
bullet_y_change = 2 # movement of the bullet
bullet_state = "ready"

#Game display
running = True

#Score display in the screen
scores = 0
font = pygame.font.Font('freesansbold.ttf', 24) # ("Type of font", Font size)



font_x = 10 #in x coordinate with the value of 10 pixel
font_y = 10 #in y coordinate with the value of 10 pixel

#Game over text
over_font = pygame.font.Font('freesansbold.ttf', 42) # ("Type of font", Font size)


#Background music of th game
mixer.music.load("backgroundmusic.mp3")
mixer.music.play(-1) # to loop the music

while running:
    #Used rgb color for background
    screen.fill((102, 0, 102))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Movement of the player
        if event.type == pygame.KEYDOWN: # keystroke is pressed
            if event.key == pygame.K_LEFT: #left key is pressed that decrement into 0.2
                player_change -= 0.2
            if event.key == pygame.K_RIGHT: #right key is pressed that increment into 0.2
                player_change = 0.2
            if event.key == pygame.K_SPACE:# if the player press the space bar the player_x value and the bullet_y value will be the argument in the function
                bullet_sound = mixer.Sound("retro_laser.mp3")#shotting laser sound
                bullet_sound.play()#playing the laser sound
                bullet_x = player_x # get the current x coordinate of the spaceship 
                fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP: #settling down the spaceship/ or to not move
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0
    
    player_x += player_change # manipulates the movement of the player from increment and decrementing the player_x
    
    #boundaries in the screen of player
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736: #800 width - the size of pixel of the Player image which is 64
        player_x = 736

    #boundaries for the enemy screen and when it reaches to the boundary it increments to the value of enemy_changeY which is 10
    for num in range (num_of_enemies):# to appear the enemy 6 times use the num iteration in all of the enemy function
        if enemy_y[num] > 440:
            for num_j in range (num_of_enemies):
                enemy_y[num_j] = 2000
            game_over()
            break

        enemy_x[num] += enemy_changeX[num] # manipulates the movement of the enemy from incrementation and decrementation the enemy_x and enemy_y
        if enemy_x[num] <= 0:
            enemy_changeX[num] = 0.3
            enemy_y[num] += enemy_changeY[num]
        elif enemy_x[num] >= 736:
            enemy_changeX[num] = -0.3
            enemy_y[num] += enemy_changeY[num]

        collision = collision_buillet(enemy_x[num], enemy_y[num], bullet_x, bullet_y)# collision means the bullet and the enemy get hit
        if collision: # if it's collision the block of codes under the condition will execute
            collision_sound = mixer.Sound("collission_sound.mp3")#collision sound
            collision_sound.play()#playing the collision sound
            bullet_y = 480 # resets the bullet fire into the middle of the space ship
            bullet_state = "ready" # calling the function that it's ready to fire again
            scores += 1 # if the bullet hits the enemy the score will increment into 1
            enemy_x[num] = random.randint (0, 735) # random spawn of enemy in x coordinate
            enemy_y[num] = random.randint (50, 150) # random spawn of enemy in y coordinate

        enemy(enemy_x[num], enemy_y[num], num)# arguments for enemy

    #bullet movement

    # boundaries for bullet once it reaches to the 0 the bullet state
    if bullet_y <= 0:
        bullet_y = 480 # space for the realease of the bullet 
        bullet_state = "ready"

    if bullet_state is "fire": # value of the bullet_state in bullet function is fire. if the user press space bar it will be true
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change # decrementation of pixel in y axis means the bullet goes up 

    # Collision of the bullets

    player(player_x, player_y)#arguments so that the player can move the spaceship
    show_score(font_x, font_y)#function that call the score with the arguments of font_x and font_y
    #player_y += 0.1 increments the movement of the player from 0.1
    #Always update the screen
    pygame.display.update()
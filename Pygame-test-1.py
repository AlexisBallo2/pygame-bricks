import pygame
import random
import time
pygame.init() #initialising


#opening a new window
size = (520, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

#defining colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
BLUE = (138, 212, 255)
score = 0
# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
x=250
y=250
vx = 1
vy= 4
paddlex = 250

blockwidth = 80
blockheight =20
score = 0
blockyn = True
blockyan = True
blockybn = True
blockycn = True
blockydn = True
blockyen = True
blockyfn = True
blockygn = True
blockyhn = True
blockyin = True
blockyjn = True
blocky11n = True
blocky12n = True
blocky13n = True
blocky14n = True
class brick(pygame.sprite.Sprite):
    def __init__(self, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        pygame.draw.rect(screen,BLACK,[width,height,blockwidth,blockheight])


# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop


    screen.fill(BLUE)
    pygame.draw.circle(screen, BLACK, [x,y], 10)
        # First, clear the screen to white.

    #ball movement
    x=x+vx
    y=y+vy
    if y > 490 and ((x >= paddlex) and (x <= paddlex+100)):
        vy=-vy
        yesorno = random.randint(1, 5)
        if yesorno == 2 or yesorno == 4:
            vx =- int(random.uniform(1,5))
            if yesorno == 3 or yesorno == 1:
                vx = int(random.uniform(1, 5))
    if x > 510:
        vx = -vx
    if y < 10:
        vy=-vy
 #      yesorno = random.randint(1,4)
 #     if yesorno == 2:
  #        vx =- int(random.uniform(1,5))
  #    if yesorno == 3 or yesorno == 1:
   #       vx = int(random.uniform(1, 5))
    if x < 10:
        vx = -vx
    if  y > 510:
        score = 0
        x = 250
        y = 250
        paddlex = 200
        vx = 0
        vy = 0
        blockyan = True
        blockyn = True
        blockybn = True
        blockycn = True
        blockydn = True
        blockycn = True
        blockydn = True
        blockyen = True
        blockyfn = True
        blockygn = True
        blockyhn = True
        blockyin = True
        blockyjn = True
        blocky11n = True
        blocky12n = True
        blocky13n = True
        blocky14n = True
        vx =1
        vy = 5
        pygame.display.flip()
        time.sleep(1)


    pygame.draw.rect(screen, BLACK, [paddlex,490,100,10])

    #key listeners
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and paddlex != 0:
            left = True
            while left:
                paddlex = paddlex-5
                break
        elif event.key == pygame.K_RIGHT and paddlex != 420:
            right = True
            while right:
                paddlex = paddlex+5
                break
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            left = False
            right = False

    #Display score:
    font = pygame.font.Font(None, 25)
    text = font.render(("Score: " + str(score)), 1, BLACK)
    screen.blit(text, (210,25))
    #BLOCK 1
    newblock1 = 400
    newblock2 = 100
    if blockyn:
        newblock = brick(newblock1,newblock2)
        if (x > newblock1 and x < newblock1+blockwidth) and (y > newblock2 and y < newblock2+blockheight):
            blockyn = False
            score += 1
            vy=-vy
    #BLOCK2
    newblock3 = 310
    newblock4 = 100
    if blockyan:
        newblock2 = brick(newblock3,newblock4)
        if (x > newblock3 and x < newblock3+blockwidth) and (y > newblock4 and y < newblock4+blockheight):
            blockyan = False
            score += 1
            vy = -vy
    # BLOCK3
    newblock5 = 220
    newblock6 = 100
    if blockybn:
        newblock3 = brick(newblock5, newblock6)
        if (x > newblock5 and x < newblock5 + blockwidth) and (y > newblock6 and y < newblock6 + blockheight):
            blockybn = False
            score += 1
            vy = -vy
    # BLOCK4
    newblock7 = 130
    newblock8 = 100
    if blockycn:
        newblock4 = brick(newblock7, newblock8)
        if (x > newblock7 and x < newblock7 + blockwidth) and (y > newblock8 and y < newblock8 + blockheight):
            blockycn = False
            score += 1
            vy = -vy
    # BLOCK5
    newblock9 = 40
    newblock10 = 100
    if blockydn:
        newblock5 = brick(newblock9, newblock10)
        if (x > newblock9 and x < newblock9 + blockwidth) and (y > newblock10 and y < newblock10 + blockheight):
            blockydn = False
            score += 1
            vy = -vy
    # BLOCK6
    newblock11 = 40
    newblock12 = 130
    if blockyen:
        newblock6 = brick(newblock11, newblock12)
        if (x > newblock11 and x < newblock11 + blockwidth) and (y > newblock12 and y < newblock12 + blockheight):
            blockyen = False
            score += 1
            vy = -vy
    # BLOCK7
    newblock13 = 130
    newblock14 = 130
    if blockyfn:
        newblock7 = brick(newblock13, newblock14)
        if (x > newblock13 and x < newblock13 + blockwidth) and (y > newblock14 and y < newblock14 + blockheight):
            blockyfn = False
            score += 1
            vy = -vy
    # BLOCK8
    newblock15 = 220
    newblock16 = 130
    if blockygn:
        newblock8 = brick(newblock15, newblock16)
        if (x > newblock15 and x < newblock15 + blockwidth) and (y > newblock16 and y < newblock16 + blockheight):
            blockygn = False
            score += 1
            vy = -vy
    # BLOCK9
    newblock17 = 310
    newblock18 = 130
    if blockyhn:
        newblock9 = brick(newblock17, newblock18)
        if (x > newblock17 and x < newblock17+ blockwidth) and (y > newblock18 and y < newblock18 + blockheight):
            blockyhn = False
            score += 1
            vy = -vy
    # BLOCK9.5
    newblock19 = 400
    newblock20 = 130
    if blockyin:
        newblock95 = brick(newblock19, newblock20)
        if (x > newblock19 and x < newblock19+ blockwidth) and (y > newblock20 and y < newblock20 + blockheight):
            blockyin = False
            score += 1
            vy = -vy
    # BLOCK10
    newblock21 = 130
    newblock22 = 160
    if blockyjn:
        newblock10 = brick(newblock21, newblock22)
        if (x > newblock21 and x < newblock21+ blockwidth) and (y > newblock22 and y < newblock22 + blockheight):
            blockyjn = False
            score += 1
            vy = -vy
    # BLOCK11
    newblock23 = 40
    newblock24 = 160
    if blocky11n:
        newblock11 = brick(newblock23, newblock24)
        if (x > newblock23 and x < newblock23+ blockwidth) and (y > newblock24 and y < newblock24 + blockheight):
            blocky11n = False
            vy = -vy
    # BLOCK12
    newblock25 = 220
    newblock26 = 160
    if blocky12n:
        newblock12 = brick(newblock25, newblock26)
        if (x > newblock25 and x < newblock25+ blockwidth) and (y > newblock26 and y < newblock26 + blockheight):
            blocky12n = False
            score += 1
            vy = -vy
    # BLOCK13
    newblock27 = 310
    newblock28 = 160
    if blocky13n:
        newblock13 = brick(newblock27, newblock28)
        if (x > newblock25 and x < newblock25+ blockwidth) and (y > newblock26 and y < newblock26 + blockheight):
            blocky13n = False
            score += 1
            vy = -vy
    # BLOCK14
    newblock29 = 400
    newblock30 = 160
    if blocky14n:
        newblock13 = brick(newblock29, newblock30)
        if (x > newblock29 and x < newblock29+ blockwidth) and (y > newblock30 and y < newblock30 + blockheight):
            blocky14n = False
            score += 1
            vy = -vy
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(120)
# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
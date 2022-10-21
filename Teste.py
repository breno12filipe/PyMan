import pygame
from pygame.locals import *
import sys
import pyganim

pygame.init()
vec= pygame.math.Vector2
acc= 0.3
size = (1280, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("scroller")
clock = pygame.time.Clock()

colours = {"white":(255, 255, 255), "green":(0, 255, 0), "blue":(0, 0, 255), "red":(255, 0, 0), "cyan":(0, 255, 255), "black":(0, 0, 0)}
groundx = 0
y_vel = 0.0
char_y = 490
spiderx = 1000
spidery = 500



#Images
run_left_anim = [pygame.image.load("assets\sprites\megaman\megaman_walking1-left.png"),
                pygame.image.load("assets\sprites\megaman\megaman_walking2-left.png"),
			    pygame.image.load("assets\sprites\megaman\megaman_walking3-left.png")]
run_right_anim = [pygame.image.load("assets\sprites\megaman\megaman_walking1-right.png"),
                pygame.image.load("assets\sprites\megaman\megaman_walking2-right.png"),
			    pygame.image.load("assets\sprites\megaman\megaman_walking3-right.png")]
boltAnim = pyganim.PygAnimation([('assets\sprites\megaman\megaman_stand1.png', 900),
                                 ('assets\sprites\megaman\megaman_stand2.png', 900)])


class Player(pygame.sprite.Sprite):
    def __init__(self):
      self.direct = "RIGHT"
      self.image = pygame.image.load("assets\sprites\megaman\megaman_stand1.png")
      self.rect = self.image.get_rect()
      #Movement variables
      self.jumping = False
      self.running = False
      self.move_frame = 0
      #Position 
      self.pos = vec(620,490)
      #Acceleration and speed
      self.acc = vec(0,0)
      self.speed = vec(0,0)
    
    def move(self):
        self.acc = vec(0,0.5)
         
        if self.speed.x !=0:
            self.running = True
        else:
          self.running = False
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.acc.x = -acc
        if keys[pygame.K_d]:
            self.acc.x = acc
        
        self.rect.midbottom = self.pos
        
    def update(self):
        if self.move_frame > 2:
            self.move_frame = 0
            return

        if self.jumping == False and self.running == True:
            if self.speed.x>0:
                self.image = run_right_anim[self.move_frame]
                self.direct = "RIGHT"
            else:
                self.image = run_left_anim[self.move_frame]
                self.direct = "LEFT"
            self.move_frame += 1
        if self.speed.x == 0 and self.move_frame != 0:
            self.move_frame = 0
            if self.direct == "RIGHT":
                self.image = run_right_anim[self.move_frame]
            elif self.direct == "LEFT":
                self.image = run_left_anim[self.move_frame]
    def attack(self):
        pass
    
    def jump(self):
        pass


player = Player()
playergroup = pygame.sprite.Group()

while True:


    for event in pygame.event.get():
        # Will run when the close window button is clicked    
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
        
        if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_SPACE:
                    player.jump()
                    
  
     
   

	
    
	
   
    ground = pygame.Rect(0 + groundx, 640, 1280, 60)
    ground2 = pygame.Rect(1280 + groundx, 560, 1280, 60)
    groundcollide = pygame.Rect(622, (player.pos.y + 77 - y_vel), 63, 1)
    spider = pygame.Rect(0 + spiderx, 620, 50, 20)
	
    if groundcollide.colliderect(ground):
        player.speed.y = 0.0
        player.pos.y = ground.y - 77
    elif groundcollide.colliderect(ground2):
        player.speed.y = 0.0
        player.pos.y = ground2.y - 77
    elif player.speed.y > -20:
        player.speed.y -= 1
	
    if player.rect.colliderect(spider):
        print("hit") 

    
	
    screen.fill(colours["cyan"])
	
    pygame.draw.rect(screen, colours["green"], ground, 0)
    pygame.draw.rect(screen, colours["green"], ground2, 0)
    #pygame.draw.rect(screen, colours["red"], groundcollide, 0)
    pygame.draw.rect(screen, colours["black"], spider, 0)
    #pygame.draw.rect(screen, colours["black"], charbox, 0)
 
    clock.tick(60)
    
    screen.blit(player.image, player.rect)
    pygame.display.update()
    
    #print (player.image.get_rect())

    #pygame.quit()
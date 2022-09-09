import pygame
from weapon import Weapon

pygame.init()

size = (1280, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("scroller")
clock = pygame.time.Clock()

done = False
colours = {"white":(255, 255, 255), "green":(0, 255, 0), "blue":(0, 0, 255), "red":(255, 0, 0), "cyan":(0, 255, 255), "black":(0, 0, 0)}
groundx = 0
chardirec = "right"
y_vel = 0.0
char_y = 490

char = pygame.image.load("./assets/sprites/megaman/megaman_stand1.png").convert_alpha()
charl = pygame.transform.flip(char, True, False)

spiderx = 1000
spidery = 500

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_a] == True:
		groundxvel = 5
		chardirec = "left"
	elif keys[pygame.K_d] == True:
		groundxvel = -5
		chardirec = "right"
	else:
		groundxvel = 0
	
	groundx += groundxvel
	spiderx += groundxvel
	
	if keys[pygame.K_SPACE] == True and (groundcollide.colliderect(ground) or groundcollide.colliderect(ground2)):
		y_vel = 17.0
	
	char_y -= y_vel
	
	charbox = pygame.Rect(624, char_y + 4, 59, 69)
	ground = pygame.Rect(0 + groundx, 640, 1280, 60)
	ground2 = pygame.Rect(1280 + groundx, 560, 1280, 60)
	groundcollide = pygame.Rect(622, (char_y + 77 - y_vel), 63, 1)
	spider = pygame.Rect(0 + spiderx, 620, 50, 20)
	
	if groundcollide.colliderect(ground):
		y_vel = 0.0
		char_y = ground.y - 77
	elif groundcollide.colliderect(ground2):
		y_vel = 0.0
		char_y = ground2.y - 77
	elif y_vel > -20:
		y_vel -= 1
	
	if charbox.colliderect(spider):
		print("hit") 

	
	screen.fill(colours["cyan"])
	
	pygame.draw.rect(screen, colours["green"], ground, 0)
	pygame.draw.rect(screen, colours["green"], ground2, 0)
	#pygame.draw.rect(screen, colours["red"], groundcollide, 0)
	pygame.draw.rect(screen, colours["black"], spider, 0)
	#pygame.draw.rect(screen, colours["black"], charbox, 0)
	
	if chardirec == "right":
		screen.blit(char, (620, char_y))
	else:
		screen.blit(charl, (620, char_y))
	
	pygame.display.flip()
	
	clock.tick(60)

print (char.get_rect())

pygame.quit()
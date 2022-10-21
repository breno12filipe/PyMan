import pygame

pygame.init()

size = (1280, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("scroller")
clock = pygame.time.Clock()

done = False
colours = {"white":(255, 255, 255), "green":(0, 255, 0), "blue":(0, 0, 255), "red":(255, 0, 0), "cyan":(0, 255, 255), "black":(0, 0, 0)}
groundx = 0
chardirec = "stand"
y_vel = 0.0
char_y = 490
spiderx = 1000
spidery = 500

sprite_value = 0
#sprites
stand_sprite = [pygame.image.load("assets\sprites\megaman\megaman_stand1.png"),
                pygame.image.load("assets\sprites\megaman\megaman_stand2.png")]

walking_left_sprite=[pygame.image.load("assets\sprites\megaman\megaman_walking1-left.png"),
																					pygame.image.load("assets\sprites\megaman\megaman_walking2-left.png"),
																					pygame.image.load("assets\sprites\megaman\megaman_walking3-left.png")]

char = pygame.image.load("./assets/sprites/megaman/megaman_stand1.png").convert_alpha()
charl = pygame.transform.flip(char, True, False)




while not done:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	if event.type  == pygame.KEYUP:
		if event.key == pygame.K_a or event.key == pygame.K_d:
			moving = False
			sprite_value = 0
 
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_a] == True:
		moving = True
		groundxvel = 5
		chardirec = "left"
		print("left")
		print(sprite_value)
	elif keys[pygame.K_d] == True:
		moving = True
		groundxvel = -5
		chardirec = "right"
		print("right")
		print(sprite_value)
	else:
		chardirec = "stand"
		groundxvel = 0
		moving = False
		print("stand")
		print(sprite_value)
	
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
	if moving == True:
		sprite_value =+1
	if moving ==True:
		if sprite_value >= len(walking_left_sprite):
			sprite_value = 0
		image = walking_left_sprite[sprite_value]
	elif moving == False:
		if sprite_value>= len(stand_sprite):
			sprite_value = 0
	image = stand_sprite[sprite_value]
	

	if chardirec == "right":
		screen.blit(char, (620, char_y))
	elif chardirec == "left":
		screen.blit(image, (620, char_y))
	else:
		screen.blit(image,(620, char_y))
	
	clock.tick(60)
	pygame.display.update()
	sprite_value +=1
	print("teste")
	

print (char.get_rect())

pygame.quit()
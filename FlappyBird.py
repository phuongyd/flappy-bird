
import pygame
from random import randint

pygame.init()
pygame.mixer.init()
screen= pygame.display.set_mode((400,600))
pygame.display.set_caption ('Flappy Bird')
clock=pygame.time .Clock()
WHITE=(255,255,255)
RED=(235, 240, 242)
BLUE=(0,0,255)
x_bird =50
y_bird =350
tube1_x=400
tube2_x=600
tube3_x=800
tube_width=50
tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)
d_2tube= 150
bird_drop_velocity=0
gravity=0.5
tube_velocity =2
score=0
font=pygame.font.SysFont('san',20)
font1 =pygame.font.SysFont('san',40)


background_img=pygame.image.load('images/background.png')
background_img=pygame.transform.scale(background_img,(400,600))
bird_img=pygame.image.load('images/bird.png')
bird_img=pygame.transform.scale(bird_img,(50,30))
tube_img=pygame.image.load('images/tube.png')
tube_op_img=pygame.image.load('images/tube_op.png')
sand_img=pygame.image.load('cat.png')
sand_img=pygame.transform.scale(sand_img,(400,30))
sound = pygame.mixer.Sound('no6.wav')
point = pygame.mixer.Sound('point.wav')
jum = pygame.mixer.Sound('sfx_swooshing.wav')
die = pygame.mixer.Sound('sfx_hit.wav')
tube1_pass=False
tube2_pass=False
tube3_pass=False


pausing =False
running = True
while running:

	clock.tick(60)
	screen.fill(WHITE)
	screen.blit(background_img,(0,0))
	#vẽ cát
	sand =screen.blit(sand_img,(0,570))

	# ép ống và vẽ ống
	tube1_img =pygame.transform.scale(tube_img,(tube_width,tube1_height))
	tube1=screen.blit(tube1_img,(tube1_x,0))
	tube2_img =pygame.transform.scale(tube_img,(tube_width,tube2_height))
	tube2=screen.blit(tube2_img,(tube2_x,0))
	tube3_img =pygame.transform.scale(tube_img,(tube_width,tube3_height))
	tube3=screen.blit(tube3_img,(tube3_x,0))
	#vẽ ống đối diện
	tube1_op_img = pygame.transform.scale(tube_op_img,(tube_width,600-(tube1_height+d_2tube)))
	tube1_op=screen.blit(tube1_op_img,(tube1_x,tube1_height+d_2tube))
	tube2_op_img = pygame.transform.scale(tube_op_img,(tube_width,600-(tube2_height+d_2tube)))
	tube2_op=screen.blit(tube2_op_img,(tube2_x,tube2_height+d_2tube))
	tube3_op_img = pygame.transform.scale(tube_op_img,(tube_width,600-(tube3_height+d_2tube)))
	tube3_op=screen.blit(tube3_op_img,(tube3_x,tube3_height+d_2tube))
	#di chuyển ống
	tube1_x-=tube_velocity
	tube2_x-=tube_velocity
	tube3_x-=tube_velocity
	#tạo ống mới
	if tube1_x<-tube_width:
		tube1_x=550
		tube1_height=randint(100,400)
		tube1_pass =False
	if tube2_x<-tube_width:
		tube2_x=550
		tube2_height=randint(100,400)
		tube2_pass =False
	if tube3_x<-tube_width:
		tube3_x=550
		tube3_height=randint(100,400)
		tube3_pass =False

	# vẽ con chim
	bird =screen.blit(bird_img,(x_bird,y_bird))
	y_bird+=bird_drop_velocity
	bird_drop_velocity+=gravity
	#ghi điểm
	score_txt=font.render("Score: "+str(score),True,RED)
	screen.blit(score_txt,(5,5))


	


	#cộng điểm
	if tube1_x+tube_width<=x_bird and tube1_pass ==False:
		score+=1
		tube1_pass=True
		pygame.mixer.Sound.play(point)
	if tube2_x+tube_width<=x_bird and tube2_pass ==False:
		score+=1
		tube2_pass=True
		pygame.mixer.Sound.play(point)
	if tube3_x+tube_width<=x_bird and tube3_pass ==False:
		score+=1
		tube3_pass=True
		pygame.mixer.Sound.play(point)
	#kiểm tra va chạm
	tubes = [tube1,tube2,tube3,tube1_op,tube2_op,tube3_op,sand]
	for tube in tubes:
		if bird.colliderect(tube):
            
			tube_velocity =0
			bird_drop_velocity =0
			game_over_txt=font1.render("Game over,Score: "+str(score),True,RED)
			screen.blit(game_over_txt,(85,200))
			space_txt=font.render("Press SPACE to continue!",True,BLUE)
			screen.blit(space_txt,(120,290))
			pausing=True
            








		if y_bird > 600 :

			tube_velocity =0
			bird_drop_velocity =0
			game_over_txt=font1.render("Game over,Score: "+str(score),True,RED)
			screen.blit(game_over_txt,(85,200))
			space_txt=font.render("Press SPACE to continue!",True,BLUE)
			screen.blit(space_txt,(120,290))
			pausing=True
		if y_bird <0 :

			tube_velocity =0
			bird_drop_velocity =0
			game_over_txt=font1.render("Game over,Score: "+str(score),True,RED)
			screen.blit(game_over_txt,(85,200))
			space_txt=font.render("Press SPACE to continue!",True,BLUE)
			screen.blit(space_txt,(120,290))
			pausing=True

	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			running = False
		if event.type ==  pygame.KEYDOWN:
			if event.key ==pygame.K_SPACE:
				pygame.mixer.Sound.play(jum)
				bird_drop_velocity=0
				bird_drop_velocity -=7

				if pausing:
					pygame.mixer.unpause()
					x_bird =50
					y_bird =350
					tube1_x=400
					tube2_x=600
					tube3_x=800
					tube_velocity =2
					score=0
					pausing = False	



	pygame.display.flip()
pygame.quit()

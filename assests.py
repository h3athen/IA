import pygame
from pygame.locals import *
import sys
import random, time


background = pygame.Surface((640,480))
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
background.fill("white")
def main(background):
	pygame.init()
	font = pygame.font.Font(None, 100)
	ball_production = 10
	pygame.time.set_timer(ball_production, 3000)
	points = []
	running = True
	game_over = False



	
	class BallObject(pygame.sprite.Sprite):
		def __init__(self, x,y, speed,image_file, number):
			pygame.sprite.Sprite.__init__(self, self.containers)
			self.x = x
			self.y = y
			self.size = 10
			self.speed = speed
			self.image = pygame.image.load(image_file).convert_alpha()
			self.image = pygame.transform.scale(self.image, (75,75))
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y
			self.font = pygame.font.SysFont('Arial', 10)
			self.number = number
			self.radius = 25
			
		def update_screen(self, points):
			screen.blit(self.image, (self.rect))
			
			if self.rect.y <= 0:
				self.rect.y = 0
				self.speed = 0
			elif self.speed == 0 and self.speed != 0:
				self.rect.y -= self.speed
				
				mouse_pos = pygame.mous.get_pos()
				mouse_clicked = pygame.mouse.get_pressed()
				
				if self.rect.collidepoint(*mouse_pos) and mouse_clicked[0]:
					self.kill()
		def collide(self, ball_list):
			col = pygame.sprite.spritecollide(self, ball_list, False, pygame.sprite.collide_circle)
			for  c in col:
				if c.speed == 0:
					self.speed += 5
		
			

		
	
	ball_list = pygame.sprite.Group()
	BallObject.containers = ball_list


	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == ball_production:
				for i in range(random.randint(1,3)):
					BallObject(random.randint(0,400), 400, random.randint(1,4), "num1.png", 1)
			elif sum(points) >= 900:
				game_over = True
					
		screen.blit(background, (0,0))
		pointsText = font.render("Points: %d" % sum(points), True, (255,255,255,), None)
		pointsText_Rect = pointsText.get_rect()
		screen.blit(pointsText, [25,100])
		
		if not game_over:
			for ball in ball_list:
				ball.update(points)
			for ball in ball_list:
				ball_list.remove(ball)
				ball.collide(ball_list)
				ball_list.add(ball)
				
		elif game_over:
			for ball in ball_list:
				ball.speed = 0
			
			if sum(points) >= 900:
				text = font.render("You win!", True, (255,255,255), None)
				textrect = text.get_rect()
				textx = screen.get_width() / 2 - textrect.width / 2
				texty = screen.get_height() / 2 - textrect.height / 2
				ball_list.clear(screen, background)
				ball_list.update(points)
				screen.blit(text, [textx,texty])
				pygame.display.flip()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						close_window = True
		else:
			ball_list.clear(screen, background)
			ball_list.update(points)
		
		pygame.display.flip()
		clock.tick(60)
	pygame.quit()
if __name__ == '__main__':
	main(background)
		

			
	
		


	
	

import pygame.sprite


class Bird(pygame.sprite.Sprite):
	def __init__(self, images, x: int, y: int, velocity: int):
		super().__init__()
		self.images = images
		self.image = images[0]
		self.rect = self.image.get_rect()
		self.rect.inflate_ip(-15, -10)
		self.rect.x = x
		self.rect.y = y
		self.velocity = velocity
		self.step_index = 0

	def update(self):
		self.handle_step_index()
		self.animation()
		self.rect.x += self.velocity

	def animation(self):
		if self.step_index > 8:
			self.image = self.images[2]
		elif self.step_index > 4:
			self.image = self.images[1]
		else:
			self.image = self.images[0]

	def check_collision(self, player):
		player_rect = player.rect.copy()
		player_rect.inflate_ip(-30, -30)
		return self.rect.colliderect(player_rect)

	def handle_step_index(self):
		self.step_index += 1
		if self.step_index >= 12:
			self.step_index = 0

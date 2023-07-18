import pygame.sprite
from dino_runner.utils.constants import BLOCK


class Block(pygame.sprite.Sprite):
	def __init__(self, x: int, velocity: int):
		super().__init__()
		self.image = BLOCK[0]
		self.rect = self.image.get_rect()
		self.rect.inflate_ip(-10, -10)
		self.rect.x = x
		self.rect.y = 345
		self.step_index = 0
		self.velocity = velocity

	def update(self):
		self.rect.x += self.velocity
		self.handle_step_index()
		self.image = BLOCK[0] if self.step_index < 5 else BLOCK[1]

	def handle_step_index(self):
		self.step_index += 1
		if self.step_index >= 10:
			self.step_index = 0

	def check_collision(self, player):
		player_rect = player.rect.copy()
		player_rect.inflate_ip(-20, -20)
		return self.rect.colliderect(player_rect)

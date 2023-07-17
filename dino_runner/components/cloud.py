import random

import pygame.sprite
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH


class Cloud(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = CLOUD
		self.rect = self.image.get_rect()
		self.rect.x = SCREEN_WIDTH + 20
		self.rect.y = random.randint(10, 150)
		self.velocity = random.randint(1, 3)

	def update(self):
		self.rect.x -= self.velocity

		if self.rect.right <= 0:
			self.kill()

import random

import pygame.sprite

from dino_runner.utils.constants import SCREEN_WIDTH, SNOW


class SnowPowerUp(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = SNOW
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(SCREEN_WIDTH, SCREEN_WIDTH * 2)
		self.rect.y = random.randrange(200, 300)
		self.duration = 200

	def update(self, game_speed):
		self.rect.x -= int(game_speed)
		if self.rect.right < 0:
			self.kill()

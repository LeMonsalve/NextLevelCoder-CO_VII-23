import random

import pygame

from dino_runner.components.power_ups.snow.snow_powerup import SnowPowerUp


class SnowManager:
	def __init__(self):
		self.power_ups = pygame.sprite.Group()
		self.spawn_timer = 0
		self.spawn_interval = 500

	def update(self, game):
		self.spawn_timer += 1
		if self.spawn_timer >= self.spawn_interval:
			if random.randrange(0, 100) < 50:
				snow_power_up = SnowPowerUp()
				self.power_ups.add(snow_power_up)
			self.spawn_timer = 0

		self.power_ups.update(game.game_speed)

	def draw(self, screen):
		self.power_ups.draw(screen)

	def reset(self):
		self.power_ups.empty()
		self.spawn_timer = 0

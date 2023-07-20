import random

import pygame

from dino_runner.components.power_ups.invincible.invincible_powerup import InvinciblePowerUp


class InvincibleManager:
	def __init__(self):
		self.invincible_power_ups = pygame.sprite.Group()
		self.spawn_timer = 0
		self.spawn_interval = 700

	def update(self, game):
		self.spawn_timer += 1
		if self.spawn_timer >= self.spawn_interval:
			if random.randrange(0, 100) < 100:
				invincible_power_up = InvinciblePowerUp()
				self.invincible_power_ups.add(invincible_power_up)
			self.spawn_timer = 0

		self.invincible_power_ups.update(game.game_speed)

	def draw(self, screen):
		self.invincible_power_ups.draw(screen)

	def reset(self):
		self.invincible_power_ups.empty()
		self.spawn_timer = 0

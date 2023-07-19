import pygame

from dino_runner.components.enemies.enemy import Enemy
from dino_runner.utils.constants import BOMB


class Bomb(Enemy):
	def __init__(self, x, velocity):
		super().__init__(BOMB)
		self.rect.inflate_ip(-10, -10)
		self.rect.x = x
		self.rect.y = -40
		self.velocity = velocity

	def update(self):
		self.rect.x -= self.velocity
		if self.rect.y < 345:
			self.rect.y += 10
		else:
			self.kill()

import pygame.sprite

from dino_runner.components.enemies.enemy import Enemy
from dino_runner.utils.constants import BLOCK


class Block(Enemy):
	def __init__(self, x: int, velocity: int):
		super().__init__(BLOCK[0])
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

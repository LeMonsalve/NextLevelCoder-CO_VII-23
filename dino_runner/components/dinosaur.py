import pygame.sprite
from dino_runner.utils.constants import RUNNING


class Dinosaur(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.images = RUNNING
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.GROUND_LEVEL = 310
		self.is_jumping = False
		self.jump_velocity = 10
		self.gravity = 0.5
		self.y_velocity = 0
		self.jump_height = 100
		self.initial_y = self.rect.y

		self.rect.x = 100
		self.rect.y = 310

	def update(self) -> None:
		# Animation
		self.index += 1
		if self.index >= len(self.images):
			self.index = 0
		self.image = self.images[self.index]

	# TODO: Jump

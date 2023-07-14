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
		self.is_falling = False
		self.jump_velocity = 10
		self.gravity = 3
		self.y_velocity = 0
		self.jump_height = 150

		self.rect.x = 100
		self.rect.y = 310

	def update(self) -> None:
		# Animation
		self.index += 1
		if self.index >= len(self.images):
			self.index = 0
		self.image = self.images[self.index]

		# Jumping
		if self.is_jumping:
			if self.rect.top >= self.jump_height and not self.is_falling:
				self.y_velocity += self.gravity
				self.rect.y -= self.y_velocity
				if self.rect.y <= self.jump_height:
					self.is_falling = True
					self.y_velocity = 0
			else:
				if self.is_falling:
					self.y_velocity += self.gravity
					self.rect.y += self.y_velocity
					if self.rect.y >= self.GROUND_LEVEL:
						self.rect.y = self.GROUND_LEVEL
						self.is_jumping = False
						self.is_falling = False
						self.y_velocity = 0

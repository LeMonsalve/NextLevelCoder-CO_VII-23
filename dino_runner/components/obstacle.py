import pygame.sprite
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class Obstacle(pygame.sprite.Sprite):
	def __init__(self, size_index: int, type_index: int, x: int, y: int, velocity: int):
		super().__init__()
		self.image = SMALL_CACTUS[type_index] if size_index == 0 else LARGE_CACTUS[type_index]
		self.rect = self.image.get_rect()
		self.rect.inflate_ip(-10, -20)
		self.rect.x = x
		self.rect.y = y
		self.velocity = velocity

	def update(self):
		self.rect.x += self.velocity

	def check_collision(self, dinosaur):
		dino_rect = dinosaur.rect.copy()
		dino_rect.inflate_ip(-30, -30)
		return self.rect.colliderect(dino_rect)

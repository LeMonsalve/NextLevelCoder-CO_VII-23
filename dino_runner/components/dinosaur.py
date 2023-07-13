import pygame.sprite
from dino_runner.utils.constants import RUNNING


class Dinosaur(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = RUNNING
		self.rect = self.image.get_rect()
		self.image = pygame.image.load('assets/dino.png').convert_alpha()

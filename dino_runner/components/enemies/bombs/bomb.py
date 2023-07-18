import pygame

from dino_runner.utils.constants import BOMB


class Bomb(pygame.sprite.Sprite):
	def __init__(self, x, velocity):
		super().__init__()
		self.image = BOMB
		self.rect = self.image.get_rect()
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

	def check_collision(self, player):
		player_rect = player.rect.copy()
		player_rect.inflate_ip(-30, -30)
		return self.rect.colliderect(player_rect)

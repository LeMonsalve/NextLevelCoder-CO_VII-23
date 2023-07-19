import pygame.sprite

from dino_runner.utils.constants import SCREEN_WIDTH


class PowerBase(pygame.sprite.Sprite):
	def __init__(self, image, velocity):
		super().__init__()
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = SCREEN_WIDTH + (SCREEN_WIDTH / 2)
		self.rect.y = 300
		self.velocity = velocity
		self.has_been_collided = False

	def update(self, game):
		self.rect.x -= self.velocity

		self.has_been_collided = self.on_player_collision(game)

		if self.has_been_collided:
			game.player.is_invincible = True

	def draw(self, screen):
		screen.blit(self.image, self.rect)

	def on_player_collision(self, game):
		player_rect = game.player.rect.copy()
		player_rect.inflate_ip(10, 10)
		return self.rect.colliderect(player_rect)

import pygame.sprite

from dino_runner.utils.constants import SPIKES


class Spike(pygame.sprite.Sprite):
	JUMP_VELOCITY = 13
	INITIAL_Y = 550

	def __init__(self, x: int, velocity):
		super().__init__()
		self.image = SPIKES[0]
		self.rect = self.image.get_rect()
		self.rect.inflate_ip(-20, -20)
		self.rect.x = x
		self.rect.y = self.INITIAL_Y
		self.step_index = 0
		self.velocity = velocity
		self.jump_velocity = self.JUMP_VELOCITY
		self.is_jumping = False

	def update(self):
		self.rect.x -= self.velocity
		self.handle_step_index()
		self.image = SPIKES[0] if self.step_index < 5 else SPIKES[1]
		self.jump()
		self.deactivate_spike()

	def handle_step_index(self):
		self.step_index += 1
		if self.step_index >= 10:
			self.step_index = 0

	def check_collision(self, player):
		player_rect = player.rect.copy()
		player_rect.inflate_ip(-20, -20)
		return self.rect.colliderect(player_rect)

	def jump(self):
		self.rect.y -= self.jump_velocity * 4
		self.jump_velocity -= 0.8

	def deactivate_spike(self):
		if self.rect.bottom >= self.INITIAL_Y:
			self.kill()

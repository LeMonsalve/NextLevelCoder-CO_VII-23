import pygame.sprite
from dino_runner.utils.constants import PLAYER_RUNNING, PLAYER_DUCKING


class Player(pygame.sprite.Sprite):
	RECT_X = 100
	REXT_Y = 320
	GROUND_LEVEL = 320

	def __init__(self):
		super().__init__()
		self.images = PLAYER_RUNNING
		self.step_index = 0
		self.image = PLAYER_RUNNING[0]
		self.rect = self.image.get_rect()
		self.rect.inflate_ip(-20, -30)

		self.is_jumping = False
		self.is_falling = False
		self.is_ducking = False
		self.can_duck = True

		self.jump_velocity = 10
		self.gravity = 4
		self.y_velocity = 0
		self.jump_height = 100

		self.rect.x = self.RECT_X
		self.rect.y = self.REXT_Y

	def update(self, user_input) -> None:
		self.handle_input(user_input)

		# Animations
		if self.is_jumping:
			self.jump()
		elif self.is_ducking:
			self.duck()
		elif not self.is_jumping and not self.is_ducking:
			self.run()

	def draw(self, screen):
		screen.blit(self.image, self.rect)

	def run(self):
		self.step_index += 1
		if self.step_index >= 10:
			self.step_index = 0

		self.image = PLAYER_RUNNING[0] if self.step_index < 5 else PLAYER_RUNNING[1]
		self.rect = self.image.get_rect()
		self.rect.x = self.RECT_X
		self.rect.y = self.REXT_Y

	def jump(self):
		self.step_index = 0
		self.image = PLAYER_RUNNING[1]

		if self.is_jumping:
			if self.rect.top >= self.jump_height and not self.is_falling and not self.is_ducking:
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

	def duck(self):
		self.image = PLAYER_DUCKING
		self.rect = self.image.get_rect()
		self.rect.inflate_ip(0, -20)
		self.rect.x = self.RECT_X
		self.rect.y = self.REXT_Y

	def handle_input(self, user_input):
		self.can_duck = False if self.is_jumping else True

		if user_input[pygame.K_SPACE]:
			if not self.is_jumping:
				self.is_jumping = True

		if user_input[pygame.K_DOWN] and self.can_duck:
			self.is_ducking = True
		else:
			self.is_ducking = False

	def handle_step_index(self):
		self.step_index += 1
		if self.step_index >= 10:
			self.step_index = 0

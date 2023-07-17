import pygame.sprite
from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING


class Dinosaur(pygame.sprite.Sprite):
	RECT_X = 100
	REXT_Y = 310

	def __init__(self):
		super().__init__()
		self.images = RUNNING
		self.step_index = 0
		self.image = RUNNING[0]
		self.rect = self.image.get_rect()
		self.GROUND_LEVEL = 310

		self.is_jumping = False
		self.is_falling = False
		self.is_ducking = False

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

		self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
		self.rect = self.image.get_rect()
		self.rect.x = self.RECT_X
		self.rect.y = self.REXT_Y

	def jump(self):
		self.step_index = 0
		self.image = JUMPING
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
		self.handle_step_index()
		self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
		self.rect = self.image.get_rect()
		self.rect.x = self.RECT_X
		self.rect.y = self.REXT_Y + 40

	def handle_input(self, user_input):
		if user_input[pygame.K_SPACE]:
			if not self.is_jumping:
				self.is_jumping = True

		if user_input[pygame.K_DOWN]:
			self.is_ducking = True
		else:
			self.is_ducking = False

	def handle_step_index(self):
		self.step_index += 1
		if self.step_index >= 10:
			self.step_index = 0

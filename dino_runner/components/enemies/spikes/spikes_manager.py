import random

import pygame

from dino_runner.components.enemies.spikes.spike import Spike


class SpikesManager:
	def __init__(self, score_to_create=0, time_to_create=200):
		self.spikes = pygame.sprite.Group()
		self.step_index = 0
		self.score_to_create = score_to_create
		self.time_to_create = time_to_create

	def update(self, game):
		self.on_player_collision(game)
		self.handle_step_index()
		if self.step_index == 0 and game.score > self.score_to_create:
			self.create_spike(game)

		for spike in self.spikes:
			spike.update()

	def draw(self, screen):
		self.spikes.draw(screen)

	def create_spike(self, game):
		x_position = game.player.rect.x + random.randint(200, 800)
		spike = Spike(x_position, game.game_speed)
		self.spikes.add(spike)

	def on_player_collision(self, game):
		for spike in self.spikes:
			has_collisioned = spike.check_collision(game.player)
			if has_collisioned:
				game.game_over = True
				break

	def handle_step_index(self):
		self.step_index += 1
		if self.step_index >= self.time_to_create:
			self.step_index = 0

	def reset(self):
		self.spikes.empty()
		self.step_index = 0

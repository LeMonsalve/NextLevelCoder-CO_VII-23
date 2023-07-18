import random

import pygame

from dino_runner.components.enemies.bombs.bomb import Bomb
from dino_runner.utils.constants import SCREEN_WIDTH


class BombsManager:
	def __init__(self, score_to_create=0, time_to_create=150):
		self.bombs = pygame.sprite.Group()
		self.score_to_create = score_to_create
		self.step_index = 0
		self.time_to_create = time_to_create

	def update(self, game):
		self.on_player_collision(game)

		if len(self.bombs) == 0 and game.score > self.score_to_create:
			self.handle_step_index()
			if self.step_index == 0:
				self.create_bomb(game)

		for bomb in self.bombs:
			bomb.update()

	def draw(self, screen):
		self.bombs.draw(screen)

	def create_bomb(self, game):
		random_x = random.randint(600, SCREEN_WIDTH)
		velocity = random.uniform(0.5, 1.5)
		bomb = Bomb(random_x, game.game_speed * velocity)
		self.bombs.add(bomb)

	def on_player_collision(self, game):
		for bomb in self.bombs:
			has_collisioned = bomb.check_collision(game.player)
			if has_collisioned:
				game.playing = False
				break

	def handle_step_index(self):
		self.step_index += 1
		if self.step_index >= self.time_to_create:
			self.step_index = 0

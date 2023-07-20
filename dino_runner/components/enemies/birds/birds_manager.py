import random

import pygame.sprite

from dino_runner.components.enemies.birds.bird import Bird
from dino_runner.utils.constants import SCREEN_WIDTH, BIRD


class BirdsManager:
	def __init__(self, score_to_start: int = 0):
		self.birds = pygame.sprite.Group()
		self.score_to_start = score_to_start

	def update(self, game):
		self.on_player_collision(game.player, game)

		if len(self.birds) == 0 and game.score > self.score_to_start:
			self.create_birds(game)

		for obstacle in self.birds:
			obstacle.update()
			self.remove_bird(obstacle)

	def draw(self, screen):
		self.birds.draw(screen)

	def create_birds(self, game):
		birds_count = random.randint(6, 10)
		separation = SCREEN_WIDTH + 10
		for o in range(birds_count):
			if o != 0:
				separation += random.randint(600, 800)
			y_position = random.randint(200, 300)
			bird = Bird(BIRD, separation, y_position, game.game_speed * -1)
			self.birds.add(bird)

	def remove_bird(self, obstacle):
		if obstacle.rect.right < 0:
			self.birds.remove(obstacle)

	def on_player_collision(self, player, game):
		for bird in self.birds:
			has_collisioned = bird.check_collision(player)
			if has_collisioned:
				game.game_over = True
				break

	def reset(self):
		self.birds.empty()


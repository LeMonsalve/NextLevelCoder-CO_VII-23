import random

import pygame.sprite

from dino_runner.components.obstacle import Obstacle
from dino_runner.utils.constants import SCREEN_WIDTH


class ObstacleManager:
	def __init__(self):
		self.obstacles = pygame.sprite.Group()

	def update(self, dino, game):
		self.on_dino_collision(dino, game)

		if len(self.obstacles) == 0:
			self.create_obstacle(game)

		for obstacle in self.obstacles:
			obstacle.update()
			self.remove_obstacle(obstacle)

	def draw(self, screen):
		self.obstacles.draw(screen)

	def create_obstacle(self, game):
		obstacle_count = random.randint(6, 10)
		separation = SCREEN_WIDTH + 10
		for o in range(obstacle_count):
			if o != 1:
				separation += random.randint(400, 600)
			random_size = random.randint(0, 1)
			random_type = random.randint(0, 2)
			y_position = 330 if random_size == 0 else 305
			obstacle = Obstacle(random_size, random_type, separation, y_position, game.game_speed * -1)
			self.obstacles.add(obstacle)

	def remove_obstacle(self, obstacle):
		if obstacle.rect.right < 0:
			self.obstacles.remove(obstacle)

	def on_dino_collision(self, dino, game):
		for obstacle in self.obstacles:
			has_collisioned = obstacle.check_collision(dino)
			if has_collisioned:
				game.playing = False
				break

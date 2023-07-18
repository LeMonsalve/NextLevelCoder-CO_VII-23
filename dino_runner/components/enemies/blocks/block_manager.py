import pygame

from dino_runner.components.enemies.blocks.block import Block
from dino_runner.utils.constants import SCREEN_WIDTH


class BlocksManager:
	def __init__(self, score_to_create=0, time_to_create=50):
		self.blocks = pygame.sprite.Group()
		self.step_index = 0
		self.score_to_create = score_to_create
		self.time_to_create = time_to_create

	def update(self, game):
		self.on_player_collision(game)
		self.handle_step_index()
		if self.step_index == 0 and game.score > self.score_to_create:
			self.create_block(game)
		for block in self.blocks:
			block.update()

	def draw(self, screen):
		self.blocks.draw(screen)

	def on_player_collision(self, game):
		for block in self.blocks:
			has_collisioned = block.check_collision(game.player)
			if has_collisioned:
				game.playing = False
				break

	def handle_step_index(self):
		self.step_index += 1
		if self.step_index >= self.time_to_create:
			self.step_index = 0

	def create_block(self, game):
		block = Block(SCREEN_WIDTH + 10, game.game_speed * -1)
		self.blocks.add(block)

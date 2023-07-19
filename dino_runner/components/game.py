import pygame

from dino_runner.components.enemies.blocks.block_manager import BlocksManager
from dino_runner.components.enemies.bombs.bombs_manager import BombsManager
from dino_runner.components.enemies.spikes.spikes_manager import SpikesManager
from dino_runner.components.objects.clouds_manager import CloudsManager
from dino_runner.components.player import Player
from dino_runner.components.enemies.birds.birds_manager import BirdsManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
	SCORE_FILE = "high_score.txt"

	def __init__(self):
		pygame.init()
		pygame.display.set_caption(TITLE)
		pygame.display.set_icon(ICON)
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		self.clock = pygame.time.Clock()
		self.playing = False
		self.game_speed = 20
		self.x_pos_bg = 0
		self.y_pos_bg = 390
		self.score = 0
		self.high_score = self.load_high_score()
		self.player = Player()
		self.clouds_manager = CloudsManager()

		# Enemies Managers
		self.blocks_manager = BlocksManager(0)
		self.bombs_manager = BombsManager(150)
		self.birds_manager = BirdsManager(50)
		self.spikes_manager = SpikesManager(80)

		# Power Ups Manager
		self.power_up_manager = PowerUpManager()

	def run(self):
		# Game loop: events - update - draw
		self.playing = True
		while self.playing:
			self.events()
			self.update()
			self.draw()
		self.save_high_score()
		pygame.quit()

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.playing = False

	def update(self):
		self.game_speed += 0.001
		self.score += 0.05
		self.player.update(pygame.key.get_pressed())
		self.power_up_manager.update(self)
		self.blocks_manager.update(self)
		self.birds_manager.update(self)
		self.bombs_manager.update(self)
		self.spikes_manager.update(self)
		self.clouds_manager.update()

	def draw(self):
		self.clock.tick(FPS)
		self.screen.fill((255, 255, 255))
		self.draw_background()
		self.player.draw(self.screen)
		self.blocks_manager.draw(self.screen)
		self.power_up_manager.draw(self.screen)
		self.birds_manager.draw(self.screen)
		self.bombs_manager.draw(self.screen)
		self.spikes_manager.draw(self.screen)
		self.clouds_manager.draw(self.screen)
		self.draw_score()
		self.draw_high_score()
		pygame.display.update()
		pygame.display.flip()

	def draw_background(self):
		image_width = BG.get_width()
		self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
		self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
		if self.x_pos_bg <= -image_width:
			self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
			self.x_pos_bg = 0
		self.x_pos_bg -= self.game_speed

	def draw_score(self):
		font = pygame.font.Font(pygame.font.get_default_font(), 16)
		text = font.render(f"Score: {int(self.score)}", True, (0, 0, 0))
		text_rect = text.get_rect()
		text_rect.center = (SCREEN_WIDTH - 50, 20)
		self.screen.blit(text, text_rect)

	def draw_high_score(self):
		font = pygame.font.Font(pygame.font.get_default_font(), 16)
		text = font.render(f"High Score: {int(self.high_score)}", True, (0, 0, 0))
		text_rect = text.get_rect()
		text_rect.topleft = (10, 20)
		self.screen.blit(text, text_rect)

	def load_high_score(self):
		try:
			with open(self.SCORE_FILE, "r") as file:
				high_score = float(file.read())
		except FileNotFoundError:
			high_score = 0.0
		return high_score

	def save_high_score(self):
		if self.score > self.high_score:
			self.high_score = self.score
			with open(self.SCORE_FILE, "w") as file:
				file.write(str(self.high_score))

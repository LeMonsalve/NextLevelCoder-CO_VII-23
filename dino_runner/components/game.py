import pygame

from dino_runner.components.enemies.blocks.block_manager import BlocksManager
from dino_runner.components.enemies.bombs.bombs_manager import BombsManager
from dino_runner.components.enemies.spikes.spikes_manager import SpikesManager
from dino_runner.components.objects.clouds_manager import CloudsManager
from dino_runner.components.player import Player
from dino_runner.components.enemies.birds.birds_manager import BirdsManager
from dino_runner.components.power_ups.invincible.invincible_manager import InvincibleManager
from dino_runner.components.power_ups.invincible.invincible_powerup import InvinciblePowerUp
from dino_runner.components.power_ups.snow.snow_powerup import SnowPowerUp
from dino_runner.components.power_ups.snow.snow_manager import SnowManager
from dino_runner.utils.constants import (
	BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, SNOW, LM_SHIELD, BACKGROUND_MUSIC, DEATH_SOUND, POWER_UP_SOUND
)


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
		self.game_over = False

		self.clouds_manager = CloudsManager()

		# Enemies Managers
		self.blocks_manager = BlocksManager()
		self.bombs_manager = BombsManager(40)
		self.birds_manager = BirdsManager(80)
		self.spikes_manager = SpikesManager(120)

		# Power Ups Manager
		self.snow_manager = SnowManager()
		self.invincible_manager = InvincibleManager()

		# Snow
		self.snow_powered = False
		self.snow_powered_timer = 0
		self.snow_powered_duration = 300

		# Invincibility
		self.invincible_active = False
		self.invincible_powered = False
		self.invincible_powered_timer = 0
		self.invincible_powered_duration = 400

		self.player = Player(self.invincible_powered_duration)

		# Music
		pygame.mixer.music.load(BACKGROUND_MUSIC)
		pygame.mixer.init()
		pygame.mixer.music.play(-1)
		pygame.mixer.music.set_volume(0.3)

	def run(self):
		# Game loop: events - update - draw
		self.playing = True
		while self.playing:
			if self.game_over:
				self.game_over_screen()
			else:
				self.events()
				self.update()
				self.draw()
		pygame.quit()

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.playing = False

	def update(self):
		self.game_speed += 0.001
		self.score += 0.05
		self.player.update(pygame.key.get_pressed(), self)
		self.snow_manager.update(self)
		self.invincible_manager.update(self)
		self.blocks_manager.update(self)
		self.birds_manager.update(self)
		self.bombs_manager.update(self)
		self.spikes_manager.update(self)
		self.clouds_manager.update()

		power_up_collisions = pygame.sprite.spritecollide(self.player, self.snow_manager.power_ups, True)
		if power_up_collisions:
			for power_up in power_up_collisions:
				if isinstance(power_up, SnowPowerUp):
					pygame.mixer.Sound(POWER_UP_SOUND).play()
					self.snow_powered = True
					self.snow_powered_timer = 0

		invincible_power_up_collisions = pygame.sprite.spritecollide(self.player,
																	 self.invincible_manager.invincible_power_ups,
																	 True)
		if invincible_power_up_collisions and not self.invincible_active:
			for power_up in invincible_power_up_collisions:
				if isinstance(power_up, InvinciblePowerUp):
					pygame.mixer.Sound(POWER_UP_SOUND).play()
			self.player.make_invincible()
			self.invincible_active = True

		if self.snow_powered:
			self.game_speed = 10
			self.snow_powered_timer += 1
			if self.snow_powered_timer >= self.snow_powered_duration:
				self.snow_powered = False
				self.game_speed = 20

		if self.player.is_invincible:
			self.invincible_powered_timer += 1
			self.invincible_powered = True

		if not self.player.is_invincible:
			self.invincible_powered_timer = 0
			self.invincible_powered = False
			self.invincible_active = False

	def draw(self):
		self.clock.tick(FPS)
		self.screen.fill((255, 255, 255))
		self.draw_background()
		self.player.draw(self.screen)
		self.blocks_manager.draw(self.screen)
		self.birds_manager.draw(self.screen)
		self.bombs_manager.draw(self.screen)
		self.spikes_manager.draw(self.screen)
		self.snow_manager.draw(self.screen)
		self.invincible_manager.draw(self.screen)
		self.clouds_manager.draw(self.screen)
		self.draw_score()
		self.draw_high_score()
		self.draw_active_powerups()
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

	def draw_active_powerups(self):
		if self.snow_powered:
			self.screen.blit(SNOW, (SCREEN_WIDTH // 2, 10))
			snow_powered_time_left = max(0, self.snow_powered_duration - self.snow_powered_timer)
			snow_powered_time_seconds = round(snow_powered_time_left / FPS, 1)
			font = pygame.font.Font(pygame.font.get_default_font(), 16)
			text = font.render(f"{snow_powered_time_seconds} s", True, (0, 0, 0))
			text_rect = text.get_rect()
			text_rect.topleft = (SCREEN_WIDTH // 2 + 5, 50)
			self.screen.blit(text, text_rect)

		if self.invincible_powered:
			self.screen.blit(LM_SHIELD, (SCREEN_WIDTH // 2 - 38, 10))
			invincible_powered_time_left = max(0, self.invincible_powered_duration - self.invincible_powered_timer)
			invincible_powered_time_seconds = round(invincible_powered_time_left / FPS, 1)
			font = pygame.font.Font(pygame.font.get_default_font(), 16)
			text = font.render(f"{invincible_powered_time_seconds} s", True, (0, 0, 0))
			text_rect = text.get_rect()
			text_rect.topleft = (SCREEN_WIDTH // 2 - 38, 50)
			self.screen.blit(text, text_rect)

	def game_over_screen(self):
		pygame.mixer.music.set_volume(0.1)
		pygame.mixer.Sound(DEATH_SOUND).play()

		font = pygame.font.Font(pygame.font.get_default_font(), 32)
		game_over_text = font.render("Game Over", True, (255, 0, 0))
		game_over_rect = game_over_text.get_rect()
		game_over_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80)

		score_text = font.render(f"Score: {int(self.score)}", True, (255, 0, 0))
		score_rect = score_text.get_rect()
		score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40)

		high_score_text = font.render(f"High Score: {int(self.high_score)}", True, (255, 0, 0))
		high_score_rect = high_score_text.get_rect()
		high_score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

		restart_text = font.render(f"-> Press any KEY to restart <-", True, (0, 255, 0))
		restart_rect = restart_text.get_rect()
		restart_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)

		self.screen.blit(game_over_text, game_over_rect)
		self.screen.blit(score_text, score_rect)
		self.screen.blit(high_score_text, high_score_rect)
		self.screen.blit(restart_text, restart_rect)

		pygame.display.update()

		waiting_for_key = True
		while waiting_for_key:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.playing = False
					waiting_for_key = False
				if event.type == pygame.KEYDOWN:
					waiting_for_key = False
					self.reset_game()

	def reset_game(self):
		self.game_speed = 20
		self.x_pos_bg = 0
		self.score = 0
		self.snow_powered = False
		self.snow_powered_timer = 0
		self.invincible_active = False
		self.invincible_powered_timer = 0
		self.playing = True
		self.game_over = False

		self.clear_obstacles()
		self.snow_manager.reset()
		self.invincible_manager.reset()
		self.player.reset()

		self.playing = True

		pygame.mixer.music.set_volume(0.3)

		self.run()

	def clear_obstacles(self):
		self.blocks_manager.reset()
		self.bombs_manager.reset()
		self.birds_manager.reset()
		self.spikes_manager.reset()

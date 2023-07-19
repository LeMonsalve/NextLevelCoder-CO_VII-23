import pygame.sprite

from dino_runner.components.power_ups.shield import Shield


class PowerUpManager:
	def __init__(self):
		self.has_powerup = False
		self.power_up = None
		self.timer = 0
		self.power_up_time = 400

	def update(self, game):
		self.handle_timer()
		print(game.player.is_invincible)

		if self.timer == 1 and not game.player.is_invincible:
			self.power_up = Shield(game.game_speed)
			self.has_powerup = True

		if game.player.is_invincible and self.power_up_time == 0:
			game.player.is_invincible = False

		if self.has_powerup:
			self.power_up.update(game)
			self.has_powerup = not self.power_up.on_player_collision(game)

		if game.player.is_invincible:
			self.handle_power_up_timer()

	def draw(self, screen):
		if self.has_powerup:
			self.power_up.draw(screen)

	def handle_timer(self):
		self.timer -= 1
		if self.timer <= 0:
			self.timer = 300

	def handle_power_up_timer(self):
		self.power_up_time += 1
		if self.power_up_time > 400:
			self.power_up_time = 0

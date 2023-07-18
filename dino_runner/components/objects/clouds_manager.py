import pygame

from dino_runner.components.objects.cloud import Cloud


class CloudsManager:
	def __init__(self):
		self.clouds = pygame.sprite.Group()
		self.timer = 0
		self.interval = 30

	def update(self):
		self.timer += 0.5
		if self.timer >= self.interval:
			self.create_cloud()
			self.timer = 0

		for cloud in self.clouds:
			cloud.update()

	def create_cloud(self):
		cloud = Cloud()
		self.clouds.add(cloud)

	def draw(self, screen):
		self.clouds.draw(screen)

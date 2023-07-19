import pygame.sprite


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

    def update(self):
        pass

    def check_collision(self, player):
        if player.is_invincible:
            return False
        player_rect = player.rect.copy()
        player_rect.inflate_ip(-30, -30)
        return self.rect.colliderect(player_rect)

import pygame
import os

# Global Constants
TITLE = "Next Level Coder CO"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
NEWER_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "Newer")
MUSIC_DIR = os.path.join(os.path.dirname(__file__), "..", "sounds")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
	pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
	pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
	pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
	pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
	pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
	pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
	pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
	pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
	pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
	pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
	pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
	pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
	pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
	pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
	pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
	pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
	pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
	pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

# My Own
PLAYER_RUNNING = [
	pygame.image.load(os.path.join(NEWER_DIR, 'Characters/Players/blue_0.png')),
	pygame.image.load(os.path.join(NEWER_DIR, 'Characters/Players/blue_1.png')),
]

PLAYER_DUCKING = pygame.image.load(os.path.join(NEWER_DIR, 'Characters/Players/blue_2.png'))

BIRD = [
	pygame.image.load(os.path.join(NEWER_DIR, "Characters/Enemies/bird_0.png")),
	pygame.image.load(os.path.join(NEWER_DIR, "Characters/Enemies/bird_1.png")),
	pygame.image.load(os.path.join(NEWER_DIR, "Characters/Enemies/bird_2.png")),
]

BG = pygame.image.load(os.path.join(NEWER_DIR, 'floor.png'))

CLOUD = pygame.image.load(os.path.join(NEWER_DIR, 'cloud.png'))

BOMB = pygame.image.load(os.path.join(NEWER_DIR, 'Characters/Enemies/bomb.png'))

SPIKES = [
	pygame.image.load(os.path.join(NEWER_DIR, 'Characters/Enemies/spike_0.png')),
	pygame.image.load(os.path.join(NEWER_DIR, 'Characters/Enemies/spike_1.png')),
]

BLOCK = [
	pygame.image.load(os.path.join(NEWER_DIR, 'Characters/Enemies/block_0.png')),
	pygame.image.load(os.path.join(NEWER_DIR, 'Characters/Enemies/block_1.png')),
]

SNOW = pygame.image.load(os.path.join(NEWER_DIR, 'snow_body.png'))

LM_SHIELD = pygame.image.load(os.path.join(NEWER_DIR, 'shield.png'))

BACKGROUND_MUSIC = os.path.join(MUSIC_DIR, 'background.wav')
POWER_UP_SOUND = os.path.join(MUSIC_DIR, 'power_up.wav')
DEATH_SOUND = os.path.join(MUSIC_DIR, 'death.mp3')
JUMP_SOUND = os.path.join(MUSIC_DIR, 'jump.mp3')
BOMB_SOUND = os.path.join(MUSIC_DIR, 'bomb.mp3')

DEFAULT_TYPE = "default"

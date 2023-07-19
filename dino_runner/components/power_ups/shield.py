from dino_runner.components.power_ups.power_base import PowerBase
from dino_runner.utils.constants import SHIELD


class Shield(PowerBase):
	def __init__(self, game_speed):
		super().__init__(SHIELD, game_speed)

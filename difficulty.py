import pygame.font

class DifficultyButton:

	def __init__(self, ai_game, msg):
		"""Initialize difficulty button attributes."""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set dimension and properties for button

		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_Color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# Build buttons rect object and place it

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.left = self.screen_rect.left

		self._prep_msg(msg)



	def _prep_msg(self, msg):
		"""Turn msg into rendered image and align to left"""
		self.msg_image = self.font.render(msg, True, self.text_Color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.left = self.rect.left

	def draw_button(self):
		# Draw a blank button then draw message
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
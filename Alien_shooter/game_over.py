import pygame.font

class GameOver:
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.SysFont(None, 96)
        self.text_color = (200, 0, 0)
        self.prep_msg()

    def prep_msg(self):
        self.msg_image = self.font.render("GAME OVER", True, self.text_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.screen_rect.center

    def draw(self):
        self.screen.blit(self.msg_image, self.msg_rect)

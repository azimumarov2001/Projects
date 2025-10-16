import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from game_over import GameOver

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    game_over_text = GameOver(ai_settings, screen)

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets, play_button, aliens, stats)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)

        else:
            if stats.ships_left == 0:
                game_over_text.draw()

        gf.update_screen(ai_settings, screen, ship, aliens, bullets, play_button, stats, sb)

if __name__ == '__main__':
    run_game()


import sys
import time
import pygame


def show_score(position: tuple, color, font: str, size: int, score: int, window):
    score_font= pygame.font.SysFont(font, size)
    score_surface = score_font.render("score: " + str(score), True, color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (position[0], position[1])
    window.blit(score_surface, score_rect)

def game_over_screen(frame_size_x, frame_size_y, game_window, score):
    font_color = pygame.color(250, 60, 60)
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('Oh no, Too Bad', True, font_color)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(pygame.color(20, 20, 20))
    game_window.blit(game_over_surface, game_over_rect)
    show_score((frame_size_x/2, frame_size_y/1.25), font_color, 'times', 20, score, game_window)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    sys.exit()
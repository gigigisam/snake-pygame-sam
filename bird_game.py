"""
Modified version of snake game made with pygame
To become a "bird game"
"""

import pygame, sys, time, random

# define constants
refresh_speed = 30
frame_size_x = 1200
frame_size_y = 700
bird_color = pygame.color(200, 120, 80)
sky_color = pygame.color(50, 50, 225)
food_color_1 = pygame.color(50, 150, 5)
food_color_2 = pygame.color(180, 50, 5)
tree_color = pygame.color(180, 80, 120)

check_errors = pygame.init()

if check_errors[1] > 0:
    print(f"[+] Had {check_errors[1]} errors when initialising game!")
    sys.exit(-1)
else:
    print("[+] Game successfully initialized.")

pygame.display.set_caption("Hungry Birdy")
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

fps_controller = pygame.time.Clock()

# global variables for game running:
bird_position = [int(frame_size_x/2), int(frame_size_y/2)]
bird_body_size = 10

food_pos_1 = [random.randrange(20, frame_size_x - 20), random.randrange(20, frame_size_y - 20)]
food_pos_2 = [random.randrange(20, frame_size_x - 20), random.randrange(20, frame_size_y - 20)]
food_1_spawned = True
food_2_spawned = True
move_direction = "RIGHT"
score = 0

# main game loop
while True:
    print("Hahaha")
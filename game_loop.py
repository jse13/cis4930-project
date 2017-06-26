"""
This module controls the main control flow of the game.
"""
import pygame
import constants as C
#from resources import Resources


def game_loop(res):
    """
    Manager function that's going to be called from the start.py module.
    """


    loop = True

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:

                    # Player movement
                    if res.player.y_change == 0:
                        res.player.y_change -= C.SPRITE_BASE_SPEED

                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:

                    # Player movement
                    if res.player.x_change == 0:
                        res.player.x_change -= C.SPRITE_BASE_SPEED

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:

                    # Player movement
                    if res.player.y_change == 0:
                        res.player.y_change += C.SPRITE_BASE_SPEED

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:

                    # Player movement
                    if res.player.x_change == 0:
                        res.player.x_change += C.SPRITE_BASE_SPEED

                elif event.key == pygame.K_RETURN:
                    print("foo")
                elif event.key == pygame.K_ESCAPE:
                    print("foo")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_w:

                    # Player movement
                    res.player.y_change = 0

                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:

                    # Player movement
                    res.player.x_change = 0

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:

                    # Player movement
                    res.player.y_change = 0

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:

                    # Player movement
                    res.player.x_change = 0


        C.GAME_DISPLAY.fill(C.WHITE)
        C.BACKGROUND.fill(C.WHITE)

        res.g_all_sprites.clear(C.GAME_DISPLAY, C.BACKGROUND)
        res.g_player_sprites.update()
        res.g_all_sprites.draw(C.GAME_DISPLAY)

        pygame.display.update()
        C.CLOCK.tick(60)
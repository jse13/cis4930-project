"""
This module controls the main control flow of the game.

start.py calls this module after running the main_menu
module and after generating a resource object.

This module handles things like drawing the room, player
movement, enemy movement, attacking, calling the pause
menu, etc.
"""
import pygame
import constants as C
import pause_menu
import generate_room
import items
import random
from resources import Ghost


def game_loop(res):
    """
    Manager function that's going to be called from the start.py module.
    """

    # Start the music
    pygame.mixer.music.load(C.MUS_LEVEL_MUSIC)
    pygame.mixer.music.set_volume(C.LEVEL_MUSIC_VOL)
    # Loop indefinitely
    pygame.mixer.music.play(-1)

    sfx_menu_open = pygame.mixer.Sound(C.SFX_MENU_OPEN)


    # Pause menu cooldown; that way holding esc after leaving doesn't make it
    # reappear instantly
    pause_cooldown = 0.0


    loop = True
    milliseconds = 0
    seconds = 0
    
    ghostReload = C.GHOST_RELOAD

    # Initial draw
    C.G_ITEMS.draw(C.GAME_DISPLAY)

    while loop:

        #print("x: "+str(res.player.x)+" y:"+str(res.player.y))

        milliseconds = C.CLOCK.tick(60)
        seconds = milliseconds/100.0

        '''keys is a dict with entries of {pygame.K_<key>, boolean}
        to tell whether any key is held down each frame'''
        keys = pygame.key.get_pressed()

        #player movement
        #check if a key is being held, update the player.pos tuple
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            res.player.move(C.RIGHT, seconds)

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            res.player.move(C.LEFT, seconds)

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:

            res.player.move(C.DOWN, seconds)

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            res.player.move(C.UP, seconds)


        '''This checks the boundaries. First two checks y cooridnates.
        Last two check the x coordiantes'''
        if (res.player.pos[0] > C.DISPLAY_WIDTH):
            res.nextRoom("right")
            res.player.x -= C.DISPLAY_WIDTH - 96

        if (res.player.pos[0] < 0):
            res.nextRoom("left")
            res.player.x += C.DISPLAY_WIDTH - 96

        if (res.player.pos[1] < 0):
            res.nextRoom("top")
            res.player.y += C.DISPLAY_HEIGHT - 96

        if (res.player.pos[1] > C.DISPLAY_HEIGHT - 32):
            res.nextRoom("bot")
            res.player.y -= C.DISPLAY_HEIGHT - 96

        '''
        depending on how we want them to be handled in the game, keyboard
        controls besides those relating to movement may need to be put in
        the event loop
        i.e. swing a sword could be detected by key_down event and have an
        attack speed related cooldown, rather then checking if the key is held
        '''
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
            res.player.attack()
        if keys[pygame.K_ESCAPE]:
            if pause_cooldown <= 0.0:
                pause_cooldown = C.PAUSE_COOLDOWN
                pygame.mixer.music.pause()
                sfx_menu_open.play()
                pause_menu.pause_menu(C.GAME_DISPLAY)
                pygame.mixer.music.unpause()
            else:
                pause_cooldown -= seconds

        #check for other events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
         #Reloading ghosts
        if ghostReload == 0:
            ghostReload = ghostReload - 1
        #Getting the odds of a ghost showing up, so they show up at random intervals
        elif not int (random.random() * C.GHOST_SHOWS):
            g = Ghost(C.DISPLAY_WIDTH, C.DISPLAY_HEIGHT)
            ghostReload = C.GHOST_RELOAD

        C.G_BELOW_TILES.clear(C.GAME_DISPLAY, C.BACKGROUND)
        C.G_BELOW_TILES.update(seconds)
        C.G_BELOW_TILES.draw(C.GAME_DISPLAY)

        C.G_PLAYER_SPRITE.update(seconds)
        C.G_ENEMY_SPRITE.update(seconds, res.player.pos[0], res.player.pos[1])

        C.G_ITEMS.clear(C.GAME_DISPLAY, C.BACKGROUND)
        C.G_ITEMS.update(seconds)
        C.G_ITEMS.draw(C.GAME_DISPLAY)

        C.G_PLAYER_SPRITE.draw(C.GAME_DISPLAY)
        C.G_ENEMY_SPRITE.draw(C.GAME_DISPLAY)

        C.G_ABOVE_TILES.clear(C.GAME_DISPLAY, C.BACKGROUND)
        C.G_ABOVE_TILES.update(seconds)
        C.G_ABOVE_TILES.draw(C.GAME_DISPLAY)

        pygame.display.flip()

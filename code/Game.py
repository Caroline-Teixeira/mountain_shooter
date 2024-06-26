# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame as pygame
# from pygame import Surface, Rect
# from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):  # construtor
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # tamanho da janela

    def run(self):  # loop da janela
        while True:
            menu = Menu(self.window)  # criação do objeto menu
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:  # se selecionar as opções do menu
                player_score = [0, 0]  # uma posição para cada jogador
                level = Level(self.window, 'Level1', menu_return, player_score)  # cria uma nova fase
                level_return = level.run(player_score)
                if level_return:  # passou de fase
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)

            else:  # se selecionar o EXIT
                pygame.quit()
                sys.exit()

# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_RED, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    # Desenho na tela
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/menu_bg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):  # laço para ficar desenhando a imagem infinitamente
        pygame.mixer_music.load('./asset/menu.wav')
        pygame.mixer_music.play(-1)  # música (toca infinitamente)
        pygame.mixer_music.set_volume(0.3)
        menu_option = 0  # seleção do menu

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_RED, ((WIN_WIDTH / 2), 70))  # Texto do menu
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))  # Texto do menu

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 30 * i))

            pygame.display.flip()  # para atualizar a tela

            # Eventos do teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # para fechar a janela e encerrar corretamente
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:  # testa se alguma tecla foi pressionada
                    if event.key == pygame.K_DOWN:  # tecla para baixo foi pressionada
                        if menu_option < len(MENU_OPTION) - 1:  # menu rotacional
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:  # tecla para cima foi pressionada
                        if menu_option > 0:  # menu rotacional
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:  # tecla para ENTER foi pressionada
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

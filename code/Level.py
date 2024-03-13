#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code import Entity
from code.Const import COLOR_WHITE, MENU_OPTION, EVENT_ENEMY
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator


class Level:
    def __init__(self, window, name, menu_option):  # criação do objeto
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # opção do menu
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))  # carrega o BG
        self.entity_list.append(EntityFactory.get_entity('Player1'))  # carrega o jogador
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 4000)  # geração de inimigos

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.wav')
        pygame.mixer_music.play(-1)  # música (toca infinitamente)
        pygame.mixer_music.set_volume(0.3)
        clock = pygame.time.Clock()  # velocidade das imagens

        while True:
            clock.tick(60)  # FPS
            for ent in self.entity_list:  # desenho
                self.window.blit(source=ent.surf, dest=ent.rect)  # aqui eu desenho minhas entidades
                ent.move()  # movimento da imagem
                # print(clock.get_fps())  # verificar o FPS

            # Texto para ser exibido na tela
            self.level_text(14, f'fps:{clock.get_fps() :.0f}', COLOR_WHITE, (10, 10))
            self.level_text(14, f'entidades:{len(self.entity_list)}', COLOR_WHITE, (10, 25))
            pygame.display.flip()  # Atualiza a tela

            # verificar relacionamentos de entidades
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            for event in pygame.event.get():  # EVENTOS
                if event.type == pygame.QUIT:  # para fechar a janela e encerrar corretamente
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:  # geração de inimigos randômicos
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))  # adicione uma nova entidade na lista

        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

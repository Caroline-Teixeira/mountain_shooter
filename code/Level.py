#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code import Entity
from code.Const import COLOR_WHITE, MENU_OPTION, EVENT_ENEMY, WIN_HEIGHT, COLOR_GREEN, COLOR_CYAN, EVENT_TIMEOUT, \
    COLOR_YELLOW
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, menu_option: str, player_score: list[int]):  # criação do objeto
        self.window = window
        self.name = name
        self.mode = menu_option  # opção do menu
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))  # carrega o BG
        # self.entity_list.append(EntityFactory.get_entity('Player1'))  # carrega o jogador

        # carrega o jogador 1
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]  # score do jogador 1
        self.entity_list.append(player)

        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            # carrega o jogador 2
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]  # score do jogador 1
            self.entity_list.append(player)

        # geração de inimigos
        pygame.time.set_timer(EVENT_ENEMY, 4000)
        self.timeout = 40000
        pygame.time.set_timer(EVENT_TIMEOUT, 100)  # verifica a condição de vitória da fase

    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.wav')
        pygame.mixer_music.play(-1)  # música (toca infinitamente)
        pygame.mixer_music.set_volume(0.3)
        clock = pygame.time.Clock()  # velocidade das imagens

        while True:
            clock.tick(60)  # FPS
            for ent in self.entity_list:  # desenho
                self.window.blit(source=ent.surf, dest=ent.rect)  # aqui eu desenho minhas entidades
                ent.move()  # movimento da imagem

                if isinstance(ent, (Player, Enemy)):  # entidades que podem atirar
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)  # tiros
                # print(clock.get_fps())  # verificar o FPS

                # barra de vida
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health:  {ent.health} | Score: {ent.score}', COLOR_GREEN, (10, 10))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health:  {ent.health} | Score: {ent.score}', COLOR_CYAN, (10, 30))

            # Texto para ser exibido na tela
            self.level_text(14, f'{self.name} - Time {self.timeout / 1000:.1f} s', COLOR_YELLOW, (10, 45))
            self.level_text(14, f'fps:{clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades:{len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()  # Atualiza a tela

            # verificar relacionamentos de entidades
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            # EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # para fechar a janela e encerrar corretamente
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:  # geração de inimigos randômicos
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))  # adicione uma nova entidade na lista

                if event.type == EVENT_TIMEOUT:  # que acontece a cada 100 milliseconds
                    self.timeout -= 100  # começa com 20000
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score  # score acumulado
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score  # score acumulado
                        return True  # final da fase

                found_player = False  # para verificar se o jogar ainda está vivo
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:  # jogador foi morto
                    return False

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

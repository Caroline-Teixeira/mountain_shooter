#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH, ENTITY_SPEED, PLAYER_KEY_UP, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, \
    PLAYER_KEY_DOWN, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):  # movimentos da nave
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:  # tecla para cima
            self.rect.centery -= ENTITY_SPEED[self.name]  # em relação ao centro do y
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:  # tecla para baixo
            self.rect.centery += ENTITY_SPEED[self.name]  # em relação ao centro do y
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:  # tecla para direita
            self.rect.centerx += ENTITY_SPEED[self.name]  # em relação ao centro do x
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:  # tecla para esquerda
            self.rect.centerx -= ENTITY_SPEED[self.name]  # em relação ao centro do x

    # pressed_key = pygame.key.get_pressed()
    #        if pressed_key[pygame.K_UP] and self.rect.top > 0:  # tecla para cima
    #            self.rect.centery -= ENTITY_SPEED[self.name]  # em relação ao centro do y
    #        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:  # tecla para baixo
    #            self.rect.centery += ENTITY_SPEED[self.name]  # em relação ao centro do y
    #        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:  # tecla para direita
    #            self.rect.centerx += ENTITY_SPEED[self.name]  # em relação ao centro do x
    #        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:  # tecla para esquerda
    #            self.rect.centerx -= ENTITY_SPEED[self.name]  # em relação ao centro do x

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:  # tiro do jogadores
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
            else:
                return None
        else:
            return None

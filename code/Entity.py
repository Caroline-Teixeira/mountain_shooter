#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame

from code.Const import ENTITY_HEALTH


class Entity(ABC):  # classe abstrata
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()  # o alfa aumenta velocidade
        self.rect = self.surf.get_rect(left=position[0], top=position[1])  # desenho da imagem da fase 1
        self.speed = 0  # movimento das imagens
        self.health = ENTITY_HEALTH[self.name]

    @abstractmethod
    def move(self):
        pass

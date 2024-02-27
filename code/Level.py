#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface

from code import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):  # criação do objeto
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # opção do menu
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        pygame.mixer_music.load('./asset/fase1.wav')
        pygame.mixer_music.play(-1)  # música (toca infinitamente)
        pygame.mixer_music.set_volume(0.3)

        while True:  # desenho
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()  # movimento da imagem
            pygame.display.flip()
        pass

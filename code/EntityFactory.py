#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod  # não precisa instanciar um objeto para usar este método
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':  # criação da fase 1
                list_bg = []
                for i in range(7):  # para carregar as imagens
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))  # criação do jogador 1

            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))  # criação do jogador 2

            case 'Enemy1':
                return Enemy('Enemy1',
                             (WIN_WIDTH + 10, random.randint(0 + 40, WIN_HEIGHT - 40)))  # criação do inimigo 1
            case 'Enemy2':
                return Enemy('Enemy2',
                             (WIN_WIDTH + 10, random.randint(0 + 40, WIN_HEIGHT - 40)))  # criação do inimigo 2

# Arquivo para constantes
import pygame

# Dimensões da janela
WIN_WIDTH = 570
WIN_HEIGHT = 324

# Cores
COLOR_ORANGE = (255, 100, 10)
COLOR_RED = (255, 0, 10)
COLOR_WHITE = (230, 230, 230)
COLOR_YELLOW = (252, 250, 110)

# Texto do menu
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - CO-OP',
               'NEW GAME 2P - COMPETITION',
               'EXIT'
               )

# VELOCIDADE DAS IMAGENS
ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 1,
                'Level1Bg2': 2,
                'Level1Bg3': 3,
                'Level1Bg4': 4,
                'Level1Bg5': 5,
                'Level1Bg6': 6,
                'Player1': 5,
                'Player2': 5,
                'Enemy1': 5,
                'Enemy2': 4,
                }

# TECLAS DE MOVIMENTO
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w,
                 }

PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s,
                   }

PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d,
                    }

PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a,
                   }

# Geração de inimigos
EVENT_ENEMY = pygame.USEREVENT + 1
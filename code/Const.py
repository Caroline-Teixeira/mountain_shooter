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
                'Player1Shot': 3,
                'Player2': 5,
                'Player2Shot': 3,
                'Enemy1': 2,
                'Enemy1Shot': 5,
                'Enemy2': 2,
                'Enemy2Shot': 5,
                }

# PONTOS DE VIDA
ENTITY_HEALTH = {'Level1Bg0': 999,
                 'Level1Bg1': 999,
                 'Level1Bg2': 999,
                 'Level1Bg3': 999,
                 'Level1Bg4': 999,
                 'Level1Bg5': 999,
                 'Level1Bg6': 999,
                 'Player1Shot': 1,
                 'Player1': 300,
                 'Player2Shot': 1,
                 'Player2': 300,
                 'Enemy1': 200,
                 'Enemy1Shot': 1,
                 'Enemy2': 200,
                 'Enemy2Shot': 1,
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

# TECLAS DE TIRO
PLAYER_KEY_SHOOT = {'Player1': pygame.K_SPACE,
                    'Player2': pygame.K_LCTRL,
                    }

# TIROS - intervalo de criação de tiro dos jogadores quanto a tecla de tiro for pressionada
ENTITY_SHOT_DELAY = {'Player1': 10,
                     'Player2': 10,
                     'Enemy1': 70,
                     'Enemy2': 90,

                     }

# Geração de inimigos
EVENT_ENEMY = pygame.USEREVENT + 1

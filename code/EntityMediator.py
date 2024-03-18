from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class EntityMediator:  # Para mediar colisões
    @staticmethod
    def __verify_collision_window(ent: Entity):  # __método protegido
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:  # passou da tela
                # print(ent.name)
                ent.health = 0

        if isinstance(ent, PlayerShot):  # Tiros
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

        if isinstance(ent, EnemyShot):  # Tiros do inimigo
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:  # vida = 0, remove entidade
                entity_list.remove(ent)

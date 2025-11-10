import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT
from code.entity import Entity


class Player(Entity):
    def __init__(self, nome: str, position: tuple):
        super().__init__(nome, position)

    def update(self):
        pass

    def move(self, ):
        preesed_keys = pygame.key.get_pressed()
        if preesed_keys[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if preesed_keys[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if preesed_keys[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if preesed_keys[PLAYER_KEY_RIGHT[self.name]] and self.rect.right > 0:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass
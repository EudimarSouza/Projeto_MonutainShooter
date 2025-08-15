from CodeGame.Cost import ENTITY_SPEED
from CodeGame.Entity import Entity


class PlayerShoot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx += ENTITY_SPEED[self.name]

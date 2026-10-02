from shlex import split

import pygame, random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)
        child_one_vector = self.velocity.rotate(split_angle)
        child_two_vector = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child_one = Asteroid(self.position.x, self.position.y, new_radius)
        child_two = Asteroid(self.position.x, self.position.y, new_radius)
        child_one.velocity = child_one_vector * 1.2
        child_two.velocity = child_two_vector * 1.2

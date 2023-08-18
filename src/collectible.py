import pygame

class Collectible:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.collected = False

    def update(self, obstacle_speed):
        self.x -= obstacle_speed

    def collides_with(self, stick_figure):
        return (self.x < stick_figure.x + stick_figure.width and
                self.x + self.size > stick_figure.x and
                self.y + self.size > stick_figure.y and
                self.y < stick_figure.y + stick_figure.height)

    def render(self, screen):
        if not self.collected:
            color = (255, 255, 0)  # Yellow color for collectible items
            pygame.draw.circle(screen, color, (self.x + self.size // 2, self.y + self.size // 2), self.size // 2)

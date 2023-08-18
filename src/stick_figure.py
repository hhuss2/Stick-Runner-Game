import pygame

class StickFigure:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 60
        self.speed = 5
        self.is_jumping = False
        self.jump_count = 10

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_count = 10

    def update(self):
        if self.is_jumping:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (self.x + self.width // 2, self.y), 15)
        pygame.draw.line(screen, (0, 0, 255), (self.x + self.width // 2, self.y), (self.x + self.width // 2, self.y + self.height), 6)
        pygame.draw.line(screen, (0, 0, 255), (self.x + self.width // 2, self.y + self.height), (self.x, self.y + self.height + 30), 6)
        pygame.draw.line(screen, (0, 0, 255), (self.x + self.width // 2, self.y + self.height), (self.x + self.width, self.y + self.height + 30), 6)
        pygame.draw.line(screen, (0, 0, 255), (self.x + self.width // 2, self.y + self.height // 2), (self.x, self.y + self.height // 4), 6)
        pygame.draw.line(screen, (0, 0, 255), (self.x + self.width // 2, self.y + self.height // 2), (self.x + self.width, self.y + self.height // 4), 6)


import pygame
import random
from stick_figure import StickFigure
from collectible import Collectible

class Game:
    def __init__(self):
        pygame.init()

        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Stick Runner Game")

        self.clock = pygame.time.Clock()

        self.stick_figure = StickFigure(100, self.screen_height - 100)
        self.obstacles = []
        self.obstacle_size = 30
        self.obstacle_speed = 5
        self.obstacle_spawn_rate = 0.7

        self.score = 0
        self.high_score = self.load_high_score()
        self.font = pygame.font.Font(None, 36)
        self.game_over = False

        self.collectibles = []  # List to store collectibles
        self.collectible_spawn_rate = 2

    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except (IOError, ValueError):
            return 0

    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.stick_figure.jump()

    def spawn_collectible(self):
        new_collectible = Collectible(self.screen_width, random.randint(100, self.screen_height - 100))
        self.collectibles.append(new_collectible)

    def update(self):
        if not self.game_over:
            self.stick_figure.update()

            for obstacle in self.obstacles:
                obstacle["x"] -= self.obstacle_speed

                if obstacle["x"] + self.obstacle_size < 0:
                    self.obstacles.remove(obstacle)
                    self.score += 1
                    if self.score > self.high_score:
                        self.high_score = self.score
                        self.save_high_score()

                if obstacle["x"] < self.stick_figure.x + self.stick_figure.width and \
                   obstacle["x"] + self.obstacle_size > self.stick_figure.x and \
                   obstacle["y"] + self.obstacle_size > self.stick_figure.y and \
                   obstacle["y"] < self.stick_figure.y + self.stick_figure.height + 15:
                    self.game_over = True

            if random.randint(0, 100) < self.obstacle_spawn_rate:
                new_obstacle = {"x": self.screen_width, "y": self.screen_height - self.obstacle_size, "size": self.obstacle_size}
                self.obstacles.append(new_obstacle)

            if random.randint(0, 100) < self.collectible_spawn_rate:
                self.spawn_collectible()

            for collectible in self.collectibles:
                collectible.update(self.obstacle_speed)

                if collectible.collides_with(self.stick_figure):
                    self.collectibles.remove(collectible)
                    self.score += 10

    def render(self):
        self.screen.fill((0, 0, 0))

        if not self.game_over:
            self.stick_figure.draw(self.screen)

            for obstacle in self.obstacles:
                pygame.draw.rect(self.screen, (0, 255, 0), (obstacle["x"], obstacle["y"], obstacle["size"], obstacle["size"]))

            for collectible in self.collectibles:
                collectible.render(self.screen)

            score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))
        else:
            game_over_font = pygame.font.Font(None, 48)
            game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
            self.screen.blit(game_over_text, (self.screen_width // 2 - game_over_text.get_width() // 2, self.screen_height // 2 - 50))

            score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(score_text, (self.screen_width // 2 - score_text.get_width() // 2, self.screen_height // 2))

            high_score_text = self.font.render(f"High Score: {self.high_score}", True, (255, 255, 255))
            self.screen.blit(high_score_text, (self.screen_width // 2 - high_score_text.get_width() // 2, self.screen_height // 2 + 50))

        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            keys = pygame.key.get_pressed()
            if self.game_over and keys[pygame.K_r]:
                self.stick_figure = StickFigure(100, self.screen_height - 100)
                self.obstacles = []
                self.score = 0
                self.game_over = False

            if not self.game_over:
                self.handle_input()
                self.update()
                self.render()

            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()

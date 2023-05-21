import pygame

pygame.init()

ROCKET_IMG = 'rocket.png'
BALL_IMG = 'ball.png'
BG_COLOR = (64, 64, 64)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0, width=0, height=0):
        image = pygame.image.load(image)
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, image, x, y, width, height, speed, k_up=pygame.K_UP, k_down=pygame.K_DOWN,):

        super().__init__(image, x, y, width, height)
        self.speed = speed
        self.k_up = k_up
        self.k_down = k_down

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.k_up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[self.k_down] and self.rect.y < (
            600 - self.rect.height
        ):
            self.rect.y += self.speed

class Ball(GameSprite):
    dx = 5
    dy = 5

    def update(self, player_1, player_2):
        if self.rect.y <= 0:
            dy *= -1
        if self.rect.y >= (600 - self.rect.height):
            dy *= -1
        if self.rect.colliderect(player_1.rect):
            dx *= -1
        if self.rect.colliderect(player_2.rect):
            dx *= -1
        self.rect.x += dx
        self.rect.y += dy

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")
window.fill(BG_COLOR)
clock = pygame.time.Clock()

player_left = Player(
    ROCKET_IMG, 5, 5, 30, 100, 5, pygame.K_w, pygame.K_s
)
player_right = Player(
    ROCKET_IMG, 800 - 35, 600 - 105,
    30, 100, 5, pygame.K_UP, pygame.K_DOWN
)

ball = Ball(BALL_IMG, 40, 40, )

game_status = 'game'
while game_status != 'off':
    window.fill(BG_COLOR)
    player_left.update()
    player_right.update()
    player_left.draw()
    player_right.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status = 'off'

    clock.tick(60)
    pygame.display.update()

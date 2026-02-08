import pygame
pygame.init()
window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Пинг - понг')

light_blue = (66, 215, 245)
window.fill(light_blue)

racket_size = (70, 200)
ball_size = (65, 65)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, speed, x, y, size):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), size)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_DOWN]:
            self.rect.y += self.speed

        if keys_pressed[pygame.K_UP]:
            self.rect.y -= self.speed

    def update_2(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_s]:
            self.rect.y += self.speed

        if keys_pressed[pygame.K_w]:
            self.rect.y -= self.speed

dir_x = -3
dir_y = 3

class Ball(GameSprite):
    def move(self):
        self.rect.x += dir_x
        self.rect.y += dir_y


white = (255,255,255)

font = pygame.font.Font(None, 60)

racket1 = Player('racket.png', 5, 10, 10, racket_size)
racket2 = Player('racket.png', 5, 620, 10, racket_size)

ball = Ball('ball.png', 7, 350, 250, ball_size)
FPS = 60
game = True
game_over = False
clock = pygame.time.Clock()
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    if not game_over:
        if ball.rect.y > 500 - ball_size[1]:
            dir_y *= -1

        if ball.rect.y < 0:
            dir_y *= -1

        if pygame.sprite.collide_rect(ball, racket2):
            dir_x *= -1

        if pygame.sprite.collide_rect(ball, racket1):
            dir_x *= -1

        window.fill(light_blue)
        racket1.reset(window)
        racket1.update()
        racket2.reset(window)
        racket2.update_2()
        ball.reset(window)
        ball.move()

        if ball.rect.x > 700:
            text_win = font.render('player left win', True, white)
            window.blit(text_win, (300, 250))
            game_over = True

        if ball.rect.x < -65:
            text_win = font.render('player right win', True, white)
            window.blit(text_win, (300, 250))
            game_over = True

    pygame.display.update()
    clock.tick(FPS)


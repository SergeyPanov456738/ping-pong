import pygame

window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Пинг - понг')
#pygame.display.set_icon()

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

        if keys_pressed[pygame.K_DOWN] and self.rect.y <500 - 210:
            self.rect.y += self.speed

        if keys_pressed[pygame.K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed

    def update_2(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_s] and self.rect.y <500 - 110:
            self.rect.y += self.speed

        if keys_pressed[pygame.K_w] and self.rect.y > 10:
            self.rect.y -= self.speed

racket1 = Player('racket.png', 5, 10, 10, racket_size)
racket2 = Player('racket.png', 5, 620, 10, racket_size)

ball = GameSprite('ball.png', 7, 350, 250, ball_size)
FPS = 60
game = True
clock = pygame.time.Clock()
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
 
        window.fill(light_blue)
        racket1.reset(window)
        racket1.update()
        racket2.reset(window)
        racket2.update_2()
        ball.reset(window)

    pygame.display.update()
    clock.tick(FPS)


import pygame

window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Пинг - понг')
#pygame.display.set_icon()

light_blue = (66, 215, 245)
window.fill(light_blue)

FPS = 60
game = True
clock = pygame.time.Clock()
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False



    clock.tick(FPS)
    pygame.display.update()
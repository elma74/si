import pygame

pygame.init()

FPS = 60
clock = pygame.time.Clock()


# set game window width and height
screen_width = 600
screen_height = 800

# show the window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders'")

bg = pygame.image.load("img/bg.png")

# set up player
player = pygame.image.load("img/spaceship.png")
sprite = pygame.sprite.Sprite()
sprite.image = player
sprite.rect = sprite.image.get_rect()
sprite.rect.center = [300, 730]

player_group = pygame.sprite.Group(sprite)

# set up enemy
enemy_texture = pygame.image.load("img/alien1.png")
enemy_sprite = pygame.sprite.Sprite()
enemy_sprite.image = enemy_texture
enemy_sprite.rect = enemy_sprite.image.get_rect()
enemy_sprite.rect.center = [300, 200]

enemy_group = pygame.sprite.Group(enemy_sprite)

# main game loop
while True:

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and sprite.rect.left > 0:
        sprite.rect.x -= 8

    if keys[pygame.K_RIGHT] and sprite.rect.right < 600 :
        sprite.rect.x += 8


    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


    screen.blit(bg, (0, 0))
    enemy_group.draw(screen)
    player_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)

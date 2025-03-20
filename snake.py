import pygame
import random
from sys import exit

pygame.init()

screen_height = 600
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))

player = pygame.image.load("for-lovely-souhrada/gg/766161.png").convert_alpha()
playerX = 200
playerY = 200
playerZone = player.get_rect(center = (playerX, playerY)) #?
speed = 10



player = pygame.image.load("for-lovely-souhrada/gg/766161.png").convert_alpha()
player = pygame.transform.scale(player, (50, 50))
player_rect = player.get_rect(center=(200, 200))
rychlost = 5
coin = pygame.Rect(random.randint(50, 750), random.randint(50, 550), 30, 30)
skore = 0

clock = pygame.time.Clock()
pygame.time.get_ticks()
font = pygame.font.Font(None, 25)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    screen.fill("white")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.y -= rychlost
    if keys[pygame.K_s]:
        player_rect.y += rychlost
    if keys[pygame.K_a]:
        player_rect.x -= rychlost
    if keys[pygame.K_d]:
        player_rect.x += rychlost
    if keys[pygame.K_p]:
        exit()


    if player_rect.colliderect(coin):
        skore += 1
        coin.x = random.randint(50, 750)
        coin.y = random.randint(50, 550)

    screen.blit(player, player_rect)  
    pygame.draw.rect(screen, "red", coin)

    text = font.render(f"Score: {skore}", True, "black")
    screen.blit(text, (screen_width - 120, 10))

    pygame.display.update()
    clock.tick(60)
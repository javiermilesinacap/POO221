import pygame
import random
class Player:
    def __init__(self, x, y, radius, color, score=0, vel=5):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 5
        self.score = score
        self.vel = vel
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        mouse = pygame.mouse.get_pos()
        if mouse[0] < self.x:
            self.x -= self.vel
        if mouse[0] > self.x:
            self.x += self.vel
        if mouse[1] < self.y:
            self.y -= self.vel
        if mouse[1] > self.y:
            self.y += self.vel
class Enemy: 
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 3
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
    def move(self):
        self.x += self.vel
        self.y += self.vel
        if self.y > 500 - self.radius or self.y < self.radius:
            self.vel *= -1
        if self.x > 500 - self.radius or self.x < self.radius:
            self.vel *= -1

def redrawGameWindow():
    win.fill((255,255,255))
    player.draw(win)
    enemy.draw(win)
    win.blit(text, (10, 10))
    pygame.display.update()
pygame.init()
info = pygame.display.Info()
SIZE = WIDTH, HEIGHT = info.current_w, info.current_h
win = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Agario")
player = Player(250, 250, 50, (255, 0, 0))
enemy = Enemy(100, 100, 50, (0, 255, 0))
run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.vel += 1
            if event.button == 3:
                player.vel -= 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            run = False
    player.move()
    enemy.move()
    if(player.x + player.radius > enemy.x - enemy.radius and player.x - player.radius < enemy.x + enemy.radius and player.y + player.radius > enemy.y - enemy.radius and player.y - player.radius < enemy.y + enemy.radius):
        print("Collision")
        player.radius += (enemy.radius/6)
        enemy.radius = -1
        if enemy.radius < 0:
            enemy.radius = 50
            enemy.x = random.randint(0, 500)
            enemy.y = random.randint(0, 500)
            player.score += 1
            print("Score: ", player.score)
    text = pygame.font.SysFont('comicsans', 30, True, True)
    text = text.render("q= exit - Score: " + str(player.score), 1, (0, 0, 0))
    
    redrawGameWindow()


pygame.quit()
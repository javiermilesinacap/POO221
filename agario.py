import pygame
class Player:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 5
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
    pygame.display.update()
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Agario")
player = Player(250, 250, 50, (255, 0, 0))
enemy = Enemy(100, 100, 50, (0, 255, 0))
run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    player.move()
    enemy.move()
    redrawGameWindow()
pygame.quit()
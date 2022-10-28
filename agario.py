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
def redrawGameWindow():
    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Agario")
player = Player(250, 250, 50, (255, 0, 0))
run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    player.move()
    redrawGameWindow()
pygame.quit()
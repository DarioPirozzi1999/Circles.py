import pygame
pygame.init()
screen = pygame.display.set_mode([500,500])

class Circle():
    def __init__(self,color, pos, radius, width):
        self.color = color
        self.pos = pos
        self.radius= radius
        self.scrn= screen
        self.width = width
    def draw(self):
        pygame.draw.circle(self.scrn, self.color, self.pos, self.radius, self.width)
    def grow(self, x):
        self.radius += x
        pygame.draw.circle(self.scrn, self.color, self.pos, self.radius + x, self.width)

redCircle= Circle("red", (250,250), 50, 0)

while True:
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            redCircle.draw()
        elif event.type == pygame.MOUSEBUTTONUP:
            redCircle.grow(10)
        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            greenCircle = Circle("green", pos, 10, 0)
            greenCircle.draw()

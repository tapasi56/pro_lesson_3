import pygame
pygame.init()
screen = pygame.display.set_mode((600, 800))
screen.fill((255,255,255))
blue = (0,0,250)
green = (0,250,0)

class Circle():
    def __init__(self,color,pos,radius,width):
        self.circle_color = color
        self.circle_pos = pos
        self.circle_radius = radius
        self.circle_width = width
        self.circle_screen = screen
    
    def draw(self):
        self.draw_circle = pygame.draw.circle()
pygame.init()
screen = pygame.display.set_mode((600, 800))
blue = (0,0,250)
green = (0,250,0)

class Circle():
    def __init__(self,color,pos,radius,width):
        self.circle_color = color
        self.circle_pos = pos
        self.circle_radius = radius
        self.circle_width = width
        self.circle_screen = screen
    
    def draw(self):
        self.draw_circle = pygame.draw.circle(self.circle_screen, self.circle_color ,self.circle_pos ,self.circle_radius ,self.circle_width )


bcircle = Circle(blue, (300,300), 25, 0)
gcircle = Circle(green, (100,100), 25, 2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            bcircle.draw()
            gcircle.draw()
            pygame.display.update()
        



    






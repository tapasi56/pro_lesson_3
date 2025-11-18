import pygame
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
        self.draw_circle = pygame.draw.circle(self.circle_color ,self.circle_pos ,self.circle_radius ,self.circle_width ,self.circle_screen )


bcircle = Circle(blue, (300,300), 25, 0)



    






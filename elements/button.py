import pygame
from elements.text import Text

class Button():

    def createButton(self, color, selectedColor, position, name, radius = -1 ,width = 250, height = 50,  offset = (0,0)):
        self.name = name
        self.width = width
        self.height = height
        self.color = color
        self.selectedColor = selectedColor
        self.position = position
        self.radius = radius
        self.offset = offset
        self.button = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        self.button.center = (position[0] - offset[0], position[1] - offset[1])
        self.selected = False

        self.text = Text()


        pass

    def Render(self, screen, textcolor= (255,255,255), stextcolor = (0,0,255)):
        self.screen = screen
        if self.selected:
            pygame.draw.rect(screen, self.selectedColor, self.button, border_radius = self.radius)
            self.text.createText(self.name, self.position, 1, color=stextcolor)
            self.text.render(screen)
        else:
            pygame.draw.rect(screen, self.color, self.button, border_radius = self.radius)
            self.text.createText(self.name, self.position, 1, color=textcolor)
            self.text.render(screen)


    def Selected(self, mousePosition):
        if self.button.collidepoint((mousePosition[0], mousePosition[1])):
            self.selected= True
            return True
        else:
            self.selected = False
            return False

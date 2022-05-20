import pygame.freetype

pygame.init()

title_font = pygame.freetype.Font("./fonts/Glitch inside.otf", 42)
text_font = pygame.freetype.Font("./fonts/PIXEARG_.ttf", 22)

class Text:
    def __init__(self):
        pass

    def createText(self, text, position, font , offset=(0,0) ,color=(255, 255, 255),):
        self.text = text
        self.color = color
        self.position = position
        self.offset = offset
        if font == 1:
            self.text1, self.rect = text_font.render(text, color)
        else:
            self.text1, self.rect = title_font.render(text, color)

        self.rect.center = (position[0] - offset[0], position[1] - offset[1])

    def render(self, screen):

        screen.blit(self.text1, self.rect)

import pygame

from elements.button import Button
from scenes.BaseScene import SceneBase

w, h = 0, 0
button1 = Button()
button2 = Button()
button3 = Button()
button4  = Button()
vh, vw = 0,0



class SettingsScene(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)


        w, h = pygame.display.get_surface().get_size()
        vw, vh = w/100, h/100

        button1.createButton((255, 0, 0), (0, 255, 0), (50*vw, 30*vh), "teste")
        button2.createButton((255, 0, 0), (0, 255, 0), (50 * vw, 50 * vh), "teste")
        button3.createButton((255, 0, 0), (0, 255, 0), (50 * vw, 70 * vh), "teste")
        button4.createButton((255, 0, 0), (0, 255, 0), (50 * vw, 90 * vh), "teste")




    def ProcessInput(self, events, pressed_keys):
        mx, my = pygame.mouse.get_pos()
        try:
            if button1.Selected((mx,my)):
                pass

            if button2.Selected((mx, my)):
                pass

            if button3.Selected((mx, my)):
                pass

            if button4.Selected((mx, my)):
                pass

            pass
        except:
            print("erro")

    def Update(self):

        pass

    def Render(self, screen):
        screen.fill((0,0,100))
        button1.Render(screen)
        button2.Render(screen)
        button3.Render(screen)
        button4.Render(screen)

        pass
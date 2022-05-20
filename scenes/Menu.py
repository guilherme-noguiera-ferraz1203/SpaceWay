from scenes.BaseScene import SceneBase
from scenes.config import SettingsScene
from elements.button import Button
from elements.text import Text
import pygame
import sys



w,h = 0,0
click, kclick = False, False
selected = 0
vh, vw = 0, 0

Ttitle = Text()
Bjogar = Button()
Bsettings = Button()
Bquit = Button()

class MenuScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

        global title_font, text_font, w, h, button1, button2, button3,  vh, vw

        w, h = pygame.display.get_surface().get_size()
        vw, vh = w / 100, h / 100


        pygame.mouse.set_visible(True)


        Ttitle.createText("Retorno A DLL",(50*vw, 15*vh), 2)
        Bjogar.createButton((255,0,0), (0,255,0), (50*vw,35*vh),"Jogar")
        Bsettings.createButton((255, 0, 0), (0, 255, 0), (50 * vw, 50 * vh), "Settings")
        Bquit.createButton((255, 0, 0), (0, 255, 0), (50 * vw, 65 * vh), "Quit")


    def ProcessInput(self, events, pressed_keys):
        global click, kclick, cbutton1, cbutton2, cbutton3, selected
        mx, my = pygame.mouse.get_pos()

        if Bjogar.Selected((mx, my)):
            if click:
                print("Jogar")


        elif Bsettings.Selected((mx, my)):
            if click:
                self.SwitchToScene(SettingsScene())


        elif Bquit.Selected((mx, my)):
            if click:
                pygame.quit()
                sys.exit()


        click = False
        if events != []:
            if events[0].type == pygame.MOUSEBUTTONDOWN:
                if events[0].button == 1:
                    click = True


    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((0, 0, 100))
        Ttitle.render(screen)
        Bjogar.Render(screen)
        Bquit.Render(screen)
        Bsettings.Render(screen)




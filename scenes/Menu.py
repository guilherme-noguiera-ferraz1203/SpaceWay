from scenes.BaseScene import SceneBase
from scenes.config import SettingsScene
from elements.button import Button
from elements.text import Text
import pygame
import sys



w,h = 0,0
click= False
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


        Ttitle.createText("SpaceWay",(50*vw, 15*vh), 2)
        Bjogar.createButton((255,0,0), (0,255,0), (50*vw,35*vh),"Jogar", radius=50)
        Bsettings.createButton((255, 0, 0), (0, 255, 0), (50 * vw, 50 * vh), "Settings",radius=50)
        Bquit.createButton((255, 0, 0), (0, 255, 0), (50 * vw, 65 * vh), "Quit",radius=50)


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
        
        bkg= pygame.image.load('./images/background/bkg03.png')
        bkg = pygame.transform.scale(bkg, (w, h))
        bkgrect = bkg.get_rect()
        bkgrect.center = ((w / 2), (h / 2))
        screen.blit(bkg, bkgrect)


        Ttitle.render(screen)
        Bjogar.Render(screen)
        Bquit.Render(screen)
        Bsettings.Render(screen)




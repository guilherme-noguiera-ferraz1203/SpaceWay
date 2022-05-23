import pygame
from scenes.BaseScene import *
from scenes.Menu import *
from elements.text import * 

now = 0
swidth, sheight = 0,0
vw, vh = 0,0

Ttitle = Text()

def run_game(width, height, fps, starting_scene):
    global sheight, swidth, vw, vh
    swidth = width
    sheight = height
    vw, vh = swidth / 100, sheight / 100
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('SpaceWay')
    logo = pygame.image.load('./images/naves/nave01.png')
    pygame.display.set_icon(logo)
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()

        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)

        now = pygame.time.get_ticks()
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)
        active_scene = active_scene.next


        pygame.display.flip()
        clock.tick(fps)


# The rest is code where you implement your game using the Scenes model

class Splash(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)          
        

    def ProcessInput(self, events, pressed_keys):
        pygame.mouse.set_visible(False)

    def Update(self):
        pass

    def Render(self, screen):
        Ttitle.createText("SpaceWay",(50*vw, 50*vh), 2)
        splash = pygame.image.load('./images/background/bkg03.png')
        splash = pygame.transform.scale(splash, (swidth, sheight))
        logorect = splash.get_rect()
        logorect.center = ((swidth / 2), (sheight / 2))
        screen.blit(splash, logorect)
        Ttitle.render(screen)

        if pygame.time.get_ticks() > now + 2500:
            self.SwitchToScene(MenuScene())

import pygame
from scenes.BaseScene import SceneBase
from scenes.Menu import MenuScene
now = 0
swidth, sheight = 0,0


def run_game(width, height, fps, starting_scene):
    global sheight, swidth
    swidth = width
    sheight = height
    pygame.init()
    screen = pygame.display.set_mode((width, height))
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
        logo = pygame.image.load('./images/logo.bmp')
        logo = pygame.transform.scale(logo, (swidth/3.5, sheight/3.5))
        logorect = logo.get_rect()
        logorect.center = ((swidth / 2), (sheight / 2))
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((0, 0, 0))
        screen.blit(logo, logorect)
        if pygame.time.get_ticks() > now + 2500:
            self.SwitchToScene(MenuScene())





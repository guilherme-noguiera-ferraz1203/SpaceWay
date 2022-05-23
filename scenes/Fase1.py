from scenes.BaseScene import *


class Fase1(SceneBase):
    def __init__(self):
        self.next = self

    def ProcessInput(self, events, pressed_keys):
        if events[0].type == pygame.KEYDOWN:
            if events[0].key  == pygame.K_w:
                
            pass
        elif events[0].type == pygame.KEYUP:
            
    def Update(self):
        pass

    def Render(self, screen):
        pass



from scenes.splash import *

from screeninfo import get_monitors

for m in get_monitors():
    pass

run_game(m.width/2, m.height/2, 60, Splash())
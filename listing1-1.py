# Spacewalk
# by Sean Mcmanus
# www.sean.co.uk /www.nostarch.com

x = 0
y = 0
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
import pgzrun

WIDTH = 800
HEIGHT = 600
player_x = 600
player_y = 350

def draw():
    screen.blit(images.backdrop, (0, 0))

pgzrun.go()

from pygame import *

display.set_caption("PingPong")
window = display.set_mode((1000, 600))
background = transform.scale(image.load("Background.png"), (1000, 600))

class GameSprite(sprite.Sprite):
    def __init__(self, plr_image, x, y, size_x, size_y, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(plr_image), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

Game = True
clock = time.Clock()
while Game:
    for e in event.get():
        if e.type == QUIT:
            Game = False
    window.blit(background,(0,0))
    display.update()
    clock.tick(60)

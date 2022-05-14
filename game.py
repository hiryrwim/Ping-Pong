from pygame import *


class GamePlayer(sprite.Sprite):
    def __init__(self, img, width, x, y, step):
        super().__init__()
        self.image = transform.scale(
            image.load(img,
            (width, height)
            )
        )
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.step = step

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class LeftPlayer(GamePlayer):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.step
        elif keys[k_s] and self.rect.y < 500 - self.height:
            self.rect.y += self.step
            
class RightPlayer(GamePlayer):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.step
        elif keys[k_DOWN] and self.rect.y < 500 - self.height:
            self.rect.y += self.step

window = display.set_mode((700, 500))
background = transform.scale(
    image.load('ping pong.jpg'),
    (500, 500)
)
fps = 60
player_1 = LeftPlayer('bobr.jpg', 40, 50, 50)
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        window.blit(background, (0, 0))
        display.update()
        clock.tick(fps)
        player_1.update()
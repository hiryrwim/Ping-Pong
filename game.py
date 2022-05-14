from pygame import *

window = display.set_mode((500, 500))
background = transform.scale(
    image.load('ping pong.jpg'),
    (500, 500)
)
fps = 60
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        window.blit(background, (0, 0))
        display.update()
        clock.tick(fps)
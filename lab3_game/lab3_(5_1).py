import pygame as pg

pg.init()

FPS = 30
screen = pg.display.set_mode((820, 550))

sky = (254, 213, 162)
sun = (252, 238, 33)
cloud = (254, 213, 196)
back = (252, 152, 49)
front = (172, 67, 52)
sand = (179, 134, 148)



screen.fill(sky)

back_x=[(0, 280), (10, 240), (180, 130), (210, 140), (220, 150), (320, 235), (360, 230), (400, 240),(440, 200), (480, 220), (510, 210), (600, 130), (630, 160), (660, 170), (710, 180), (750,140), (820, 200)]

pg.draw.rect(screen, cloud, (0, 150, 820, 130)) #облака
pg.draw.circle(screen, sun, (400, 150), 50) #солнце
pg.draw.rect(screen, sand, (0, 350 , 820, 200)) #песок
pg.draw.polygon(screen, back, back_x)
pg.draw.ellipse(screen, back, [(660, 170), ()] )



pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()
pg.quit()

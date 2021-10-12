import pygame

pygame.init()

# создаем экран для рисунка
FPS = 30
(length, height) = (1250, 834)
screen = pygame.display.set_mode((length, height))

# задаём цвета, которые используются в изображении
front_color = (180, 135, 149)
back_color = (254, 214, 149)
sky_color = (254, 214, 163)
hight_color = (254, 214, 197)
back_mountains_color = (252, 153, 45)
front_mountains_color = (173, 65, 49)
sun_color = (252, 239, 27)
bird_color = (64, 27, 3)
mountain_color = (44, 7, 33)
width = 10

# рисуем небо верхнюю и нижнюю часть. rect - задаёт прямоугольники
pygame.draw.rect(screen, sky_color, (0, 0 * height,
                 length, 0.25 * height))
pygame.draw.rect(screen, hight_color, (0, 0.25 * height,
                 length, 0.26 * height))

# горы(верхние). polygon - создает ломанную, которая задает силуэт гор. (координаты нахождения каждой точки ломанной)
pygame.draw.polygon(screen, back_mountains_color, [(0, 0.5 * height),
    (0, 0.4 * height),
    (0.06 * length, 0.38 * height),
    (0.18 * length, 0.2 * height),
    (0.24 * length, 0.24 * height),
    (0.27 * length, 0.3 * height),
    (0.44 * length, 0.45 * height),
    (0.5 * length, 0.4 * height),
    (0.55 * length, 0.39 * height),
    (0.6 * length, 0.42 * height),
    (0.64 * length, 0.4 * height),
    (0.7 * length, 0.35 * height),
    (0.8 * length, 0.24 * height),
    (0.82 * length, 0.2 * height),
    (0.85 * length, 0.21 * height),
    (0.9 * length, 0.34 * height),
    (0.96 * length, 0.3 * height),
    (length, 0.2 * height),
    (length, 0.4 * height)])

# рисуем солнце с помощью опеора circle (задаем центр окружности и радиус)
pygame.draw.circle(screen, sun_color, (int(0.5 * length),
                   int(0.25 * height)), 80)

# rect создает землю (задаются координаты верхней левой точки, длина, ширина)
pygame.draw.rect(screen, back_color, (0, 0.5 *
                 height, length, 0.25 * height)) # земля

# создаем горы (нижние). они задаются двумя эллипсами ellipse (задаются параметры прямоугольника в который вписан эллипс, аналогично параметрам предыдущих прямоугольников). так же используем ломанную, при помощи polygon
pygame.draw.ellipse(screen, front_mountains_color,
                    (0.04 * length, 0.45 * height, 200, 400))
pygame.draw.ellipse(screen, front_mountains_color,
                    (0.62 * length, 0.55 * height, 140, 380))
pygame.draw.polygon(screen, front_mountains_color, [(0, 0.75 * height),
    (0, 0.55 * height),
    (0.2 * length, 0.75 * height),
    (0.27 * length, 0.6 * height),
    (0.35 * length, 0.7 * height),
    (0.38 * length, 0.55 * height),
    (0.48 * length, 0.6 * height),
    (0.54 * length, 0.7 * height),
    (0.62 * length, 0.68 * height),
    (0.68 * length, 0.55 * height),
    (0.8 * length, 0.65 * height),
    (0.88 * length, 0.55 * height),
    (0.93 * length, 0.6 * height),
    (length, 0.45 * height),
    (length, 0.75 * height)])
# создаем прямоугольник, задающий низ земли.
pygame.draw.rect(screen, front_color,
                 (0, 0.75 * height, length, 0.25 * height))

# задаем самые нижние горы, при помощи polygon.
pygame.draw.polygon(screen, mountain_color, [(0, height),
    (0, 0.55 * height),
    (0.12 * length, 0.65 * height),
    (0.3 * length, 0.94 * height),
    (0.4 * length, 0.98 * height),
    (0.5 * length, 0.92 * height),
    (0.65 * length, 0.85 * height),
    (0.7 * length, 0.9 * height),
    (0.86 * length, 0.86 * height),
    (0.94 * length, 0.66 * height),
    (length, 0.60 * height),
    (length, height)])

# создаем объект типа surface, на котором рисуем птичек. птички рисуем при помощи дуги arc. задается координаты левой верхней вершины, длину, ширину эллипса, а также уголы, которыми мы задаем длину дуги.
sre=pygame.Surface((100, 60))
sre.fill((0, 0, 0))
sre.set_colorkey((0, 0, 0))
pygame.draw.arc(sre, bird_color, (1.5, 11,
                    50, 30), 0, 3, width)
pygame.draw.arc(sre, bird_color, (42, 8, 40, 50), 1, 3, width)

# создаем еще один объект типа surface, он создает такую же птичку, размеры и угол наклона которой можно менять при помощь rotozoom. rotozoom(объект, угол поворота, размер). с помощью flip можем отражать птичку по вертикали и по горизонтали. flip(объект, по ветрикали, по горизонтали)
sre1=pygame.transform.rotozoom(sre, 0, 1)
sre1=pygame.transform.flip(sre1, 0, 0)
sre1.set_colorkey((0, 0, 0))

# вставляем семь птичек с помощью blit. blit(объект, координата по горизонтали, координата по вертикали)
screen.blit(sre1, (0.7 * length, 0.65 * height))
screen.blit(sre1, (0.76 * length, 0.62 * height))
screen.blit(sre1, (0.58 * length, 0.7 * height))
screen.blit(sre1, (0.5 * length, 0.4 * height))
screen.blit(sre1, (0.56 * length, 0.3 * height))
screen.blit(sre1, (0.66 * length, 0.35 * height))
screen.blit(sre1, (0.6 * length, 0.6 * height))




pygame.display.update()
clock=pygame.time.Clock()
finished=False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

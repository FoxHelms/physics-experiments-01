import pygame, sys, pymunk, time, math, random

def get_gravity(gravMag):


    rn = int(time.time())

    rn1 = rn % 1000

    per = rn1 / 1000

    dg = per

    not_unit_x = math.acos(dg)
    not_unit_y = math.asin(dg)

    unit_x = not_unit_x / math.sqrt(not_unit_x ** 2 + not_unit_y ** 2)
    unit_y = not_unit_y / math.sqrt(not_unit_x ** 2 + not_unit_y ** 2)

    gravity = (round(gravMag * unit_x), round(gravMag * unit_y))

    return gravity
    

def create_apples(space, pos):
    body = pymunk.Body(1,100,body_type=pymunk.Body.DYNAMIC)
    #body.position = (400,0)
    body.position = pos
    shape = pymunk.Circle(body, 50)
    space.add(body,shape)
    return shape

def draw_apples(apples,colors):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        apple_color = random.choice(colors)
        apples_colors.append(apple_color)
        apple_index = apples.index(apple)
        pygame.draw.circle(screen,apples_colors[apple_index],(pos_x,pos_y),50)

def draw_balls(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(pos_x,pos_y),50)

def static_balls(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (450,450)
    #body.position = get_gravity(500)
    shape = pymunk.Circle(body,50)
    space.add(body,shape)
    return shape

pygame.init()

gravMag = 10
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
space = pymunk.Space()
#space.gravity = (0,100)
space.gravity = get_gravity(gravMag)
apples = []
apples_colors = []
balls = []
colors = [(220,20,60),(255,127,80),(233,150,122),(255,215,0),(128,128,0),(173,255,47),(102,205,170),(224,255,255),(100,149,237)]


#apples.append(create_apples(space))

balls.append(static_balls(space))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            apples.append(create_apples(space, pos))

    screen.fill((217,217,217))
    draw_apples(apples,colors)
    draw_balls(balls)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)


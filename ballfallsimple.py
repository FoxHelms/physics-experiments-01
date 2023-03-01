import pygame, sys, pymunk

def create_apples(space):
    body = pymunk.Body(1,100,body_type=pymunk.Body.DYNAMIC)
    body.position = (400,0)
    shape = pymunk.Circle(body, 50)
    space.add(body,shape)
    return shape

def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(pos_x,pos_y),50)

def draw_balls(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(pos_x,pos_y),50)

def static_balls(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (450,450)
    shape = pymunk.Circle(body,50)
    space.add(body,shape)
    return shape

pygame.init()

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,100)
apples = []
balls = []
apples.append(create_apples(space))
balls.append(static_balls(space))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((217,217,217))
    draw_apples(apples)
    draw_balls(balls)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)


import pygame

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 680))
background = pygame.image.load("tarmac.jpg")

pygame.display.set_caption("Motii")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

image = pygame.image.load("user.png")
user_img = pygame.transform.rotate(image, 180)
user_x = 465
user_y = 545
user_x_change = 0

image1 = pygame.image.load("car1.png")
car1_img = pygame.transform.rotate(image1, 180)
car1_x = 0
car1_y = 0
car1_y_change = 0.1

car2_img = pygame.image.load("car2.png")
car2_x = 310
car2_y = 50
car2_y_change = 0.2


def user(x, y):
    screen.blit(user_img, (x, y))


def car1(x, y):
    screen.blit(car1_img, (x, y))


def car2(x, y):
    screen.blit(car2_img, (x, y))


running = True
while running:
    screen.fill((255, 255, 255))
    # screen.blit(background, (0, 0))
    pygame.draw.line(screen, (0, 0, 0), (300, 0), (300, 680), width=5)
    pygame.draw.line(screen, (0, 0, 0), (150, 0), (150, 680), width=2)
    pygame.draw.line(screen, (0, 0, 0), (450, 0), (450, 680), width=2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                user_x_change = -0.3
                user_img = pygame.transform.rotate(user_img, 20)
            if event.key == pygame.K_RIGHT:
                user_x_change = 0.3
                user_img = pygame.transform.rotate(user_img, -20)
            if event.key == pygame.K_UP:
                car1_y_change = 0.5
                car2_y_change = 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                user_x_change = 0
                user_img = pygame.transform.rotate(image, 180)
            if event.key == pygame.K_UP:
                car1_y_change = 0.1
                car2_y_change = 0.3

    if user_x > 465:
        user_x = 465
    elif user_x < 0:
        user_x = 0

    if car1_y >= 680:
        car1_y = 0

    car1_y += car1_y_change
    car2_y += car2_y_change

    user_x += user_x_change
    user(user_x, user_y)
    car1(car1_x, car1_y)
    car2(car2_x, car2_y)

    pygame.display.update()

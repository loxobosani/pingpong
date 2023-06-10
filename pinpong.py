from pygame import *

window = display.set_mode((600, 600))
back = (145, 235, 42)
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > -50:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 520:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > -50:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 520:
            self.rect.y += self.speed

clock = time.Clock()

game = True 
finish = False

speed_x = 3
speed_y = 3



rocket1 = Player('grib.png', 20, 250, 5, 100, 200)
rocket2 = Player('grib.png', 400, 250, 5, 100, 200)
ball = Player('biden.png', 250, 250, 5, 50, 50)
font.init()
font = font.Font(None, 50)

lose1 = font.render('1 Игрок проиграл!', True, (150, 0, 0))
lose2 = font.render('2 Игрок проиграл!', True, (150, 0, 0))

while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        rocket1.reset()
        rocket2.reset()
        rocket1.update_l()
        rocket2.update_r()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y


    display.update()                                               
    clock.tick(60)
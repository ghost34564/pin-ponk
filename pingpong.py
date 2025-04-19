from pygame import *
from random import randint


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < win_widh - 80:
            self.rect.x += self.speed
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x < win_widh - 80:
            self.rect.x += self.speed

back = (200, 255, 255)
win_widh = 600
win_height = 500
window = display.set_mode((win_widh, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket_1 = Player('.png', 30, 200, 4, 50, 150)
racket_2 = Player('.png', 520, 200, 4, 50, 150)

ball = GameSprite('.png', 200, 200, 4, 50, 50)
font = font.Font(None, 35)
lose1 = font.render('PLAYER_1 lose!', True, (180, 0, 0))
lose2 = font.render('PLAYER_2 lose!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket_1.update_l()
        racket_2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.colide_rect(racket_1, ball) or sprite.collide_rect(racket_2, ball):
            speed_x *= -1
            speed_y *= 1
        
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True
        
        if ball.rect.x > win_widh:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        racket_1.reset()
        racket_2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
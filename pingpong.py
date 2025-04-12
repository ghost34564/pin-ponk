from pygame import *
from random import randint



win_heit = 500
win_wert = 700

font.init()
font1 = font.Font(None, 80)
font2 = font.SysFont('Arial', 36)
win = font1.render('you win!!!', True, (255, 255, 255))
lose = font1.render('you lose!', True, (100, 200, 250))

back = 'ping.png'
ball = 'ball.png'
rock = 'rock.png'
color = 255, 250, 200

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
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_wert - 80:
            self.rect.x += self.speed
    

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        

window = display.set_mode((win_wert, win_heit))
display.set_caption('ping_pong')
window.fill(color)


Rock = Player(rock, 5, win_heit - 100, 80, 100, 10)

finish = False
run = True

rel_time = False
num_fire = 0


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    display.update()
    time.delay(50)



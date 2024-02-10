from pygame import *
from time import sleep
from random import *

font.init()
back = (200,255,255)
win_height = 500
win_width = 1000
window = display.set_mode((win_width, win_height))
window.fill(back)
clock = time.Clock()
score1 = 0
score2 = 0
clock = time.Clock()
FPS = 60
game = True
finish = False
mixer.init()
mixer.music.load("win.mp3")
mixer.music.load("Duck.mp3")

class GameSpirit(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSpirit):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < win_width - 80: 
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < win_width - 80: 
            self.rect.y += self.speed


font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 50)
win = font2.render("1 PLAYER WIN!", True, (180, 0, 0))
lose = font2.render("2 PLAYER WIN!", True, (180, 0, 0))
racket = Player("racket.png", 100, 200, 30, 90, 10)
racket2 = Player("racket2.png", 900, 200, 30, 90, 10)
ball = GameSpirit("tenis_ball.png", 500, 200, 70, 60, 0)
seeds = GameSpirit("seeds.png", randrange(200, 800),randrange(100, 400), 80, 80, 5)
wood = GameSpirit("wood.jpg", 0, 0, 1000, 500, 0 )


speed_x = 3
speed_y = 3

mixer.music.play()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.fill(back)
        wood.update()
        wood.reset()
        racket.update()
        racket.reset()
        racket2.update2()
        racket2.reset()
        ball.update()
        ball.reset()
        seeds.update()
        seeds.reset()

    

        if sprite.collide_rect(racket, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1.1
            speed_y *= 1.1
        
        if sprite.collide_rect(seeds, ball):
            seeds.kill()


        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            mixer.music.play("win.mp3")
            finish = True
            window.blit(win, (200,200))

        if ball.rect.x > 900:
            mixer.music.play("win.mp3")
            finish = True
            window.blit(lose, (200,200))
        



    display.update()
    clock.tick(FPS)


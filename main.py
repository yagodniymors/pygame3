from pygame import *
init()
class Label(sprite.Sprite):
    def __init__(self, text, font_size,x,y,color):
        super().__init__()
        self.image = font.Font(None,font_size).render(text,True,color)
        self.x = x
        self.y = y
        self.font_size = font_size
        self.color = color
    def set_text(self,text,color):
        self.image = font.Font(None, self.font_size).render(text, True, self.color)
    def reset(self):
        window.blit(self.image, (self.x, self.y))
class Sprite(sprite.Sprite):
    def __init__(self, filename, x, y, width, long):
        super().__init__()
        self.image = transform.scale(image.load(filename), (width, long))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y ))
class Ball(Sprite):
    def __init__(self, filename, x, y , width, long):
        super().__init__(filename, x, y, width, long)
        self.speed_x = 2
        self.speed_y = 2
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if ball.rect.y >= 400 or ball.rect.y < 0:
            self.speed_y = self.speed_y *(-1)
class Wall(Sprite):
    def __init__(self, filename, x, y, width, long, key_up, key_down):
        super().__init__(filename, x, y, width, long)
        self.speed = 2
        self.key_up = key_up
        self.key_down = key_down
    def update(self):
        keys = key.get_pressed()
        if keys[self.key_up]:
            self.rect.y = self.rect.y - self.speed
        if keys[self.key_down]:
            self.rect.y = self.rect.y + self.speed
window = display.set_mode((700,500))
background = transform.scale(image.load('images/background.webp'),(700, 500))
clock = time.Clock()
ball = Ball('images/ball.png', 200,200, 100,100)
player = Wall('images/player.jpg', 0, 100, 50,200, K_UP, K_DOWN)
player2 = Wall('images/player.jpg', 600,100,50,200, K_w, K_s)
score = 0
widget = Label(str(score),100, 300,300,(250,0,0))
game = True
while game:
    window.blit(background, (0,0))
    if ball.rect.x > 700:
        score = score + 1
        print(score)
        widget.set_text(str(score),(0,255,0) )
        ball.rect.x = 300
    if ball.rect.x <= 0:
        score = score - 1
        print(score)
        ball.rect.x = 400
        widget.set_text(str(score),(0,255,0))
    widget.reset()
    ball.reset()
    ball.update()
    player.reset()
    player.update()
    player2.reset()
    player2.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if player.rect.colliderect(ball.rect):
        ball.speed_x = ball.speed_x *(-1)
    if player2.rect.colliderect(ball.rect):
        ball.speed_x = ball.speed_x *(-1)
    display.update()
    clock.tick(144)

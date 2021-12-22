from pgzero.clock import Clock
import pgzrun
from random import randint

WIDTH = 1000
HEIGHT = 600
PLAYER_SPEED = 4

playing = True
game_over = False
lives_count = 3
hedge_speed = 4
score = 0

fox = Actor('fox')
fox.pos = 100, 100

hedge = Actor('hedgehog_left')
hedge.pos = (WIDTH + 27.5, 100)

lives = Actor('3_lives', (900, 35))

coin = Actor('coin')

music.play('theme')
music.set_volume(0.05)

def draw():
    global score
    
    screen.fill('light blue')

    fox.draw()
    coin.draw()
    hedge.draw()
    lives.draw()

    show_score(score)

def on_mouse_down(pos):
    screen.fill('light blue')

def place_coin():
    coin.x = randint(15, 985)
    coin.y = randint(15, 585)

def show_score(score):
    result = str(score)

    if score == 1:
        result = result + ' point'
    else:
        result = result + ' points'

    screen.draw.text(result, topleft=(10, 10), fontsize = 60)

def handle_navigation():
    if keyboard.rctrl or keyboard.lctrl:
        speed = PLAYER_SPEED * 2
    else:
        speed = PLAYER_SPEED

    if keyboard.left or keyboard.a:
        fox.x = fox.x - speed

    if keyboard.right or keyboard.d:
        fox.x = fox.x + speed
    
    if keyboard.up or keyboard.w:
        fox.y = fox.y - speed

    if keyboard.down or keyboard.s:
        fox.y = fox.y + speed

    if fox.x > WIDTH + 31:
        fox.x = -31

    if fox.x < -31:
        fox.x = WIDTH + 31

    if fox.y > HEIGHT + 41.5:
        fox.y = -41.5
    
    if fox.y < -41.5:
        fox.y = HEIGHT + 41.5

def move_hedge():
    global hedge_speed
    
    if not playing:
        return

    hedge.x = hedge.x - hedge_speed
    if hedge.x < -27.5:
        hedge.y = randint(0, 600)
        hedge.x = WIDTH + 27.5
        hedge_speed = randint(10, 20)

def life_lost():
    lives.image = str(lives_count) + '_lives'

def update():
    global score
    global lives_count
    global playing

    move_hedge()

    handle_navigation()

    if fox.colliderect(hedge) and playing:
        playing = False
        lives_count = lives_count - 1
        life_lost()

    if fox.colliderect(coin):
        sounds.coin.play()
        score = score + 1
        show_score(score)
        place_coin() 

place_coin()

pgzrun.go()

import pygame
import random
from os import path 

#파일
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd') 

WIDTH = 600
HEIGHT = 400
FPS = 80

#색설정
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#시작/창 설정
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE WAR")
clock = pygame.time.Clock()

#폰트/텍스트상자
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

#몬스터 그룹
def newmob0():
    m = Mob0()
    all_sprites.add(m)
    mobs0.add(m)

def newmob1():
    m = Mob1()
    all_sprites.add(m)
    mobs1.add(m)

def newmob2():
    m = Mob2()
    all_sprites.add(m)
    mobs2.add(m)

#실드바
def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 400
    BAR_HEIGHT = 10
    fill = pct
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, WHITE, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def draw_shield_bar2(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 400
    BAR_HEIGHT = 10
    fill = 400-pct
    outline_rect = pygame.Rect(x+pct, y, 400-pct, BAR_HEIGHT)
    fill_rect = pygame.Rect(x+pct, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)
#플레이어
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.current_frame = 0
        self.animation_frames = explosion_anim['Run']
        self.attack_animation_frames = explosion_anim['Attack']
        self.attack = False
        self.image = pygame.transform.scale(self.animation_frames[self.current_frame], (150,150))


        self.rect = self.image.get_rect()
        self.radius = 1
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = 100
        self.rect.centery = 235
        self.speedx = 0
        self.shield =200
        self.last_shot = pygame.time.get_ticks()


    def collide_with_mob(self):
        self.attack = True
        self.current_frame = 0
        self.animation_frames = self.attack_animation_frames
        

#플레이어 업데이트
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_1]:
            self.rect.centery = 125
        if keystate[pygame.K_2]:
            self.rect.centery = 235
        if keystate[pygame.K_3]:
            self.rect.centery = 345 
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.attack:
            # Update attack animation frame
            self.current_frame += 1
            if self.current_frame >= len(self.attack_animation_frames):
                self.attack = False
                self.current_frame = 0
                self.animation_frames = explosion_anim['Run']
            self.image = pygame.transform.scale(self.attack_animation_frames[self.current_frame], (150,150))
        else:
            # Update ideal animation frame
            self.current_frame += 1
            if self.current_frame >= len(self.animation_frames):
                self.current_frame = 0
            self.image = pygame.transform.scale(self.animation_frames[self.current_frame], (150, 150))
#몬스터
class Mob0(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = star0_img
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.x = WIDTH 
        self.rect.centery = 125
        self.speedx = 7
        self.spawn_delay = random.randint(2000, 5000)  # Random delay between spawns
        self.last_spawn_time = pygame.time.get_ticks() + self.spawn_delay     
   

#업데이트
    def update(self):
        self.rect.x -= self.speedx
        if self.rect.x<= 0:
            player.shield -= 10
            self.respawn()
            self.kill()

    def respawn(self):
        mob0 = Mob0()
        mobs0.add(mob0)
        all_sprites.add(mob0)
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time >= self.spawn_delay:
            self.rect.x = WIDTH
            self.rect.centery = 125
            self.last_spawn_time = current_time
            
            


          

class Mob1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = star1_img
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.x = WIDTH+320
        self.rect.centery = 235
        self.speedx = 7
        self.spawn_delay = random.randint(2000, 5000)  # Random delay between spawns
        self.last_spawn_time = pygame.time.get_ticks() + self.spawn_delay     
   

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.x<=0:
            player.shield -= 10
            self.respawn()
            self.kill()

    def respawn(self):
        mob1 = Mob1()
        mobs1.add(mob1)
        all_sprites.add(mob1)
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time >= self.spawn_delay:
            self.rect.x = WIDTH+320
            self.rect.centery = 235
            self.last_spawn_time = current_time
            
    

class Mob2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = star2_img
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = WIDTH+160
        self.rect.centery = 345 

        self.speedx = 7
        self.spawn_delay = random.randint(2000, 5000)  # Random delay between spawns
        self.last_spawn_time = pygame.time.get_ticks() + self.spawn_delay     
   

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.x<=0:
            player.shield-=10
            self.respawn()
            self.kill()

    def respawn(self):
        mob2 = Mob2()
        mobs2.add(mob2)
        all_sprites.add(mob2)
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time >= self.spawn_delay:
            self.rect.x = WIDTH+160
            self.rect.centery = 345
            self.last_spawn_time = current_time
            
    

#폭발
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
#업데이트
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
#스크린 
def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "RHYTHM HERO", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "1 is ORANGE 2 is GREEN 3 is BLUE", 22,
              WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Press SPACEBAR to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    #게임 시작/끝내기
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_SPACE]:
                waiting = False
    pygame.mixer.music.load(path.join(snd_dir, 'BossBattle.ogg'))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1) 
#우승 스크린
def win_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "congratulations", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "defended the city!", 22,
              WIDTH / 2, HEIGHT / 2)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                      


# 게임 그래픽
background = pygame.image.load(path.join(img_dir, "street.png")).convert()
background= pygame.transform.scale(background, (1600, 800))
background_rect = background.get_rect()





star0_img = pygame.image.load(path.join(img_dir, "star0.png")).convert()
star1_img = pygame.image.load(path.join(img_dir, "star1.png")).convert()
star2_img = pygame.image.load(path.join(img_dir, "star2.png")).convert()
star0_img= pygame.transform.scale(star0_img, (100, 100))
star1_img= pygame.transform.scale(star1_img, (100, 100))
star2_img= pygame.transform.scale(star2_img, (100, 100))

square = pygame.image.load(path.join(img_dir, "square.png")).convert()
square = pygame.transform.scale(square, (600, 340))
square.set_alpha(100)

explosion_anim = {}
explosion_anim['1'] = []
explosion_anim['2'] = []
explosion_anim['3'] = []
explosion_anim['Run'] = []
explosion_anim['Attack'] = []
for i in range(3):
    filename = 'effect1_0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_1 = pygame.transform.scale(img, (60, 60))
    explosion_anim['1'].append(img_1)
    filename = 'effect2_0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_2 = pygame.transform.scale(img, (60, 60))
    explosion_anim['2'].append(img_2)
    filename = 'effect3_0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_3 = pygame.transform.scale(img, (60, 60))
    explosion_anim['3'].append(img_3)
    

for i in range(7):
    filename = 'Run_0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_Run = pygame.transform.scale(img, (100, 100))
    explosion_anim['Run'].append(img_Run)

for i in range(6):
    filename = 'Attack_0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_Attack = pygame.transform.scale(img, (100, 100))
    explosion_anim['Attack'].append(img_Attack)

#게임사운드

attack_sound=pygame.mixer.Sound(path.join(snd_dir, "pew.wav"))
attack_sound.set_volume(0.2)




#그룹
all_sprites = pygame.sprite.Group()
mobs0 = pygame.sprite.Group()
mobs1 = pygame.sprite.Group()
mobs2 = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(3):
    newmob0()
    newmob1()
    newmob2()



#게임루프
game_over = True
running = True
you_win=False

while running:
    if you_win:
        win_screen()
        you_win=False
    if game_over:
        show_go_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        mobs0 = pygame.sprite.Group()
        mobs1 = pygame.sprite.Group()
        mobs2 = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(3):
            newmob0()
            newmob1()
            newmob2()
        score = 0   


    #적당한 소리
    clock.tick(FPS)
    #창닫기
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #업데이트
    all_sprites.update()

    # 몹->플레이어 충돌 체크
    hits0 = pygame.sprite.spritecollide(player, mobs0, True, pygame.sprite.collide_circle)
    for hit in hits0:
        player.collide_with_mob()
        player.shield += 2
        expl = Explosion(hit.rect.center, '1')
        attack_sound.play()
        all_sprites.add(expl)
        mob0 = Mob0()
        mobs0.add(mob0)
        all_sprites.add(mob0)
       
        
    hits1= pygame.sprite.spritecollide(player, mobs1, True, pygame.sprite.collide_circle)
    for hit in hits1:
        player.collide_with_mob()
        player.shield += 2
        expl = Explosion(hit.rect.center, '2')
        attack_sound.play()
        all_sprites.add(expl)
        mob1 = Mob1()
        mobs1.add(mob1)
        all_sprites.add(mob1)
     
        
    hits2 = pygame.sprite.spritecollide(player, mobs2, True, pygame.sprite.collide_circle)
    for hit in hits2:
        player.collide_with_mob()
        player.shield += 2
        expl = Explosion(hit.rect.center, '3')
        attack_sound.play()
        all_sprites.add(expl)
        mob2 = Mob2()
        mobs2.add(mob2)
        all_sprites.add(mob2)
   



    


    #승패판별   
    if player.shield <= 0:
        game_over = True
    if player.shield >=400:
        you_win = True

        

    # 그리기
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    screen.blit(square, (0,60))
    pygame.draw.line(screen, BLACK, (0,175),(600,175))
    pygame.draw.line(screen, BLACK, (0,285),(600,285))
    all_sprites.draw(screen)
    draw_shield_bar(screen, 100, 5, player.shield)
    draw_shield_bar2(screen, 100, 5, player.shield)
    draw_text(screen, "MY POWER", 10, 60, 5)
    draw_text(screen, "ENEMY POWER", 10, 540, 5)
    # 화면 플립
    pygame.display.flip()

pygame.quit()
import pygame
import math
import sys
pygame.init()
pygame.mixer.init()
# bgm&background
pygame.mixer.music.load("sounds/background.wav")
pygame.mixer.music.set_volume(0.15)
pygame.mixer.music.play(-1)

def reset_game():
    global player_x, player_y, player_velocity_y
    global coin_count, game_clear, clear_time
    global enemies, is_jumping, facing_right
    is_jumping = False
    facing_right = True
    player_x = 100
    player_y = 440
    player_velocity_y = 0

    coin_count = 0
    game_clear = False
    clear_time = None
    for coin in coins:
        coin["collected"] = False

    for box in boxs:
        box["used"] = False

    enemies = [
    {
        "orginal_x": 800,
        "x": 800,
        "y": GROUND_Y - 40,
        "vx": -1.2,
        "vy": 0,
        "alive": True,
        "death_timer": 0,
        "flipped": False,
        "falling": False
    },
    {
        "orginal_x": 1200,
        "x": 1200,
        "y": GROUND_Y - 40,
        "vx": -1.0,
        "vy": 0,
        "alive": True,
        "death_timer": 0,
        "flipped": False,
        "falling": False
    },
    {
        "orginal_x": 275,
        "x": 275,
        "y": 0,
        "vx": -1.2,
        "vy": 0,
        "alive": True,
        "death_timer": 0,
        "flipped": False,
        "falling": False
    }
]
# Camera
camera_x = 0
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("An easy mario-liked game")
# Color Set
SKY_BLUE = (135, 206, 235)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLACK = (0,0,0)
BROWN = (139, 69, 19)
WHILE = (255, 255, 255)
MARIO_RED = (226, 29, 29) 
MARIO_BLUE = (33, 119, 184)
MARIO_SKIN = (255, 180, 125)
MARIO_BROWN = (184, 111, 80)
MARIO_WHITE = (255, 255, 255)
# Buildings & Background
WORLD_WIDTH = 3000
GROUND_Y = 500
Platforms = [
    (200, 400, 150, 20),
    (400, 350, 150, 20),
    (600, 300, 150, 20),
]
coins = [
    {"x": 230, "y": 360, "collected": False},
    {"x": 430, "y": 310, "collected": False},
    {"x": 630, "y": 260, "collected": False}
]
goal_flag = {
    "x": 2800,
    "y": 300,
    "width": 20,
    "height": 140
}
boxs = [
    {"x": 500, "y": 350, "used": False},
    {"x": 900, "y": 350, "used": False}
]
clouds = [
    {"x": 100, "y": 80, "speed": 0.2},
    {"x": 400, "y": 120, "speed": 0.15},
    {"x": 800, "y": 60, "speed": 0.25},
    {"x": 1400, "y": 100, "speed": 0.18},
]
trees = [
    {"x": 300, "y": GROUND_Y, "scale": 1.0},
    {"x": 700, "y": GROUND_Y, "scale": 1.2},
    {"x": 1200, "y": GROUND_Y, "scale": 0.9},
    {"x": 1800, "y": GROUND_Y, "scale": 1.1},
    {"x": 2300, "y": GROUND_Y, "scale": 1.2},
    {"x": 2700, "y": GROUND_Y, "scale": 1.3}
]
# Sound
coin_sound = pygame.mixer.Sound("sounds/coinss.wav")
coin_sound.set_volume(0.2)
jump_sound = pygame.mixer.Sound("sounds/jump.wav")
jump_sound.set_volume(0.25)
mario_dath = pygame.mixer.Sound("sounds/death.wav")
mario_dath.set_volume(0.5)
shot_sound = pygame.mixer.Sound("sounds/shot.wav")
shot_sound.set_volume(0.2)
enemy_death_sound = pygame.mixer.Sound("sounds/enemy_death.wav")
enemy_death_sound.set_volume(0.25)
flag_sound = pygame.mixer.Sound("sounds/shot.wav")
flag_sound.set_volume(0.4)
# Flag
flag_current_y = goal_flag["y"]
flag_target_y = goal_flag["y"] + goal_flag["height"] - 40
flag_speed = 2
flag_dropping = False
# Attack
is_attacking = False
attack_timer = 0
ATTACK_DURATION = 10
bullets = []
# Sports
player_velocity_y = 0
is_jumping = False
GARVITY = 0.5
JUMP_POWER = -12

game_clear = False
# Player
player_x = 100
player_y = 440
player_speed = 5
enemy_up_speed = 4
enemies = [
    {
        "orginal_x": 900,
        "x": 800,
        "y": GROUND_Y - 40,
        "vx": -1.2,
        "vy": 0,
        "alive": True,
        "death_timer": 0,
        "flipped": False,
        "falling": False
    },
    {
        "orginal_x": 500,
        "x": 500,
        "y": GROUND_Y - 40,
        "vx": -1.2,
        "vy": 0,
        "alive": True,
        "death_timer": 0,
        "flipped": False,
        "falling": False
    },
    {
        "orginal_x": 1600,
        "x": 1500,
        "y": GROUND_Y - 40,
        "vx": -1.2,
        "vy": 0,
        "alive": True,
        "death_timer": 0,
        "flipped": False,
        "falling": False
    },
    {
        "orginal_x": 1800,
        "x": 1800,
        "y": GROUND_Y - 40,
        "vx": -1.2,
        "vy": 0,
        "alive": True,
        "death_timer": 0,
        "flipped": False,
        "falling": False
    },
    {
        "orginal_x": 2300,
        "x": 2200,
        "y": GROUND_Y - 40,
        "vx": -1.2,
        "vy": 0,
        "alive": True,
        "death_timer": 0,
        "flipped": False,
        "falling": False
    },
    {
        "orginal_x": 2600,
        "x": 2600,
        "y": GROUND_Y - 40,
        "vx": -1.2,
        "vy": 0,
        "alive": True,
        "death_timer": 0,
        "flipped": False,
        "falling": False
    },
    {
        "orginal_x": 1200,
        "x": 1200,
        "y": GROUND_Y - 40,
        "vx": -1.0,
        "vy": 0,
        "alive": True,
        "death_timer": 0,
        "flipped": False,
        "falling": False
    },
    {
        "orginal_x": 275,
        "x": 275,
        "y": 0,
        "vx": -1.2,
        "vy": 0,
        "alive": True,
        "death_timer": 0,
        "flipped": False,
        "falling": False
    }
]
# Time
clear_time = None
clock = pygame.time.Clock()
FPS = 60
coin_time = 0
start_time = pygame.time.get_ticks()
# Calculation
coin_count = 0
# Animal
walk_frame = 0
walk_timer = 0
WALk_SPEED = 0.15
facing_right = True
def check_bullet_hit_enemies(bullets, enemies):
    for bullet in bullets:
        if not bullet["alive"]:
            continue

        bullet_rect = pygame.Rect(
            bullet["x"] - 2,
            bullet["y"] - 2,
            4,
            4
        )

        for enemy in enemies:
            if not enemy["alive"]:
                continue

            enemy_rect = pygame.Rect(
                enemy["x"],
                enemy["y"],
                40,
                30
            )

            if bullet_rect.colliderect(enemy_rect):
                bullet["alive"] = False
                enemy_death_sound.play()

                enemy["alive"] = False
                enemy["death_timer"] = 30
                enemy["flipped"] = True
                enemy["falling"] = True

                return

def check_box_hit(player_x, player_y, velocity_y, boxs):
    for box in boxs:
        if box["used"]:
            continue
        box_rect = pygame.Rect(box["x"], box["y"], 40, 50)
        player_head = pygame.Rect(player_x + 5, player_y, 30, 5)

        # up to hit
        if velocity_y < 0 and player_head.colliderect(box_rect):
            box["used"] = True
            return box
    return None
def draw_cloud(x,y):
    pygame.draw.circle(screen, WHILE, (x,y), 30)
    pygame.draw.circle(screen, WHILE, (x + 25,y - 10), 25)
    pygame.draw.circle(screen, WHILE, (x + 25,y + 10), 25)
    pygame.draw.circle(screen, WHILE, (x + 50,y), 30)
def draw_tree(x, y, scale):
    trunk_w = int(20 * scale)
    trunk_h = int(60 * scale)
    leaf_r = int(35 * scale)

    pygame.draw.rect(
        screen,
        BROWN,
        (x - trunk_w // 2, y - trunk_h, trunk_w, trunk_h)
    )

    pygame.draw.circle(
        screen,
        GREEN,
        (x, y - trunk_h),
        leaf_r
    )
def update_draw_cloud():
    for cloud in clouds:
        cloud["x"] += cloud["speed"]

        if cloud["x"] > WORLD_WIDTH + 100:
            cloud = -100
        screen_x = cloud["x"] - camera_x * 0.5
        draw_cloud(screen_x, cloud["y"])
def draw_trees():
    for tree in trees:
        screen_x = tree["x"] - camera_x * 0.8
        draw_tree(screen_x, tree["y"], tree["scale"])
def draw_box(box):
    x = box["x"] - camera_x
    y = box["y"]
    color = (255, 200, 0) if not box["used"] else (160, 160, 160)
    pygame.draw.rect(screen, color, (x, y, 40, 40))
    pygame.draw.rect(screen, (0, 0, 0), (x, y, 40, 40), 2)
    if not box["used"]:
        font = pygame.font.Font(None, 36)
        q = font.render("?", True, (0, 0, 0))
        screen.blit(q, (x + 12, y + 6))
def check_goal(player_x, player_y,flag):
    player_rect = pygame.Rect(player_x,player_y,40,60)
    flag_rect = pygame.Rect(
        flag["x"],
        flag["y"],
        flag["width"],
        flag["height"]
    )
    return player_rect.colliderect(flag_rect)
def draw_goal_flag(flag):
    x = flag["x"] - camera_x
    y = flag_current_y

    pygame.draw.rect(screen, (200,200,200), (x,y,6,flag["height"]))
    pygame.draw.polygon(
        screen,
        (255,0,0),
        [
            (x+6,y+10),
            (x+60, y+30),
            (x+6,y+50)
        ]
    )
def draw_coin(coin,t):
    offset = math.sin(t + coin["x"] * 0.05) * 4
    pygame.draw.circle(
        screen,
        (255,215,0),
        (coin["x"] - camera_x,coin["y"] + offset),
        10
    )
def draw_enemy(enemy):
    if not enemy["alive"] and not enemy["falling"]:
        return

    x = enemy["x"] - camera_x
    y = enemy["y"]

    if enemy["flipped"] and enemy["falling"]:
        y += enemy_up_speed

    pygame.draw.ellipse(screen, (150, 75, 0), (x, y, 40, 30))
    pygame.draw.circle(screen, (0, 0, 0), (x + 12, y + 12), 3)
    pygame.draw.circle(screen, (0, 0, 0), (x + 28, y + 12), 3)
def update_enemies(enemies):
    for enemy in enemies:
        if enemy["falling"]:
            enemy["death_timer"] -= 1
            enemy["y"] += enemy_up_speed
            continue
        if enemy["death_timer"] <= 0:
            enemy["falling"] = False
        if not enemy["alive"]:
            continue

        enemy["vy"] += GARVITY
        enemy["y"] += enemy["vy"]
        enemy["x"] += enemy["vx"]

        if enemy["y"] > GROUND_Y - 40:
            enemy["y"] = GROUND_Y - 40
            enemy["vy"] = 0

        for plat in Platforms:
            px, py, pw, ph = plat

            if (enemy["vy"] > 0 and
                enemy["y"] + 40 <= py + 5 and
                enemy["y"] + 40 + enemy["vy"] >= py and
                enemy["x"] + 40 > px and
                enemy["x"] < px + pw):
                enemy["y"] = py - 40
                enemy["vy"] = 0
                
            if (enemy["y"] + 40 > py and
                enemy["y"] < py + ph):
                if enemy["x"] + 40 >= px and enemy["x"] + 40 <= px + 5:
                    enemy["vx"] *= -1
                if enemy["x"] <= px + pw and enemy["x"] >= px + pw - 5:
                    enemy["vx"] *= -1

            if enemy["x"] < enemy["orginal_x"] - 100 or enemy["x"] > enemy["orginal_x"] + 100:
                enemy["vx"] *= -1
def draw_bullet(bullet):
    screen_x = bullet["x"] - camera_x
    screen_y = bullet["y"]

    pygame.draw.circle(
        screen,
        (0, 0, 0),
        (int(screen_x), int(screen_y)),
        4
    )
def check_coin_collision(player_x, player_y, coins):
    global coin_count
    player_rect = pygame.Rect(player_x, player_y, 40, 60)
    
    for coin in coins:
        if coin["collected"]:
            continue
        coin_rect = pygame.Rect(coin["x"] - 8, coin["y"] - 8, 16, 16)
        if player_rect.colliderect(coin_rect):
            coin["collected"] = True
            coin_count += 1
            coin_sound.play()
def check_enemy_collision(player_x, player_y, velocity_y, enemies):
    player_rect = pygame.Rect(player_x, player_y, 40, 60)
    player_bottom = player_y + 60

    for enemy in enemies:
        if not enemy["alive"]:
            continue

        enemy_rect = pygame.Rect(enemy["x"], enemy["y"], 40, 30)

        # victory
        if (velocity_y > 0 and
            player_bottom <= enemy["y"] + 10 and
            player_rect.colliderect(enemy_rect)):
            enemy["alive"] = False
            enemy["death_timer"] = 30
            enemy["flipped"] = True
            enemy["falling"] = True
            return "stomp"

        # game over
        if player_rect.colliderect(enemy_rect):
            return "hit"

    return None

# ========== Function ==========
 
def draw_background():
    screen.fill(SKY_BLUE)

    for x in range(0, WORLD_WIDTH, 100):
        pygame.draw.rect(
            screen,
            GREEN,
            (x - camera_x, GROUND_Y, 100, 100)############
        )
    update_draw_cloud()
    draw_trees()
    font = pygame.font.Font(None,45)    
    text = font.render(f"Anglos's Adventure", True, WHILE)
    screen.blit(text, (500,25))

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True
def draw_player(x, y, frame, facing_right):
    pygame.draw.ellipse(screen, MARIO_RED, (x, y - 12, 40, 18))   # 帽顶
    pygame.draw.rect(screen, MARIO_RED, (x, y, 40, 10))           # 帽檐

    pygame.draw.rect(screen, MARIO_SKIN, (x + 6, y + 8, 28, 20))

    pygame.draw.ellipse(screen, MARIO_SKIN, (x + 22, y + 14, 10, 8))

    pygame.draw.circle(screen, (0, 0, 0), (x + 16, y + 16), 2)
    pygame.draw.circle(screen, (0, 0, 0), (x + 22, y + 16), 2)
    pygame.draw.rect(screen, MARIO_BROWN, (x + 12, y + 20, 16, 4))

    pygame.draw.rect(screen, MARIO_RED, (x + 6, y + 28, 28, 10))

    pygame.draw.rect(screen, MARIO_BLUE, (x + 4, y + 38, 32, 14))


    pygame.draw.rect(screen, MARIO_BLUE, (x + 10, y + 28, 4, 12))
    pygame.draw.rect(screen, MARIO_BLUE, (x + 26, y + 28, 4, 12))

    pygame.draw.circle(screen, (255, 255, 0), (x + 12, y + 40), 2)
    pygame.draw.circle(screen, (255, 255, 0), (x + 28, y + 40), 2)

    pygame.draw.rect(screen, MARIO_SKIN, (x - 4, y + 32, 8, 10))
    pygame.draw.rect(screen, MARIO_SKIN, (x + 36, y + 32, 8, 10))

    leg_offset_y = 3 if frame == 0 else -3
    leg_offset_x = 3 if frame == 0 else -3

    if not facing_right:
        leg_offset_x = -leg_offset_x

    # Left_leg
    pygame.draw.rect(
        screen,
        MARIO_BROWN,
        (x + 4 + leg_offset_x, y + 52 + leg_offset_y, 14, 6)
    )

    # Right_leg
    pygame.draw.rect(
        screen,
        MARIO_BROWN,
        (x + 22 - leg_offset_x, y + 52 - leg_offset_y, 14, 6)
    )
    font = pygame.font.Font(None,18)
    text = font.render("Angelos", True, BLACK)
    screen.blit(text, (x - 5, y - 25))

def update_player_position(keys, x, y, speed, velocity_y, jumping):
    new_x = x
    new_y = y
    new_velocity_y = velocity_y
    new_jumping = jumping
    global facing_right

    new_y, new_velocity_y, new_jumping = check_platform_collision(new_x, new_y,new_velocity_y,Platforms)
    new_y, new_velocity_y, new_jumping = check_box_collision(new_x, new_y,new_velocity_y, boxs)
    if keys[pygame.K_SPACE] and not new_jumping:
        new_velocity_y = JUMP_POWER
        new_jumping = True
        jump_sound.play()

    new_velocity_y += GARVITY
    new_y += new_velocity_y
    moving = False
    if keys[pygame.K_a]:
        new_x -= speed
        facing_right = False
        moving = True
    if keys[pygame.K_d]:
        new_x += speed
        facing_right = True
        moving = True

    if new_x < 0:
        new_x = 0
    if new_x > WORLD_WIDTH - 40:
        new_x = WORLD_WIDTH - 40
    if new_y < 0:
        new_y = 0
    if new_y > GROUND_Y - 60:
        new_y = GROUND_Y - 60
    return new_x, new_y, new_velocity_y, new_jumping, moving
def update_bullets(bullets):
    for bullet in bullets:
        if not bullet["alive"]:
            continue

        bullet["x"] += bullet["vx"]

        if bullet["x"] < 0 or bullet["x"] > WORLD_WIDTH:
            bullet["alive"] = False

def draw_platform(x, y, length, width):
    pygame.draw.rect(screen, BROWN,(x, y, length, width)) 
    pygame.draw.rect(screen, (101, 67, 33),(x+2, y+2, length-4, width-4))

def check_platform_collision(x, y, velocity_y, platforms):
    new_y = y
    realnew_y = new_y + velocity_y
    player_bottom = new_y + 60
    new_velocity_y = velocity_y

    for platform in platforms:
        plat_x, plat_y, plat_length, plat_width = platform

        if (new_velocity_y > 0 and
            plat_y >= player_bottom - 1 and
            realnew_y + 61 >= plat_y and
            x + 40 > plat_x and
            x < plat_x + plat_length):
            new_y = plat_y - 60
            new_velocity_y = 0
            global is_jumping
            is_jumping = False

        if (new_velocity_y < 0 and
            realnew_y <= plat_y + plat_width <= new_y and
            x + 40 > plat_x and
            x < plat_x + plat_length):
            new_y = plat_y + plat_width
            new_velocity_y = 0
    return new_y, new_velocity_y, is_jumping
def check_box_collision(x,y,velocity_y,boxs):
    new_y = y
    realnew_y = new_y + velocity_y
    new_velocity_y = velocity_y
    for box in boxs:
        box_x = box["x"]
        box_y = box["y"]
        if(new_velocity_y < 0 and
           realnew_y <= box_y + 40 <= new_y and
           x + 40 > box_x and
           x < box_x + 40):
            new_y = box_y + 60
            new_velocity_y = 0
        if(new_velocity_y > 0 and
           box_y >= new_y - 59 and
           realnew_y + 61 >= box_y and
           x + 40 > box_x and
           x < box_x + 40):
            new_y = box_y - 60
            new_velocity_y = 0
            global is_jumping
            is_jumping = False
    return new_y, new_velocity_y, is_jumping
# ========== Game ==========
running = True 

while running:
    running = handle_input()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        reset_game()
    if keys[pygame.K_ESCAPE]:
        running = False

    camera_x = player_x - 400#######
    camera_x = max(0, min(camera_x, WORLD_WIDTH - 800))#######

    player_x, player_y, player_velocity_y, is_jumping, moving = update_player_position(
        keys,
        player_x,
        player_y,
        player_speed,
        player_velocity_y,
        is_jumping
    )
    if flag_dropping:
        if flag_current_y < flag_target_y:
            flag_current_y += flag_speed
        else:
            flag_current_y = flag_target_y
            flag_dropping = False

    if is_attacking:
        attack_timer -= 1
        if attack_timer <= 0:
            is_attacking = False

    if keys[pygame.K_j] and not is_attacking:
        shot_sound.play()
        is_attacking = True
        attack_timer = ATTACK_DURATION

        bullets.append({
            "x": player_x + (40 if facing_right else 0),
            "y": player_y + 30,
            "vx": 12 if facing_right else -12,
            "alive": True
        })
            
    result = check_enemy_collision(player_x, player_y, player_velocity_y, enemies)

    if result == "stomp":
        player_velocity_y = -8
    elif result == "hit":
        reset_game()
        mario_dath.play()
    hit_box = check_box_hit(player_x, player_y, player_velocity_y, boxs)
    if hit_box:
        coins.append({
            "x": hit_box["x"] + 20,
            "y": hit_box["y"] - 20,
            "collected": False
        })
    # Enginer
    if moving:
        walk_timer += WALk_SPEED
    if walk_timer >= 1:
        walk_frame = (walk_frame + 1) % 2
        walk_timer = 0
    else:
        walk_frame = 0

    draw_background()
    if player_y == 440:
        is_jumping = False

    draw_platform(200 - camera_x,400,150,20)
    draw_platform(400 - camera_x,350,150,20)
    draw_platform(600 - camera_x,300,150,20)
    for box in boxs:
        draw_box(box)
    for coin in coins:
        if not coin["collected"]:
            draw_coin(coin, coin_time)
            coin_time += 0.05
    check_coin_collision(player_x, player_y, coins)
    draw_player(player_x - camera_x, player_y, walk_frame, facing_right)
    update_bullets(bullets)
    for bullet in bullets:
        if bullet["alive"]:
            draw_bullet(bullet)

    for enemy in enemies:
        draw_enemy(enemy)
    update_enemies(enemies)
    check_bullet_hit_enemies(bullets, enemies)
    draw_goal_flag(goal_flag)
    if not game_clear and check_goal(player_x,player_y,goal_flag):
            game_clear = True
            clear_time = pygame.time.get_ticks()
            player_speed = 0
            flag_sound.play()
            flag_dropping = True
    if game_clear:
        if pygame.time.get_ticks() - clear_time < 3000:
            font = pygame.font.Font(None, 80)
            text = font.render("COURSE CLEAR!", True, (255,255,0))
            screen.blit(text,(200,200))
    if game_clear and check_goal(player_x, player_y,goal_flag):
        clear_time = pygame.time.get_ticks()
    if pygame.time.get_ticks() - start_time < 3000:
        font = pygame.font.Font(None,60)    
        text = font.render("MARIO GAME!", True, WHILE)
        screen.blit(text, (250,250))
    coin_number = font.render(f"Coins:{coin_count}", True, RED)
    screen.blit(coin_number, (20,20))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
pygame.mixer.music.stop()
sys.exit()
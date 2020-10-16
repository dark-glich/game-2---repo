import random

import pygame
import os
import math

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, 24)

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path
image_path = os.path.join(resource_path, 'images')

caption = pygame.display.set_caption("DESTROYER")
i = "icon.png"
icon = pygame.image.load("/home/mmohdbilal/bilal/game-2---repo/icon.png")
pygame.display.set_icon(icon)
playerIMG = pygame.image.load('/home/mmohdbilal/bilal/game-2---repo/spaceship (7).png')

playerX = 650
playerY = 630
playerX_change = 0

enemyIMG = pygame.image.load("/home/mmohdbilal/bilal/game-2---repo/meteor.png")

enemyX = random.randint(20, 1200)
enemyY = -300
enemyY_change = 10

enemy2IMG = pygame.image.load("/home/mmohdbilal/bilal/game-2---repo/asteroid.png")

enemy2X = random.randint(20, 1200)
enemy2Y = -500
enemy2Y_change = 0

enemy3IMG = pygame.image.load("/home/mmohdbilal/bilal/game-2---repo/asteroid2.png")

enemy3X = random.randint(20, 1200)
enemy3Y = -800
enemy3Y_change = 0

game = "on"

bulletIMG = pygame.image.load("/home/mmohdbilal/bilal/game-2---repo/dot.png")
bulletX = 605
bulletY = 590
bulletY_change = 40
bullet_state = "ready"

restartIMG = pygame.image.load("/home/mmohdbilal/bilal/game-2---repo/replay.png")
restartX = 400
restartY = -800

pauseIMG = pygame.image.load("/home/mmohdbilal/bilal/game-2---repo/pause.png")
pauseX = 1215
pauseY = -1500

font2 = pygame.font.Font("freesansbold.ttf", 100)
overX = -400
overY = -200

pe = pygame.font.Font("/home/mmohdbilal/bilal/game-2---repo/KurriIslandItaPERSONAL-Bold.ttf", 100)
peX = -400
peY = -200

py = pygame.font.Font("/home/mmohdbilal/bilal/game-2---repo/KurriIslandItaPERSONAL-Bold.ttf", 30)
pyX = -400
pyY = -200

on = pygame.font.Font("/home/mmohdbilal/bilal/game-2---repo/KurriIslandItaPERSONAL-Bold.ttf", 30)
onX = -400
onY = -200

bonus = pygame.font.Font("/home/mmohdbilal/bilal/game-2---repo/KurriIslandItaPERSONAL-Bold.ttf", 60)
bonusX = -400
bonusY = -200

resume = pygame.font.Font("/home/mmohdbilal/bilal/game-2---repo/KurriIslandItaPERSONAL-Bold.ttf", 30)
resumeX = -400
resumeY = -200

game_type = "start"

start = pygame.font.Font("/home/mmohdbilal/bilal/game-2---repo/SEASRN__.ttf", 200)
startX = -400
startY = -300

go = pygame.font.Font("/home/mmohdbilal/bilal/game-2---repo/KurriIslandItaPERSONAL-Bold.ttf", 100)
goX = 600
goY = -380

playIMG = pygame.image.load("/home/mmohdbilal/bilal/game-2---repo/play-button (1).png")
playX = 800
playY = -600

bonus_value = 0


def game_pause(x, y):
    pausing = pe.render("GAME PAUSED ", True, (0, 0, 0))
    screen.blit(pausing, (x, y))


def bonos(x, y):
    bonsed = bonus.render("BONUS +" + str(bonus_value), True, (0, 0, 0))
    screen.blit(bonsed, (x, y))


def paused(x, y):
    paus = py.render("click 'DOWN' button to pause", True, (0, 0, 0))
    screen.blit(paus, (x, y))


def game_resume(x, y):
    resuming = resume.render("click 'UP' button to resume", True, (0, 0, 0))
    screen.blit(resuming, (x, y))


def game_on(x, y):
    oning = on.render("click 'ENTER' key to start the game", True, (0, 0, 0))
    screen.blit(oning, (x, y))


def going(x, y):
    goer = go.render("PLAY", True, (0, 0, 0))
    screen.blit(goer, (x, y))


def play_game():
    screen.blit(playIMG, (playX, playY))


def game_start(x, y):
    starting = start.render("DESTROYER", True, (0, 0, 0))
    screen.blit(starting, (x, y))


def overs(x, y):
    overing = font2.render("GAME OVER", True, (0, 0, 0))
    screen.blit(overing, (x, y))


score_value = 0
font = pygame.font.Font("freesansbold.ttf", 100)
scoreX = 28
scoreY = 18

font3 = pygame.font.Font("freesansbold.ttf", 30)
reX = -699
reY = 90


def retry(x, y):
    retro = font3.render("CLICK 'ENTER' KEY TO RESTART ", True, (0, 0, 0))
    screen.blit(retro, (x, y))


def score(x, y):
    scoring = font.render(str(score_value), True, (0, 0, 0))
    screen.blit(scoring, (x, y))


def enemy():
    screen.blit(enemyIMG, (enemyX, enemyY))


def enemy2():
    screen.blit(enemy2IMG, (enemy2X, enemy2Y))


def enemy3():
    screen.blit(enemy3IMG, (enemy3X, enemy3Y))


def player():
    screen.blit(playerIMG, (playerX, playerY))


def res(x, y):
    screen.blit(restartIMG, (x, y))


def pause(x, y):
    screen.blit(pauseIMG, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIMG, (x, y))


def collide(enemyX, enemyY, bulletX, bulletY):
    difference = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    if difference <= 70:
        return True
    else:
        return False


def collide2(enemy2X, enemy2Y, bulletX, bulletY):
    difference = math.sqrt((enemy2X - bulletX) ** 2 + (enemy2Y - bulletY) ** 2)
    if difference <= 70:
        return True
    else:
        return False


def collide3(enemy3X, enemy3Y, bulletX, bulletY):
    difference = math.sqrt((enemy3X - bulletX) ** 2 + (enemy3Y - bulletY) ** 2)
    if difference <= 70:
        return True
    else:
        return False


def game_over(enemyX, enemyY, playerX, playerY):
    deff = math.sqrt((playerX - enemyX) ** 2 + (playerY - enemyY) ** 2)
    if deff <= 100:
        return True
    else:
        return False


def game2_over(enemy2X, enemy2Y, playerX, playerY):
    deff = math.sqrt((playerX - enemy2X) ** 2 + (playerY - enemy2Y) ** 2)
    if deff <= 100:
        return True
    else:
        return False


def game3_over(enemy3X, enemy3Y, playerX, playerY):
    deff = math.sqrt((playerX - enemy3X) ** 2 + (playerY - enemy3Y) ** 2)
    if deff <= 100:
        return True
    else:
        return False


def game_over2():
    if enemyY >= 650:
        return True
    else:
        return False


def game2_over2():
    if enemy2Y >= 650:
        return True
    else:
        return False


def game3_over3():
    if enemy3Y >= 650:
        return True
    else:
        return False


running = True
while running:

    screen.fill((200, 200, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -28

            if event.key == pygame.K_RIGHT:
                playerX_change = 28

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bulletX += 50
                    fire_bullet(bulletX, bulletY)

            if event.key == pygame.K_RETURN:
                if game == "over":
                    bullet_state = "ready"
                    onX = -400
                    onY = -200
                    bulletX = playerX
                    game_type = "not start"
                    restartX = 400
                    restartY = -800
                    bulletY_change = 40
                    bulletY = 610
                    bulletX += 50
                    playerX = 650
                    playerY = 630
                    enemyX = random.randint(20, 1200)
                    resumeX = -400
                    resumeY = -200
                    enemyY = -300
                    enemyY_change = 7
                    pauseX = 1215
                    pauseY = 15
                    pyX = 950
                    pyY = 150
                    enemy2X = random.randint(20, 1200)
                    enemy2Y = -500
                    enemy2Y_change = 0
                    enemy3X = random.randint(20, 1200)
                    enemy3Y = -800
                    enemy3Y_change = 0
                    overX = -400
                    overY = -200
                    scoreX = 28
                    scoreY = 18
                    reX = -699
                    reY = 90
                    startX = -400
                    startY = -300
                    score_value = 0

            if event.key == pygame.K_RETURN:
                if game == "new":
                    startX = -400
                    startY = -300
                    onX = -400
                    onY = -200
                    bullet_state = "ready"
                    bulletX = playerX
                    game_type = "not start"
                    restartX = 400
                    restartY = -800
                    bulletY_change = 40
                    bulletY = 610
                    bulletX += 50
                    playerX = 650
                    playerY = 630
                    enemyX = random.randint(20, 1200)
                    enemyY = -300
                    enemyY_change = 7
                    enemy2X = random.randint(20, 1200)
                    enemy2Y = -500
                    enemy2Y_change = 0
                    enemy3X = random.randint(20, 1200)
                    enemy3Y = -800
                    enemy3Y_change = 0
                    overX = -400
                    game = "off"
                    pyX = 950
                    pyY = 150
                    overY = -200
                    scoreX = 28
                    scoreY = 18
                    reX = -699
                    reY = 90
                    pauseX = 1215
                    pauseY = 15
                    playX = -300
                    playY = -500
                    goX = 600
                    goY = -380
                    score_value = 0

            if event.key == pygame.K_DOWN:
                game_type = "paused"
                enemyY_change = 0
                enemy2Y_change = 0
                enemy3Y_change = 0
                resumeX = 580
                resumeY = 400
                pauseX = 300
                pauseY = 250
                peX = 460
                peY = 250
                pyX = 950
                onX = -400
                onY = -200
                pyY = -1500
            if event.key == pygame.K_LEFT:
                if game_type == "paused":
                    playerX_change = 0
            if event.key == pygame.K_RIGHT:
                if game_type == "paused":
                    playerX_change = 0
            if event.key == pygame.K_SPACE:
                if game_type == "paused":
                    bulletX = 10000
            if game_type == "paused":
                bulletY_change = 0
            if event.key == pygame.K_UP:
                if game_type == "paused":
                    enemyY_change = 8
                    bulletY_change = 40
                    game_type = "on"
                    onX = -400
                    onY = -200
                    bulletX = playerX
                    pyX = 950
                    pyY = 150
                    bulletX += 25
                    peX = 460
                    peY = -2500
                    pauseX = 1215
                    pauseY = 15
                    resumeX = -400
                    resumeY = -200
            if score_value == 0:
                if game_type == "start":
                    if event.key == pygame.K_DOWN:
                        overX = 900
                        overY = -1000
            if event.key == pygame.K_UP:
                if game_type == "on":
                    if event.key == pygame.K_LEFT:
                        playerX_change = -28
                    if event.key == pygame.K_LEFT:
                        playerX_change = 28

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    if playerX <= 20:
        playerX = 20

    if playerX >= 1200:
        playerX = 1200

    if bulletY <= 0:
        bulletY = 610
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    collision = collide(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 610
        bullet_state = "ready"
        enemyY = -300
        enemyX = random.randint(20, 1200)
        score_value += 1

    collision2 = collide2(enemy2X, enemy2Y, bulletX, bulletY)
    if collision2:
        bulletY = 610
        bullet_state = "ready"
        enemy2Y = -450
        enemy2X = random.randint(20, 1200)
        score_value += 1

    collision3 = collide3(enemy3X, enemy3Y, bulletX, bulletY)
    if collision3:
        bulletY = 610
        bullet_state = "ready"
        enemy3Y = -450
        enemy3X = random.randint(20, 1200)
        score_value += 1

    over = game_over(enemyX, enemyY, playerX, playerY)
    if over:
        fire_bullet(-3000, 300)
        pyX = 950
        resumeX = -400
        resumeY = -200
        onX = -400
        onY = -200
        pyY = -1500
        restartX = 610
        restartY = 500
        enemyY = -300
        enemyX = 600
        pauseX = 1215
        pauseY = -1500
        enemyY_change = 0
        enemy2Y = 1500
        enemy2X = 600
        game = "over"
        enemy2Y_change = 0
        overX = 350
        overY = 200
        playerY = -300
        bulletY = 200
        bulletY_change = 0
        playerX = bulletX
        bulletX = -400
        scoreX = 640
        scoreY = 320
        reX = 450
        reY = 700
        peX = -400
        peY = -200

    over2 = game2_over(enemy2X, enemy2Y, playerX, playerY)
    if over2:
        fire_bullet(-3000, 300)
        restartX = 610
        resumeX = -400
        resumeY = -200
        restartY = 500
        onX = -400
        onY = -200
        enemyY = -300
        enemyX = 600
        pyX = 950
        pyY = -1500
        enemyY_change = 0
        enemy2Y = 1500
        enemy2X = 600
        pauseX = 1215
        pauseY = -1500
        enemy2Y_change = 0
        overX = 350
        overY = 200
        playerY = -300
        bulletY = 200
        game = "over"
        bulletY_change = 0
        playerX = bulletX
        bulletX = -400
        scoreX = 640
        scoreY = 320
        reX = 425
        reY = 700
        peX = -400
        peY = -200

    over3 = game3_over(enemy3X, enemy3Y, playerX, playerY)
    if over3:
        fire_bullet(-3000, 300)
        restartX = 610
        onX = -400
        resumeX = -400
        resumeY = -200
        onY = -200
        restartY = 500
        enemyY = -300
        pauseY = -1500
        enemyX = 600
        pyX = 950
        pyY = -1500
        enemyY_change = 0
        enemy2Y = 1500
        enemy2X = 600
        enemy2Y_change = 0
        enemy3Y = 1500
        enemy3X = 600
        enemy3Y_change = 0
        overX = 350
        overY = 200
        playerY = -300
        bulletY = 200
        game = "over"
        bulletY_change = 0
        playerX = bulletX
        bulletX = -400
        scoreX = 640
        scoreY = 320
        reX = 425
        reY = 700
        peX = -400
        peY = -200

    over2 = game_over2()
    if over2:
        fire_bullet(-3000, 300)
        restartX = 610
        resumeX = -400
        resumeY = -200
        restartY = 500
        onX = -400
        onY = -200
        pyX = 950
        pyY = -1500
        enemyY = -300
        enemyX = 600
        overX = 350
        pauseY = -1500
        enemy2Y = 1500
        enemy2X = 300
        enemy2Y_change = 0
        overY = 200
        enemyY_change = 0
        playerY = -300
        bulletY = 200
        game = "over"
        bulletY_change = 0
        playerX = bulletX
        bulletX = -400
        scoreX = 640
        scoreY = 320
        reX = 425
        reY = 700
        peX = -400
        peY = -200

    over4 = game2_over2()
    if over4:
        fire_bullet(-3000, 300)
        restartX = 610
        resumeX = -400
        resumeY = -200
        restartY = 500
        enemyY = -300
        onX = -400
        onY = -200
        game = "over"
        enemyX = 600
        overX = 350
        pauseY = -1500
        overY = 200
        enemyY_change = 0
        enemy2Y = 1500
        pyX = 950
        pyY = -1500
        enemy2X = 600
        enemy2Y_change = 0
        playerY = -300
        bulletY = 200
        bulletY_change = 0
        playerX = bulletX
        bulletX = -400
        scoreX = 640
        scoreY = 320
        reX = 425
        reY = 700
        peX = -400
        peY = -200

    over5 = game3_over3()
    if over4:
        fire_bullet(-3000, 300)
        restartX = 610
        restartY = 500
        resumeX = -400
        resumeY = -200
        onX = -400
        onY = -200
        enemyY = -300
        pauseY = -1500
        game = "over"
        enemyX = 600
        pyX = 950
        pyY = -1500
        overX = 350
        peX = -400
        peY = -200
        overY = 200
        enemyY_change = 0
        enemy2Y = 1500
        enemy2X = 600
        enemy2Y_change = 0
        enemy3Y = 1500
        enemy3X = 600
        enemy3Y_change = 0
        playerY = -300
        bulletY = 200
        bulletY_change = 0
        playerX = bulletX
        bulletX = -400
        scoreX = 640
        scoreY = 320
        reX = 425
        reY = 700

    if score_value >= 18:
        enemy2Y_change = 8
    if score_value >= 18:
        if game_type == "paused":
            enemy2Y_change = 0
    if score_value >= 2:
        enemy3Y_change = 5
    if score_value >= 2:
        if game_type == "paused":
            enemy3Y_change = 0

    if score_value == 0:
        if game_type == "start":
            fire_bullet(-3000, 300)
            enemyY = -300
            onX = 450
            onY = 700
            game = "new"
            enemyX = 600
            overX = 350
            overY = -2000
            enemyY_change = 0
            peX = -400
            resumeX = -400
            resumeY = -200
            peY = -200
            enemy2Y = 1500
            enemy2X = 600
            enemy2Y_change = 0
            enemy3Y = 1500
            enemy3X = 600
            enemy3Y_change = 0
            startX = 90
            startY = 15
            playerY = -3000
            bulletY = 200
            bulletY_change = 0
            playerX = -900
            bulletX = -400
            pyX = -400
            pyY = -200
            scoreX = 640
            scoreY = -320
            restartX = 400
            restartY = -800
            playX = 500
            playY = 485
            reX = 425
            reY = -700
            goX = 600
            goY = 450

    if score_value == 25:
        bonusX = 150
        bonusY = 10
        score_value += 2
        bonus_value = 2
    elif score_value == 30:
        bonusY = -1000
    else:
        bonusY = -1000

    if score_value == 40:
        bonusX = 150
        bonusY = 10
        score_value += 3
        bonus_value = 3
    elif score_value == 45:
        bonusY = -1000
    else:
        bonusY = -1000

    if score_value == 50:
        bonusX = 150
        bonusY = 10
        score_value += 5
        bonus_value = 5
    elif score_value == 57:
        bonusY = -1000
    else:
        bonusY = -1000

    if score_value == 75:
        bonusX = 150
        bonusY = 10
        score_value += 7
        bonus_value = 7
    elif score_value == 84:
        bonusY = -1000
    else:
        bonusY = -1000

    if score_value == 100:
        bonusX = 150
        bonusY = 10
        score_value += 10
        bonus_value = 10
    elif score_value == 112:
        bonusY = -1000
    else:
        bonusY = -1000

    if score_value == 150:
        bonusX = 150
        bonusY = 10
        score_value += 15
        bonus_value = 15
    elif score_value == 168:
        bonusY = -1000
    else:
        bonusY = -1000

    playerX += playerX_change
    enemyY += enemyY_change
    enemy2Y += enemy2Y_change
    enemy3Y += enemy3Y_change

    player()
    enemy()
    enemy2()
    enemy3()
    game_start(startX, startY)
    play_game()
    res(restartX, restartY)
    bonos(bonusX, bonusY)
    paused(pyX, pyY)
    pause(pauseX, pauseY)
    overs(overX, overY)
    score(scoreX, scoreY)
    retry(reX, reY)
    game_on(onX, onY)
    game_pause(peX, peY)
    game_resume(resumeX, resumeY)
    going(goX, goY)
    pygame.display.update()
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random

timer = 0
timer2 = 0
aux = 0
cronm_doubleshot = 0
temp_doubleshot = 0

vel_enemy = 200

lifes = 2
score = 0
duracao = 0

verifica = False


def game(fator_dificuldade):
    global timer, timer2, aux, cronm_doubleshot, temp_doubleshot, vel_enemy, lifes, score, verifica

    def controlarNave():
        global timer, timer2, aux, cronm_doubleshot, temp_doubleshot, verifica
        if (teclado.key_pressed('RIGHT') or teclado.key_pressed('D')) and (ship.x + ship.width) < janela_game.width:
            ship.x = ship.x + vel_ship * janela_game.delta_time()

        if (teclado.key_pressed('LEFT') or teclado.key_pressed('A')) and ship.x > 0:
            ship.x = ship.x - vel_ship * janela_game.delta_time()

        if teclado.key_pressed('SPACE'):
            if temp_doubleshot == 0:
                if timer > 0.4:
                    laser = Sprite('lasershot_red.png', 1)
                    laser.y = ship.y - 35
                    laser.x = ship.x + (ship.width/2) - 10
                    all_shots.append(laser)
                    timer = 0
            temp_doubleshot += janela_game.delta_time()

            if temp_doubleshot > 2:
                if cronm_doubleshot >= 10:
                    if timer > 0.2:
                        verifica = True
                        laser1 = Sprite('lasershot_purple.png', 1)
                        laser2 = Sprite('lasershot_purple.png', 1)
                        laser1.y = ship.y - 35
                        laser1.x = ship.x
                        laser2.y = ship.y - 35
                        laser2.x = ship.x + ship.width
                        all_double_shots.append(laser1)
                        all_double_shots.append(laser2)
                        timer = 0
                        if cronm_doubleshot > 11.5:
                            verifica = False
                            cronm_doubleshot = 0
                            temp_doubleshot = 0

        if not teclado.key_pressed('SPACE'):
            temp_doubleshot = 0

        for shot in all_shots:
            shot.y = shot.y - vel_laser * janela_game.delta_time()
            shot.draw()
            if shot.y < 0:
                all_shots.remove(shot)

        for shot in all_double_shots:
            shot.y = shot.y - vel_laser * janela_game.delta_time()
            shot.draw()
            if shot.y < 0:
                all_double_shots.remove(shot)

    def desenharInimigos():
        global vel_enemy, lifes
        hit = 0
        for i in range(len(all_enemies)):
            if all_enemies[i][-1].x + all_enemies[i][-1].width > janela_game.width and hit == 0:
                hit = 1
                vel_enemy *= -1
            if all_enemies[i][0].x < 0 and hit == 0:
                hit = 2
                vel_enemy *= -1

        for i in range(len(all_enemies)):
            for enemy in all_enemies[i]:
                if hit == 1:
                    enemy.x -= 5
                    enemy.y += 20
                if hit == 2:
                    enemy.x += 5
                    enemy.y += 20
                if random.randint(0, (100//fator_dificuldade) * quant_inimigos[0]) == 5:
                    shot_enemy = Sprite('lasershot_green.png', 1)
                    shot_enemy.x = enemy.x
                    shot_enemy.y = enemy.y
                    all_enemy_shots.append(shot_enemy)

                enemy.move_x(vel_enemy * janela_game.delta_time())
                if enemy.y + enemy.height > ship.y:  # Gameover
                    return True
                enemy.draw()

        for shot in all_enemy_shots:
            shot.y = shot.y + 1.2 * (vel_laser + 15*fator_dificuldade) * janela_game.delta_time()
            shot.draw()
            if shot.collided(ship) and not invencible[0]:
                if lifes > 0:
                    lifes -= 1
                    invencible[0] = True
                    ship.x = janela_game.width / 2 - ship.width / 2
                    ship.y = janela_game.height / 1.05 - ship.height / 1.05
                else:
                    return True
            if shot.y > janela_game.height:
                all_enemy_shots.remove(shot)

        return False

    def detectarColisao():
        global score
        for fileira in all_enemies:
            for enemy in fileira:
                if len(all_shots) > 0:
                    for shot in all_shots:
                        if shot.collided(enemy):
                            all_shots.remove(shot)
                            fileira.remove(enemy)
                            quant_inimigos[0] -= 1
                            score += 250
                if len(all_double_shots) > 0:
                    for shot in all_double_shots:
                        if shot.collided(enemy):
                            all_double_shots.remove(shot)
                            fileira.remove(enemy)
                            quant_inimigos[0] -= 1
                            score += 100
            if len(fileira) == 0:
                all_enemies.remove(fileira)
        if len(all_enemies) == 0:
            return True
        return False

    janela_game = Window(1024, 768)
    janela_game.set_title('SpaceInvaders - Luiz Willner')
    teclado = Window.get_keyboard()
    mouse = Window.get_mouse()

    if fator_dificuldade == 1:
        dificuldade = 'EASY'
    elif fator_dificuldade == 2:
        dificuldade = 'MEDIUM'
    else:
        dificuldade = 'HARD'

    background = GameImage('sw_background.jpg')
    img_gameover = GameImage('empirepixel.png')
    img_gameover.x = janela_game.width / 4
    img_gameover.y = janela_game.height / 8
    img_victory = GameImage('rebellionpixel.png')
    img_victory.x = janela_game.width / 4
    img_victory.y = janela_game.height / 8

    ship = Sprite('xwing2.png', 1)
    ship.x = janela_game.width/2 - ship.width/2
    ship.y = janela_game.height/1.05 - ship.height/1.05
    vel_ship = 400

    vel_laser = 400
    all_shots = []
    all_double_shots = []
    all_enemy_shots = []

    piscar_cronom = 0
    piscar_ritmo = 0

    timer = 0
    timer2 = 0
    aux = 0
    cronm_doubleshot = 0
    temp_doubleshot = 0

    vel_enemy = 200

    lifes = 2
    score = 0
    duracao = 0

    all_enemies = []
    quant_fileiras = 5
    inimigos_por_fileira = 8
    quant_inimigos = [quant_fileiras * inimigos_por_fileira]

    life_symbol = GameImage('r2d2pixel.png')
    life_symbol.x = janela_game.width / 32
    life_symbol.y = janela_game.height / 64
    invencible = [False]
    gameover = False
    victory = False
    on = True

    # Montando matriz de inimigos
    for index_linha in range(quant_fileiras):
        enemies_list = []
        for index_coluna in range(inimigos_por_fileira):
            enemy = Sprite('tiefighter2.png', 1)
            enemy.set_position(80 * index_coluna, 80 * index_linha)
            enemies_list.append(enemy)
        all_enemies.append(enemies_list)
    janela_game.update()
    janela_game.update()

    # Game Loop
    while on:
        aux += janela_game.delta_time()
        if cronm_doubleshot >= 10 and not verifica:
            cronm_doubleshot = 10
        else:
            cronm_doubleshot += janela_game.delta_time()
        print(aux)

        if gameover or victory:
            on = False

        background.draw()
        controlarNave()

        if not invencible[0]:
            ship.draw()
        else:
            piscar_cronom += janela_game.delta_time()
            if piscar_cronom <= 2:
                piscar_ritmo += janela_game.delta_time()
                if piscar_ritmo <= 0.3:
                    ship.draw()
                elif piscar_ritmo >= 0.6:
                    piscar_ritmo = 0
            else:
                piscar_cronom = 0
                piscar_ritmo = 0
                invencible[0] = False

        if aux > 0.1:
            gameover = desenharInimigos()
            victory = detectarColisao()
            janela_game.draw_text(f"SCORE: {score}", janela_game.width / 1.2, (janela_game.height - 300) / 16, size=24, color=(255, 215, 0), font_name='pixel-art')
            janela_game.draw_text(f"x{lifes}", (janela_game.width / 32) + 40, (janela_game.height / 64) + 10, size=32, color=(0, 50, 215), font_name='pixel-art')
            if cronm_doubleshot < 10:
                janela_game.draw_text(f"DoubleShot {cronm_doubleshot * 10:.0f}%", (janela_game.width / 32) + 80, (janela_game.height / 64) + 10, size=32, color=(0, 50, 215), font_name='pixel-art')
            else:
                janela_game.draw_text(f"DoubleShot 100%", (janela_game.width / 32) + 80, (janela_game.height / 64) + 10, size=40, color=(0, 200, 0), font_name='pixel-art')
            life_symbol.draw()
            timer += janela_game.delta_time()

            if teclado.key_pressed('ESC'):
                aux = 0
                return

        janela_game.update()

    duracao = aux
    aux = 0
    while gameover:
        img_gameover.draw()
        # aux[0] = 0
        if teclado.key_pressed('P'):
            return
        janela_game.update()

    while victory:
        img_victory.draw()
        score_total = score * (10/duracao) * (lifes + 1) * fator_dificuldade
        janela_game.draw_text(f'DIFFICULTY:  {dificuldade}', janela_game.width / 3, janela_game.height / 1.2, size=20, color=(255, 215, 0), bold=True)
        janela_game.draw_text(f'RAW SCORE:  {score}', janela_game.width / 3, janela_game.height/1.2 + 20, size=20, color=(255, 215, 0), bold=True)
        janela_game.draw_text(f'DURATION:  {duracao:.2f}', janela_game.width / 3, janela_game.height / 1.2 + 40, size=20, color=(255, 215, 0), bold=True)
        janela_game.draw_text(f'REMAINING LIVES:  {lifes}', janela_game.width / 3, janela_game.height / 1.2 + 60, size=20, color=(255, 215, 0), bold=True)
        janela_game.draw_text(f'FINAL SCORE:  {score_total:.2f}', janela_game.width / 3, janela_game.height / 1.2 + 80, size=20, color=(255, 215, 0), bold=True)
        # aux[0] = 0
        if teclado.key_pressed('P'):
            return
        janela_game.update()

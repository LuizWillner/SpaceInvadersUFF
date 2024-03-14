from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.sound import *
from space_invaders import space_invaders_game


def selectDifficulty(background_difficulty_menu):
    # Janela do menu das dificuldades
    janela_difficulty = Window(1024, 768)
    janela_difficulty.set_title('SpaceInvaders - Difficulties - Luiz Willner')

    # Botões de dificuldade
    easy_button = GameImage('select_difficulty_easy.png')
    medium_button = GameImage('select_difficulty_medium.png')
    hard_button = GameImage('select_difficulty_hard.png')

    # Posição dos Botões
    easy_button.x = janela_difficulty.width / 4 - easy_button.width / 4
    easy_button.y = janela_difficulty.height / 2.5 - easy_button.height / 2
    medium_button.x = janela_difficulty. width / 4 - medium_button.width / 4
    medium_button.y = janela_difficulty.height / 2 - medium_button.height / 2
    hard_button.x = janela_difficulty.width / 4 - hard_button.width / 4
    hard_button.y = janela_difficulty.height / 1.65 - hard_button.height / 2

    while True:
        background_difficulty_menu.draw()
        easy_button.draw()
        medium_button.draw()
        hard_button.draw()
        if mouse.is_over_object(easy_button):
            if mouse.is_button_pressed(1):
                dificuldade[0] = 1
                break
        if mouse.is_over_object(medium_button):
            if mouse.is_button_pressed(1):
                dificuldade[0] = 2
                break
        if mouse.is_over_object(hard_button):
            if mouse.is_button_pressed(1):
                dificuldade[0] = 4
                break
        janela_difficulty.update()


def MenuButtons(background):
    if mouse.is_over_object(difficulty_button):
        if mouse.is_button_pressed(1):
            selectDifficulty(background)
            return

    if mouse.is_over_object(play_button):
        if mouse.is_button_pressed(1):
            space_invaders_game.game(dificuldade[0])

    if mouse.is_over_object(exit_button):
        if mouse.is_button_pressed(1):
            janela.close()


# Inicialização
janela = Window(1024, 768)
janela.set_title('SpaceInvaders - Menu - Luiz Willner')
teclado = Window.get_keyboard()
mouse = Window.get_mouse()

aux = 0

background = GameImage('sw_background.jpg')
play_button = GameImage('play.png')
ranking_button = GameImage('ranking.png')
difficulty_button = GameImage('difficulty.png')
exit_button = GameImage('exit.png')
title = GameImage('spaceinvaders_title.png')

play_button.x = janela.width/2 - play_button.width/2
play_button.y = janela.height/2 - play_button.height/2
difficulty_button.x = janela.width/2 - difficulty_button.width/2
difficulty_button.y = janela.height/1.7 - difficulty_button.height/2
ranking_button.x = janela.width/2 - difficulty_button.width/2
ranking_button.y = janela.height/1.48 - difficulty_button.height/2
exit_button.x = janela.width/2 - exit_button.width/2
exit_button.y = janela.height/1.31 - exit_button.height/2
title.x = janela.width/2 - title.width/2
title.y = janela.height/3.5 - title.height/2

dificuldade = [2]

# Game Loop
while True:
    # Interface
    background.draw()
    title.draw()
    play_button.draw()
    ranking_button.draw()
    difficulty_button.draw()
    exit_button.draw()

    # Mouse (butões funfando)
    MenuButtons(background)

    janela.update()

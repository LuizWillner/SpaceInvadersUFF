from PPlay.window import *
from PPlay.sprite import *


# funcao para desenhar inimigos na tela e comportamento deles
def colocarInimigos():
    verificar = 0
    for index in range(len(todos_inimigos)):
        if todos_inimigos[index][-1].x > janela.width - todos_inimigos[index][-1].width and verificar == 0:
            verificar = 1
            velocidade_inimigo[0] *= -1
        if todos_inimigos[index][0].x < 0 and verificar == 0:
            verificar = 2
            velocidade_inimigo[0] *= -1
    for index in range(len(todos_inimigos)):
        for inimigos in todos_inimigos[index]:
            if verificar == 1:
                inimigos.y += 30
                inimigos.x -= 10
            if verificar == 2:
                inimigos.x += 10
                inimigos.y += 30
            inimigos.move_x(velocidade_inimigo[0] * janela.delta_time())
            if inimigos.y > nave.y - inimigos.height:
                return 1
            inimigos.draw()
    return 0


# funcao dos controles do player
def controlesDoJogador():
    if (teclado.key_pressed('D')) or (teclado.key_pressed('RIGHT')) and (nave.x < janela.width - nave.width):
        nave.x = nave.x + janela.delta_time() * velocidade_nave
    if (teclado.key_pressed('LEFT') or teclado.key_pressed('A')) and nave.x > 0:
        nave.x = nave.x - velocidade_nave * janela.delta_time()
    if cronometro[0] > 0.4:
        if teclado.key_pressed('SPACE'):
            laser = Sprite('lasershot.png', 1)
            laser.x = nave.x + 15
            laser.y = nave.y - 35
            todos_tiros.append(laser)
            cronometro[0] = 0
    for tiro in todos_tiros:
        tiro.y = tiro.y - velocidade_tiro * janela.delta_time()
        tiro.draw()
        if tiro.y < 0:
            todos_tiros.remove(tiro)


# funcao da colisao
def colisao():
    for fileira in todos_inimigos:
        for inimigo in fileira:
            if len(todos_tiros) > 0:
                for tiro in todos_tiros:
                    if tiro.collided(inimigo):
                        todos_tiros.remove(tiro)
                        fileira.remove(inimigo)
                        pontuacao[0] += 1
        if len(fileira) == 0:
            todos_inimigos.remove(fileira)
    if len(todos_inimigos) == 0:
        return 1
    return 0


# janela e teclado
janela = Window(1024, 800)
janela.set_title('Space Invaders (Eduardo Motta)')
teclado = Window.get_keyboard()

# Booleanas
perdeu = 0
ganhou = 0
ligado = 1

# Sprites e imagens
img_de_fundo = Sprite('background.jpg', 1)
img_perdeu = Sprite('perdeu.png', 1)
img_ganhou = Sprite('vitoria.png', 1)
nave = Sprite('nave.png', 1)

# Posições
nave.x = janela.width/2 - nave.width/2
img_perdeu.x = janela.width/4
img_ganhou.x = janela.width/4
nave.y = janela.height / 1.1 - nave.height / 1.1
img_perdeu.y = janela.height/8
img_ganhou.y = janela.height/8

# Velocidades
velocidade_nave = 500
velocidade_tiro = 300

# Listas
todos_inimigos = []
velocidade_inimigo = [350]
todos_tiros = []
cronometro = [0]
pontuacao = [0]

# Criando lista inimigos
for i in range(6):
    lista_inimigos = []
    for j in range(6):
        nave_inimiga = Sprite('inimigo.png', 1)
        nave_inimiga.set_position(90 * j, 90 * i)
        lista_inimigos.append(nave_inimiga)
    todos_inimigos.append(lista_inimigos)

# game loop
while ligado == 1:
    if ganhou or perdeu:
        ligado = 0
    else:
        img_de_fundo.draw()
        nave.draw()
        controlesDoJogador()
        perdeu = colocarInimigos()
        ganhou = colisao()
        janela.draw_text(f"{pontuacao[0]} pts", janela.width / 16, (janela.height - 300) / 16, size=32, color=(0, 215, 0))
        cronometro[0] += janela.delta_time()

        if teclado.key_pressed('ESC'):
            break
        janela.update()

# tela do venceu
while ganhou == 1:
    if teclado.key_pressed('ESC'):
        break
    img_ganhou.draw()
    janela.update()

# tela do perdeu
while perdeu == 1:
    if teclado.key_pressed('ESC'):
        break
    img_perdeu.draw()
    janela.update()

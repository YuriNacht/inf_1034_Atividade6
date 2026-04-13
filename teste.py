from pygame import *
init()

window = display.set_mode((1280, 720))

# Inicializar cores do background
bg_color = [151, 209, 250]  # Azul claro inicial (R, G, B)
bg_target = [255, 165, 0]   # Vermelho fim de tarde (R, G, B)
color_change_speed = 0.01    # Velocidade de transição

# Nuvem andando
nuvem_x = 800
velocidade = 0.5

running = True

while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False

    # Gradiente de transição do background
    for i in range(3):  # Para R, G e B
        if bg_color[i] < bg_target[i]:
            bg_color[i] += color_change_speed
        elif bg_color[i] > bg_target[i]:
            bg_color[i] -= color_change_speed

    # Atualizar o fundo com a nova cor
    window.fill((int(bg_color[0]), int(bg_color[1]), int(bg_color[2])))


    # Nuvem andando
    nuvem_x += velocidade
    if nuvem_x > 1280:
        nuvem_x = -200

    # Desenho
    draw.rect(window, (72, 157, 37), (0, 500, 1280, 220))  # Chão
    draw.rect(window, (255, 255, 255), (425, 300, 350, 200))  # Casa
    draw.circle(window, (255, 255, 0), (175, 175), 100, 0)  # Sol
    draw.rect(window, (210, 105, 30), (500, 375, 75, 125))  # Porta
    draw.polygon(window, (0, 0, 0), ((425, 300), (600, 150), (775, 300)))  # Teto
    draw.circle(window, (0, 0, 0), (560, 435), 7, 0)  # Maçaneta
    draw.rect(window, (128, 128, 128), (650, 350, 75, 75))  # Janela
    draw.rect(window, (100, 50, 0), (975, 350, 50, 150))  # Árvore
    draw.circle(window, (34, 139, 34), (1000, 350), 75, 0)  # Folhas da árvore

    # Linhas do sol
    draw.line(window, (255, 255, 0), (175, 175), (175, 25), 2)  # Cima
    draw.line(window, (255, 255, 0), (175, 175), (175, 325), 2)  # Baixo
    draw.line(window, (255, 255, 0), (175, 175), (25, 175), 2)  # Esquerda
    draw.line(window, (255, 255, 0), (175, 175), (325, 175), 2)  # Direita
    draw.line(window, (255, 255, 0), (175, 175), (75, 75), 2)  # Diagonal superior esquerda
    draw.line(window, (255, 255, 0), (175, 175), (275, 75), 2)  # Diagonal superior direita
    draw.line(window, (255, 255, 0), (175, 175), (75, 275), 2)  # Diagonal inferior esquerda
    draw.line(window, (255, 255, 0), (175, 175), (275, 275), 2)  # Diagonal inferior direita

    # Nuvem
    draw.circle(window, (255, 255, 255), (nuvem_x, 100), 50)
    draw.circle(window, (255, 255, 255), (nuvem_x + 65, 100), 50)
    draw.circle(window, (255, 255, 255), (nuvem_x + 130, 100), 50)
    draw.circle(window, (255, 255, 255), (nuvem_x + 195, 100), 50)

    display.update()
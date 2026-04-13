
from pygame import *
init()

window = display.set_mode((1280,720))

window.fill("light blue")

#imagens
anjo_png = image.load("anjo.png")
anjo_png = transform.scale(anjo_png,(250,250))

#texto
anjo_font = font.Font("gwenchana.ttf", 30)
anjo_text = anjo_font.render("OHHHHHHHHHHH", True, (0,0,0))

#musica
mixer_music.load("manha.mp3")
mixer_music.play(-1)
music = mixer.Sound("manha.mp3")
music.set_volume(0.1)



#nuvem andando
nuvem_x = 800
velocidade = 0.5

running = True

while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False






 #nuvem andando
    window.fill((151, 209, 250))
    nuvem_x += velocidade
    if nuvem_x > 1280:
        nuvem_x = -200



    #desenho

#chao
    draw.rect(window,(72, 157 , 37), (0 , 500, 1280, 220))
#casa
    draw.rect(window, (255, 255 , 255),(425, 300, 350, 200))
#sol
    draw.circle(window,(255, 255, 0), (175, 175),100,0)
#porta
    draw.rect(window,(210, 105, 30),(500, 375, 75, 125))
#teto
    draw.polygon(window,(0 , 0 , 0 ),((425, 300),(600, 150),(775, 300)))
#macaneta
    draw.circle(window,(0, 0 , 0),(560, 435), 7, 0)
#janela
    draw.rect(window, (128, 128, 128),(650, 350, 75 , 75))

#arvore
    draw.rect(window,(100, 50 , 0),(975,350, 50, 150))
    draw.circle(window,(34, 139, 34),(1000,350),75,0)
#linhasdosol
    draw.line(window, (255, 255, 0), (175, 175), (175, 25), 2)   # Cima
    draw.line(window, (255, 255, 0), (175, 175), (175, 325), 2)  # Baixo
    draw.line(window, (255, 255, 0), (175, 175), (25, 175), 2)   # Esquerda
    draw.line(window, (255, 255, 0), (175, 175), (325, 175), 2)  # Direita
    draw.line(window, (255, 255, 0), (175, 175), (75, 75), 2)    # Diagonal superior esquerda
    draw.line(window, (255, 255, 0), (175, 175), (275, 75), 2)   # Diagonal superior direita
    draw.line(window, (255, 255, 0), (175, 175), (75, 275), 2)   # Diagonal inferior esquerda
    draw.line(window, (255, 255, 0), (175, 175), (275, 275), 2)  # Diagonal inferior direita
#nuvem
    draw.circle(window,(255, 255, 255), (nuvem_x, 100), 50)
    draw.circle(window,(255, 255, 255), (nuvem_x + 65, 100), 50)
    draw.circle(window,(255, 255, 255), (nuvem_x + 130, 100), 50)
    draw.circle(window,(255, 255, 255), (nuvem_x + 195, 100), 50)

 #desenhar imagem:
    window.blit(anjo_png,(940,-25))
   
    
    #desenhar texto:
    window.blit(anjo_text,(940, 210))

    #colocar som:
    music.play()




    display.update()

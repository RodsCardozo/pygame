import pygame

# cria a tela a ser mostrada set_mode((tamanho))

display = pygame.display.set_mode((1280, 720))
# cria um retangulo no começo da tela
player1 = pygame.Rect(0,0,30,150)
player1_speed = 1


# cria um retanculo no final da tela
player2 = pygame.Rect(1250,590,30,150)
# cria uma bola na tela
ball = pygame.Rect(600,350, 15,15)

# mantém a janela do jogo aberto
loop = True
while loop:
    # cria os eventos que vao mudar o jogo
    for event in pygame.event.get():

        # QUIT é o botão fecha
        if event.type == pygame.QUIT:
            loop = False

        # evento de clicar uma tecla qualquer
        if event.type == pygame.KEYDOWN:
            # clica na tecla a
            if event.key == pygame.K_w:
                player1_speed = -1

            elif event.key == pygame.K_s:
                player1_speed = 1
    if player1.y <= 0:
        player1.y = 0
    elif player1.y >= 590:
        player1.y = 590
    player1.y += player1_speed*2

    display.fill('black') # preenche a tela com a cor escolhida

    # mostra na tela os retangulos criados anteriormente
    pygame.draw.rect(display, "white", player1)
    pygame.draw.rect(display, "white", player2)
    pygame.draw.circle(display, "white", ball.center, 8)
    # mantém a tela aberta
    pygame.display.flip()

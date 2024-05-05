#Import de biblioteca
import pygame 
import random

#Iniciar pygame
pygame.init()

#Nome do título da janela 
pygame.display.set_caption('Snake Game')

# Tamanho da tela
largura, altura = 1200, 600

# Passando a largura e altura para dentro do pygame display
tela = pygame.display.set_mode((largura, altura))

# Relogio que controla o tempo da velocidade da cobrinha
relogio = pygame.time.Clock()

# Cores do Jogo --- RGB
background = (0, 0, 0) # ===> Cor do background
cobrinha = (22, 227, 30) # ===> Cor da cobrinha
pontos_text = (132, 234, 22) # ===> Cor da pontuação
comida = (255, 0, 0) # ===> Cor da comida

# Tamanho do Quadrado (Cobra/Comida)
tamanho_quadrado = 20

# Velocidade que a cobrinha anda
velocidade_atual = 15 # ===> Quanto menor é mais lento// Quanto maior é mais rápido (Quanto a cobra anda a cada execução)

# Criando uma função para gerar a comida
def food():
    # Gerando a comida na posição x aleatória e deixando ela centralizado em um pixel/quadrado
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)

    # Gerando a comida na posição y aleatória e deixando ela centralizado em um pixel/quadrado
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)

    # Retorna o valor própria
    return comida_x, comida_y

# Criando uma função para desenhar comida (Fazer o quadradinho que representa a comida)
def desenhar_food(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, comida, [comida_x,comida_y, tamanho, tamanho ])

# Criando uma função para desenhar a cobra(Fazer o quadradinho que representa a cobra)
def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, cobrinha, [pixel[0], pixel[1], tamanho, tamanho])

# Função para criar os pontos
def desenhar_pontuação(pontuacao):
    # Fonte do texto da pontuação
    fonte = pygame.font.SysFont('Courier New, monospace', 35)
    texto = fonte.render(f'Pontos: {pontuacao}', True, pontos_text)
    # Posição em que o texto irá ficar
    tela.blit(texto, [1, 1])

# Função para alterar a direção que a cobrinha anda 
def selecionar_velocidade(tecla):
    # Se o usuário clicar a seta para baixo:
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado

    # Se o usuário clicar a seta para cima:
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado

    # Se o usuário clicar a seta para direita:
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0

    # Se o usuário clicar a seta para esquerda:
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0

    return velocidade_x, velocidade_y

# Criando a função para o jogo
def game_play():
    # Declarando o gameover como Falso
    gameover = False

    # Posição inicial que a cobrinha começa
    x = largura / 2
    y = altura / 2

    # Quantos pixels ela ta andando pra ambas direções por isso começa parada até ir adcionando a cada execução do usuario
    velocidade_x = 0
    velocidade_y = 0

    # Ela começa com apenas 1 e vai aumentando e entrando na lista de pixels
    tamanho_cobrinha = 1
    # A cada passo que ela der é adcionado um novo quadradinho aqui
    pixels = []

    # Chamando a função para criar a comida:
    comida_x, comida_y = food()

# Loop do Game
    # Enquanto não for gameover:
    while not gameover:

        # Colocando o background do jogo
        tela.fill(background)

        # Ação do Usuário
        for evento in pygame.event.get():
            # Evento de fechar a janela
            if evento.type == pygame.QUIT:
                # Interrompendo o looping infinito
                gameover = True 

            # Se o evento for uma tecla pressionada    
            elif evento.type == pygame.KEYDOWN:
                # Chama a função selecionar_velocidade para determinar a direção baseada na tecla pressionada
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        # Chamando a função para desenhar a comida no nosso jogo
        desenhar_food(tamanho_quadrado,comida_x, comida_y)

        # Movimento da cobrinha
        if x < 0 or x >= largura or y <0 or y >= altura:
            gameover = True
        x += velocidade_x
        y += velocidade_y

        # Desenhando a cobrinha
        # A cada vez que o usuario apertar uma tecla ela vai apagar o quadradinho antigo.
        pixels.append([x,y])
        if len(pixels) > tamanho_cobrinha:
            del pixels[0]

        # Se a cobrinha bateu no proprio corpo o jogo se encerra
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                gameover = True

        # Chamando a função de desenhar a cobra e passando os parâmetros dela
        desenhar_cobra(tamanho_quadrado, pixels)

        # Chamando a função de desenhar a pontuação e passando os parâmetros dela
        desenhar_pontuação(tamanho_cobrinha-1)

        # Atualizando a tela
        pygame.display.update()

        # Criando uma nova comida em um lugar aleatório do mapa pela função food()
        if x == comida_x and y == comida_y:
            tamanho_cobrinha += 1
            comida_x, comida_y = food()

        # Velocidade que a cobrinha anda
        relogio.tick(velocidade_atual)
        
# Chamando a função de iniciar o jogo
game_play()



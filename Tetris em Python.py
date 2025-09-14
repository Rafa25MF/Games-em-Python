import pygame
import random
import time
import os


# Configurações da tela
TAMANHO_BLOCO = 30
GRID_LARGURA = 10
GRID_ALTURA = 20
JANELA_LARGURA = GRID_LARGURA * TAMANHO_BLOCO + 300  # espaço extra para o HUD
JANELA_ALTURA = GRID_ALTURA * TAMANHO_BLOCO

# Inicialização
pygame.init()
tela = pygame.display.set_mode((JANELA_LARGURA, JANELA_ALTURA))
pygame.display.set_caption("Tetris Clássico com HUD")
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("monospace", 20)

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
CINZA = (50, 50, 50)
AZUL = (0, 0, 255)

# Formas
formas = [
    [[1, 1, 1, 1, 1]],             # I
    [[1, 1, 1, 1]],                # w
    [[1, 1, 1]],                   # G
    [[1, 1], [1, 1]],              # O
    [[1, 1, 1], [1, 1, 1]],        # R
    #[[1, 1, 1]], [[1, 1, 1]], [[1, 1, 1]], # D
    [[0, 1, 0], [1, 1, 1]],        # T
    [{1, 1, 1}, {1}],               # Y
    [[1, 1, 0], [0, 1, 1]],        # S
    [[0, 1, 1], [1, 1, 0]],        # Z
    [[1, 0, 0], [1, 1, 1]],        # L
    [[0, 0, 1], [1, 1, 1]],        # J
    [[0, 1], [1, 1,]],
    [{1}]
]

def nova_peca():
    return {"forma": random.choice(formas), "x": GRID_LARGURA // 2 - 2, "y": 0}

def desenhar_bloco(matriz, x_offset=0, y_offset=0):
    for y, linha in enumerate(matriz):
        for x, val in enumerate(linha):
            if val:
                pygame.draw.rect(
                    tela, VERDE,
                    ((x + x_offset) * TAMANHO_BLOCO, (y + y_offset) * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO),
                    2
                )

def colide(tab, forma, x, y):
    for i, linha in enumerate(forma):
        for j, val in enumerate(linha):
            if val:
                if x + j < 0 or x + j >= GRID_LARGURA or y + i >= GRID_ALTURA:
                    return True
                if y + i >= 0 and tab[y + i][x + j]:
                    return True
    return False

def fixar(tab, forma, x, y):
    for i, linha in enumerate(forma):
        for j, val in enumerate(linha):
            if val and 0 <= y + i < GRID_ALTURA:
                tab[y + i][x + j] = 1

def limpar_linhas(tab):
    novas = [linha for linha in tab if not all(linha)]
    removidas = GRID_ALTURA - len(novas)
    for _ in range(removidas):
        novas.insert(0, [0] * GRID_LARGURA)
    return novas, removidas

def rotacionar(forma):
    return [list(r) for r in zip(*forma[::-1])]

def novo_tabuleiro():
    return [[0] * GRID_LARGURA for _ in range(GRID_ALTURA)]

def desenhar_interface(pontos, nivel, tempo, velocidade):
    hud_x = GRID_LARGURA * TAMANHO_BLOCO + 20
    tela.blit(fonte.render(f"Pontuação: {pontos}", True, VERDE), (hud_x, 30))
    tela.blit(fonte.render(f"Nível: {nivel}", True, VERDE), (hud_x, 60))
    tela.blit(fonte.render(f"Tempo: {int(tempo)}s", True, VERDE), (hud_x, 90))
    tela.blit(fonte.render(f"Velocidade: {velocidade}", True, VERDE), (hud_x, 120))

def carregar_recorde():
    if os.path.exists("recorde.txt"):
        with open("recorde.txt", "r") as f:
            try:
                return int(f.read())
            except ValueError:
                return 0
    return 0

def salvar_recorde(pontuacao):
    recorde_atual = carregar_recorde()
    if pontuacao > recorde_atual:
        with open("recorde.txt", "w") as f:
            f.write(str(pontuacao))

def desenhar_interface(pontos, nivel, tempo, velocidade, recorde):
    hud_x = GRID_LARGURA * TAMANHO_BLOCO + 20
    tela.blit(fonte.render(f"Pontuação: {pontos}", True, VERDE), (hud_x, 30))
    tela.blit(fonte.render(f"Recorde: {recorde}", True, VERDE), (hud_x, 60))
    tela.blit(fonte.render(f"Nível: {nivel}", True, VERDE), (hud_x, 90))
    tela.blit(fonte.render(f"Tempo: {int(tempo)}s", True, VERDE), (hud_x, 120))
    tela.blit(fonte.render(f"Velocidade: {velocidade}", True, VERDE), (hud_x, 150))


def jogar():
    tab = novo_tabuleiro()
    peca = nova_peca()
    
    # Ajuste de velocidade e nível
    pontos = 0
    nivel = 1
    queda_vel = 30  # Intervalo de tempo entre quedas das peças
    queda_contador = 0
    tempo_inicio = time.time()
    recorde = carregar_recorde()

    rodando = True
    while rodando:
        relogio.tick(60)
        tela.fill(PRETO)

        # Desenhar moldura do jogo
        pygame.draw.rect(tela, CINZA, (0, 0, GRID_LARGURA * TAMANHO_BLOCO, JANELA_ALTURA), 2)
        pygame.draw.rect(tela, VERDE, (0, 0, GRID_LARGURA * TAMANHO_BLOCO, JANELA_ALTURA), 5)

        # Tempo atual
        tempo_decorrido = time.time() - tempo_inicio

        # Atualizar nível e velocidade conforme a pontuação
        nivel = 1 + pontos // 500  # A cada 500 pontos, o nível aumenta
        queda_vel = max(5, 30 - nivel * 2)  # A velocidade de queda vai diminuindo (a peça cai mais rápido)

        # Queda automática
        queda_contador += 1
        if queda_contador >= queda_vel:
            if not colide(tab, peca["forma"], peca["x"], peca["y"] + 1):
                peca["y"] += 1
            else:
                fixar(tab, peca["forma"], peca["x"], peca["y"])
                tab, linhas = limpar_linhas(tab)
                pontos += linhas * 100  # Pontuação baseada no número de linhas apagadas
                peca = nova_peca()
                if colide(tab, peca["forma"], peca["x"], peca["y"]):
                    salvar_recorde(pontos)
                    jogar()
                    return
            queda_contador = 0

        # Controles
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salvar_recorde(pontos)
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and not colide(tab, peca["forma"], peca["x"] - 1, peca["y"]):
                    peca["x"] -= 1
                elif evento.key == pygame.K_RIGHT and not colide(tab, peca["forma"], peca["x"] + 1, peca["y"]):
                    peca["x"] += 1
                elif evento.key == pygame.K_DOWN and not colide(tab, peca["forma"], peca["x"], peca["y"] + 1):
                    peca["y"] += 1
                elif evento.key == pygame.K_UP:
                    nova_forma = rotacionar(peca["forma"])
                    if not colide(tab, nova_forma, peca["x"], peca["y"]):
                        peca["forma"] = nova_forma

        desenhar_bloco(tab)
        desenhar_bloco(peca["forma"], peca["x"], peca["y"])
        desenhar_interface(pontos, nivel, tempo_decorrido, queda_vel, recorde)

        # Atualiza a tela
        pygame.display.flip()

# Iniciar o jogo
jogar()

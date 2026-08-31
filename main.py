import pygame
from scripts.cenas import Partida, Menu

pygame.init()

tamanhoTela = [400, 600]
tela = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption("Carro Desvia - Exercício 1")
relogio = pygame.time.Clock()
corFundo = (15, 25, 40)

listaCenas = {
    "partida": Partida(tela),
    "menu": Menu(tela)
}

cenaAtual = "menu"

rodando = True
while rodando:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            rodando = False

    tela.fill(corFundo)

    cenaAtual = listaCenas[cenaAtual].atualizar()

    relogio.tick(60)
    pygame.display.flip()

pygame.quit()
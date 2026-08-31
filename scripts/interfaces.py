import pygame

class Texto:
    def __init__(self, tela, texto, x, y, cor, tamanho):
        self.tela = tela
        self.texto = texto
        self.posicao = (x, y)
        self.cor = cor
        self.tamanho = tamanho
        pygame.font.init()
        self.fonte = pygame.font.Font(None, self.tamanho)
        self.imagemTexto = self.fonte.render(self.texto, True, self.cor)

    def desenhar(self):
        self.tela.blit(self.imagemTexto, self.posicao)

    def atualizarTexto(self, novoTexto):
        self.imagemTexto = self.fonte.render(novoTexto, True, self.cor)


class Botao:
    def __init__(self, tela, texto, x, y, tamanho, corFundo, corTexto):
        self.tela = tela
        self.texto = Texto(tela, texto, x, y, corTexto, tamanho)
        self.posicao = (x, y)
        self.corFundo = corFundo
        self.rect = pygame.Rect(x - 15, y - 8, self.texto.imagemTexto.get_width() + 30, self.texto.imagemTexto.get_height() + 16)

    def desenhar(self):
        pygame.draw.rect(self.tela, self.corFundo, self.rect, border_radius=10)
        self.texto.desenhar()

    def get_click(self):
        posicaoMouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(posicaoMouse) and pygame.mouse.get_pressed()[0]:
            return True
        return False
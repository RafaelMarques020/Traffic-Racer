import pygame

class Jogador:
    def __init__(self, tela):
        self.tela = tela
        self.largura = 50
        self.altura = 80
        self.x = tela.get_width() // 2 - self.largura // 2
        self.y = tela.get_height() - 120
        self.velocidade = 6

        # Carrega a imagem do carro
        self.imagem = pygame.image.load("assets/carro.png").convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (self.largura, self.altura))

    def atualizar(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.x -= self.velocidade
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.x += self.velocidade

        # Limites da pista
        self.x = max(40, min(self.tela.get_width() - self.largura - 40, self.x))

    def desenhar(self):
        self.tela.blit(self.imagem, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)
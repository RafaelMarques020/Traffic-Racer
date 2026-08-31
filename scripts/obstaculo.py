import pygame
import random

class Obstaculo:
    def __init__(self, tela):
        self.tela = tela
        self.largura = random.randint(40, 70)
        self.altura = random.randint(50, 80)
        self.x = random.randint(50, tela.get_width() - self.largura - 50)
        self.y = -self.altura
        self.velocidade = random.uniform(4, 7)
        self.cor = random.choice([
            (220, 40, 40),
            (255, 140, 0),
            (40, 200, 80),
            (180, 50, 255)
        ])

    def atualizar(self):
        self.y += self.velocidade

    def desenhar(self):
        pygame.draw.rect(self.tela, self.cor, (self.x, self.y, self.largura, self.altura), border_radius=6)
        pygame.draw.rect(self.tela, (255, 255, 255), (self.x + 5, self.y + 5, self.largura - 10, 10))

    def saiu_da_tela(self):
        return self.y > self.tela.get_height()

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)
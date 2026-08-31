import pygame
from scripts.jogador import Jogador
from scripts.obstaculo import Obstaculo
from scripts.interfaces import Texto, Botao

class Partida:
    def __init__(self, tela):
        self.tela = tela
        self.jogador = Jogador(tela)
        self.obstaculos = []
        self.estado = "partida"
        self.pontosValor = 0
        self.contador = 0
        self.tempoSpawn = 0
        self.velocidadeJogo = 1.0
        self.pontosTexto = Texto(tela, "Pontos: 0", 15, 15, (255, 255, 255), 36)

    def reiniciar(self):
        self.jogador = Jogador(self.tela)
        self.obstaculos = []
        self.pontosValor = 0
        self.contador = 0
        self.tempoSpawn = 0
        self.velocidadeJogo = 1.0
        self.pontosTexto.atualizarTexto("Pontos: 0")

    def atualizar(self):
        self.estado = "partida"
        self.jogador.atualizar()

        # Spawn de obstáculos
        self.tempoSpawn += 1
        if self.tempoSpawn > max(25, 55 - int(self.velocidadeJogo * 4)):
            self.tempoSpawn = 0
            self.obstaculos.append(Obstaculo(self.tela))

        # Atualiza obstáculos
        for obs in self.obstaculos[:]:
            obs.atualizar()
            if obs.saiu_da_tela():
                self.obstaculos.remove(obs)
                self.pontosValor += 10
                self.pontosTexto.atualizarTexto(f"Pontos: {self.pontosValor}")

        # Aumenta dificuldade
        self.contador += 1
        if self.contador > 60:
            self.contador = 0
            self.velocidadeJogo += 0.06
            for obs in self.obstaculos:
                obs.velocidade += 0.12

        # Colisão
        for obs in self.obstaculos:
            if self.jogador.get_rect().colliderect(obs.get_rect()):
                self.estado = "menu"
                self.reiniciar()

        # Desenho
        self.desenhar_pista()
        for obs in self.obstaculos:
            obs.desenhar()
        self.jogador.desenhar()
        self.pontosTexto.desenhar()

        return self.estado

    def desenhar_pista(self):
        # Fundo da pista
        pygame.draw.rect(self.tela, (40, 40, 40), (30, 0, self.tela.get_width() - 60, self.tela.get_height()))
        # Linhas laterais amarelas
        pygame.draw.rect(self.tela, (255, 220, 50), (30, 0, 8, self.tela.get_height()))
        pygame.draw.rect(self.tela, (255, 220, 50), (self.tela.get_width() - 38, 0, 8, self.tela.get_height()))
        # Linha central tracejada
        for y in range(0, self.tela.get_height(), 50):
            pygame.draw.rect(self.tela, (255, 255, 255), (self.tela.get_width() // 2 - 4, y, 8, 25))


class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.titulo = Texto(tela, "  Traffic Racer", 70, 150, (255, 220, 50), 55)
        self.subtitulo = Texto(tela, "Desvie dos obstáculos!", 90, 230, (255, 255, 255), 32)
        self.botao_jogar = Botao(tela, "JOGAR", 150, 340, 40, (40, 200, 80), (0, 0, 0))
        self.estado = "menu"

    def atualizar(self):
        self.estado = "menu"
        self.titulo.desenhar()
        self.subtitulo.desenhar()
        self.botao_jogar.desenhar()

        if self.botao_jogar.get_click():
            self.estado = "partida"

        return self.estado
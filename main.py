import pygame
import sys
from fruit import Fruit
from snake import Snake
pygame.init()
pygame.mixer.pre_init()
tamanioCelda = 40
numeroCeldas = 20
screen = pygame.display.set_mode(
    (numeroCeldas*tamanioCelda, numeroCeldas*tamanioCelda))
reloj = pygame.time.Clock()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)


#fondo
fondo = pygame.image.load('Imagenes/fondo.png').convert_alpha()
game_over_sound=pygame.mixer.Sound('Musica/game_over.mp3')
# Muisca de fondo
pygame.mixer.music.load('Musica\juego.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.25)


class Main:
    def __init__(self):
        self.serpiente = Snake()
        self.fruta = Fruit(numeroCeldas)

    def update(self):
        self.serpiente.move_snake()
        self.comerFruta()
        self.muerte()

    def draw(self):
        screen.blit(fondo, [0, 0])
        self.fruta.draw(screen, tamanioCelda)
        self.serpiente.draw_snake(screen, tamanioCelda)
        self.score()

    def comerFruta(self):
        if self.serpiente.body[0] == self.fruta.pos:
            self.fruta.randomize()
            self.serpiente.grow()
            self.serpiente.juego_sonido_comer()
            for block in self.serpiente.body:
                if block == self.fruta.pos:
                    self.fruta.randomize()

    def muerte(self):
        if not 0 <= self.serpiente.body[0].x < numeroCeldas or not 0 <= self.serpiente.body[0].y < numeroCeldas:
            self.game_over()
        if self.serpiente.body[0] in self.serpiente.body[1:]:
            self.game_over()

    def game_over(self):
        self.serpiente.reset()
        game_over_sound.play()

    def score(self):
        score_text = str(len(self.serpiente.body)-3)
        score_surface = game_font.render(
            'Score: '+str(score_text), True, (255, 255, 255))
        screen.blit(score_surface, (0, 0))


game_font = pygame.font.Font('Fonts/AmericanCaptain.otf', 25)


main_game = Main()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.serpiente.direction.y != 1:
                    main_game.serpiente.direction = pygame.Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.serpiente.direction.y != -1:
                    main_game.serpiente.direction = pygame.Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.serpiente.direction.x != 1:
                    main_game.serpiente.direction = pygame.Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.serpiente.direction.x != -1:
                    main_game.serpiente.direction = pygame.Vector2(1, 0)
            if event.key == pygame.K_p:
                main_game.serpiente.pause()
            if event.key == pygame.K_r:
                main_game.serpiente.reset()
    
    #screen.fill((0, 0, 0))
    main_game.draw()
    pygame.display.update()
    reloj.tick(60)

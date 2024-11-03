#Importação dos módulos
import pygame #pip install pygame
import random
import time
import playsound
from pygame.locals import *


def escolher_cor_aleatoria():
    pisca_vermelho = {'cor':cor_vermelho,'posicao':(251,282),'raio':130}
    pisca_verde = {'cor': cor_verde, 'posicao': (251, 282), 'raio': 130}
    pisca_laranja = {'cor': cor_laranja, 'posicao': (251, 282), 'raio': 130}
    pisca_azul = {'cor': cor_azul, 'posicao': (251, 282), 'raio': 130}
    cores = [pisca_vermelho,pisca_verde,pisca_laranja,pisca_azul]
    return random.choice(cores)


def piscar_cores(lista_cores):
    for cor in lista_cores:
        if cor['cor'] == cor_verde:
            #Desenhar 1/4 do circulo verde
            pygame.draw.circle(interface,cor['cor'],cor['posicao'],cor['raio'],draw_top_right=True)
        elif cor['cor'] == cor_laranja:
            pygame.draw.circle(interface, cor['cor'], cor['posicao'], cor['raio'], draw_bottom_left=True)
        elif cor['cor'] == cor_vermelho:
            pygame.draw.circle(interface, cor['cor'], cor['posicao'], cor['raio'], draw_bottom_right=True)
        elif cor['cor'] == cor_azul:
            pygame.draw.circle(interface, cor['cor'], cor['posicao'], cor['raio'], draw_top_left=True)
        pygame.display.update()
        time.sleep(0.4) #Tempo para mostrar a proxima cor
        interface.blit(Fundo,(0,30)) #Retorna para a imagem anterior
        pygame.display.update()
        time.sleep(0.4) #Tempo para a cor ficar apagada


def obter_resposta(quantidade_cores):
    resposta_usuario = [] #Armazena a resposta
    while quantidade_cores > 0:
        #Aguarda a resposta do usuario
        for evento in pygame.event.get():
            if evento.type == QUIT:
                quit()
            if evento.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if botao_verde.collidepoint(mouse):
                    resposta_usuario.append(cor_verde)
                    quantidade_cores -= 1
                elif botao_laranja.collidepoint(mouse):
                    resposta_usuario.append(cor_laranja)
                    quantidade_cores -= 1
                elif botao_vermelho.collidepoint(mouse):
                    resposta_usuario.append(cor_vermelho)
                    quantidade_cores -= 1
                elif botao_azul.collidepoint(mouse):
                    resposta_usuario.append(cor_azul)
                    quantidade_cores -= 1
    return resposta_usuario


def restart():
    texto_jogar_novamente = fonte_botoes.render('RESTART',True,cor_preto) #Texto do botao jogar novamente
    interface.blit(Fundo,(0,30))
    botao_jogar_novamente = pygame.draw.rect(interface,cor_branco,(175,70,155,60))
    interface.blit(texto_jogar_novamente,(176,73))
    pygame.display.update()
    while True: #Aguarda o clique do usuario
        for evento in pygame.event.get():
            if evento.type == QUIT:
                quit()
            if evento.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if botao_jogar_novamente.collidepoint(mouse):
                    interface.blit(Fundo,(0,30))
                    pygame.display.update()
                    return True


playsound.playsound('musica_tema.mp3',block = False)

pygame.init() #Inicialização do pygame
interface = pygame.display.set_mode((500,530)) #Definindo o tamanho da interface passando largura e altura
fonte_botoes = pygame.font.SysFont('Arial',40) #Definindo a fonte dos botoes
fonte_contagem = pygame.font.SysFont('Arial',30) #Definindo a fonte da contagem de pontos
barra_status = pygame.Surface((interface.get_width(),30)) #Criação da área de contagem de pontos

Fundo = pygame.image.load('Imagem.png')

#Definição das cores
cor_preto = (0,0,0)
cor_branco = (255,255,255)
cor_vermelho = (255,0,0)
cor_verde = (0,255,0)
cor_azul = (0,0,255)
cor_laranja = (255,127,0)

#Poligonos que detectam a escolha do mouse
botao_azul = pygame.draw.circle(interface,cor_azul,center=(251,282),radius=130,draw_top_left=True)
botao_verde = pygame.draw.circle(interface,cor_verde,center=(251,282),radius=130,draw_top_right=True)
botao_vermelho = pygame.draw.circle(interface,cor_vermelho,center=(251,282),radius=130,draw_bottom_right=True)
botao_laranja = pygame.draw.circle(interface,cor_laranja,center=(251,282),radius=130,draw_bottom_left=True)


#Textos
texto_comeco = fonte_botoes.render('START',True,cor_preto) #Render() passa o texto, define se vai suavizá-lo e a cor
pontos = 0 #Pontuação
cores_sequencia =[] #Sequencia de cores que vai piscar
jogando = False


while not jogando: #Se não estiver jogando faça:

    interface.blit(Fundo,(0,30)) #Escreve o background
    botao_comecar = pygame.draw.rect(interface,cor_branco,(180,70,150,60))
    #Desenha o botao de começo passando as coordenadas
    interface.blit(texto_comeco,(200,74)) #Desenha o texto no botao
    pygame.display.update() #Atualiza a interface para o usuario
    for evento in pygame.event.get(): #Para cada clique do usuario faça:
        if evento.type == QUIT:
            quit() #Fechar a interface
        if evento.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos() #Pega a posição do mouse
            if botao_comecar.collidepoint(mouse): #Testa se foi na posição do botao começar
                jogando = True #Coloca jogando como True para finalizar o loop

interface.blit(Fundo,(0,30)) #Atualiza o fundo mais uma vez para tirar o botao comecar
pygame.display.update() #Atualiza para o usuario

while jogando: #Enquanto estiver em jogo
    barra_status.fill(cor_preto) #Sobrescrever o texto antigo para o novo
    pontuacao = fonte_contagem.render('Pontos:'+str(pontos),True,(cor_branco))
    barra_status.blit(pontuacao,(0,0)) #Desenha a pontuação
    interface.blit(barra_status,(0,0)) #Desenha a barra
    pygame.display.update() #Apresenta ao usuario
    time.sleep(.5) #Delay para começar a proxima sequencia
    for evento in pygame.event.get(): #Dar opção do usuario fechar o jogo enquanto joga
        if evento.type == QUIT:
            quit()
    cores_sequencia.append(escolher_cor_aleatoria()) #Escolhe uma cor aleatória e adiciona na lista sequencia
    piscar_cores(cores_sequencia) #Pisca as cores que estão em sequencia
    resposta_jogador = obter_resposta(len(cores_sequencia)) #Aguarda a resposta do jogador
    sequencia_cores = [] #Lista para conferencia
    for cor in cores_sequencia:
        sequencia_cores.append(cor['cor']) #Adiciona as cores em sequencia_cores a partir da chave cor
    if sequencia_cores == resposta_jogador: #Caso o usuario acerte:
        pontos += 1 #Atualiza os pontos
    else:
        jogando = restart() #Perguntar se o usuario deseja reiniciar
        if jogando: #Se retornar verdadeiro reinicia o loop
            pontos = 0 #Zera a pontuação
            cores_sequencia = [] #Zera a sequencia

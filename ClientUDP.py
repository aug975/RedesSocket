import socket  # importa modulo socket
import sys
import pygame
import datetime

pygame.init()

pygame.display.init()
size = [1100, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('BlackJack - por Augusto R Scrideli')
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
gray = (128, 128, 128)
DEFAULT_CARD_SIZE = (80, 100)


# gera log da acao no servidor
def geralog(logtxt):
    current_time = datetime.datetime.now()
    print('')
    print("[", current_time.hour, ":", current_time.minute, ":", current_time.second, "] - " + logtxt)


# monta a tela de fundo padrao, sem botoes
def telapadrao():
    screen.fill(white)
    fundo = pygame.image.load("CardTable.jpg")
    fundo.set_alpha(200)
    screen.blit(fundo, (0, 0))
    

# adiciona os botoes "entrar" e "sair"
def telaentra():
    banner = pygame.image.load("blankmsg2.jpg")
    banner.set_alpha(128)
    screen.blit(banner, (0, 0))
    tFonte = pygame.font.SysFont("Impact", 36)
    con = tFonte.render("BlackJack", True, black)
    screen.blit(con, [350, 20])
    tFonte = pygame.font.SysFont("Courier New", 20)
    con = tFonte.render("por Augusto Rassi Scrideli", True, black)
    screen.blit(con, [350, 60])
    screen.blit(banner, (0, 500))
    entrar = pygame.image.load("entrar.jpg")
    screen.blit(entrar, (20, 550))
    sair = pygame.image.load("sair.jpg")
    screen.blit(sair, (940, 550))


# adiciona os botoes "iniciar" e "sair"
def telainicia():
    tFonte = pygame.font.SysFont("Bahnschrift", 15)
    con = tFonte.render("Outro jogador já conectado.", True, black)
    screen.blit(con, [250, 50])
    iniciar = pygame.image.load("iniciar.jpg")
    screen.blit(iniciar, (480, 40))
    sair = pygame.image.load("sair.jpg")
    screen.blit(sair, (940, 550))
    pygame.display.flip()


# adiciona os botoes "iniciar" e "sair"
def telainiciapos():
    tFonte = pygame.font.SysFont("Bahnschrift", 15)
    con = tFonte.render("Outro jogador já conectado.", True, black)
    screen.blit(con, [250, 50])
    iniciar = pygame.image.load("iniciar.jpg")
    screen.blit(iniciar, (480, 40))
    sair = pygame.image.load("sair.jpg")
    screen.blit(sair, (940, 550))
    pygame.display.flip()


# limpa msg adiciona os botoes "recarregar" e "sair"
def telarecarga():
    con = tFonte.render("Nao ha outro jogador no servidor no momento.", True, black)
    screen.blit(con, [250, 50])
    iniciar = pygame.image.load("recarregar.jpg")
    screen.blit(iniciar, (600, 40))
    sair = pygame.image.load("sair.jpg")
    screen.blit(sair, (940, 550))
    pygame.display.flip()


# adiciona os botoes "outra" e "parar"
def telacarta():
    outra = pygame.image.load("outra.jpg")
    screen.blit(outra, (310, 480))
    parar = pygame.image.load("parar.jpg")
    screen.blit(parar, (650, 480))
    pygame.display.flip()


def telafull():
    tFonte = pygame.font.SysFont("Bahnschrift", 20)
    con = tFonte.render("Ja ha 2 jogadores conectados", True, black)
    screen.blit(con, [520, 50])
    sair = pygame.image.load("sair.jpg")
    screen.blit(sair, (940, 550))
    pygame.display.flip()


def telaespera(jogn):
    if jogn == 1:
        con = tFonte.render("Jogador 1", True, black)
        screen.blit(con, [100, 50])
        con = tFonte.render("Aguardando Jogador 2 ...", True, black)
        screen.blit(con, [700, 50])
    else:
        con = tFonte.render("Jogador 2", True, black)
        screen.blit(con, [700, 50])
        con = tFonte.render("Aguardando Jogador 1 ...", True, black)
        screen.blit(con, [250, 50])

    pygame.display.flip()


# Posiciona as cartas na tela, de acordo com o numero da carta e jogador
def mostracarta(carta, num, jogn):
    ecarta = carta + ".png"
    pcarta = pygame.image.load(ecarta)
    pcarta = pygame.transform.scale(pcarta, DEFAULT_CARD_SIZE)
    posx = 220 + num * 35 + (jogn - 1) * 400
    posy = 370
    screen.blit(pcarta, (posx, posy))
    pygame.display.flip()


# envia mensagem usando socket UDP
def enviamsg(msg):
    sock.sendto(msg.encode('UTF-8'), (IP_destino, PORTA_destino))


# recebe mensagem usando socket UDP
def recebemsg():
    data, addr = sock.recvfrom(1024)
    msg = data.decode('utf-8')
    return msg


# verifica quem foi o vencedor

def apuraresult(total1, total2):
    tot1 = int(total1)
    tot2 = int(total2)
    if tot1 > 21:
        if tot2 > 21:
            txt = "Ambos excederam 21 pontos!"
        else:
            txt = "Jogador 2 foi o vencedor!"
    elif tot1 == 21:
        if tot2 != 21:
            txt = "Jogador 1 foi o vencedor!"
        else:
            txt = "Empate! Ambos fizeram 21 pontos."
    else:
        if tot2 > 21:
            txt = "Jogador 1 foi o vencedor!"
        if tot2 == 21:
            txt = "Jogador 2 foi o vencedor!"
        else:
            if tot1 > tot2:
                txt = "Jogador 1 foi o vencedor!"
            else:
                txt = "Jogador 2 foi o vencedor!"
    return txt


telapadrao()
telaentra()

IP_destino = "192.168.3.33"  # Endereço IP do servidor
PORTA_destino = 4202  # Numero de porta do servidor

# Criação de socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ctrloop = 0
ctrloop2 = 0

running = True
NomeJogador = "Jogador"
msgr = ""
x = 0
y = 0
geralog("Aberta sessão CLIENTE")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:

            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            # Clicou em Entrar para conectar ao servidor
            if (550 <= y < 580) and (20 <= x < 160):

                telapadrao()
                NomeJogador = "Jogador"

                msg = "E:" + NomeJogador
                enviamsg(msg)

                msgr = recebemsg()

                # se um terceiro jogador tenta conectar
                if msgr == "C":
                    telapadrao()
                    telafull()
                # Jogador 1 ou 2 conectando
                else:
                    list1 = msgr.split(":")
                    msg1 = list1[0]
                    msg2 = list1[1]
                    msg3 = list1[2]

                    conectados = int(msg3)
                    jogn = int(msg2)  # numero do jogador
                    msg4 = msg1 + " " + str(jogn)
                    NomeJogador = msg4

                    geralog(NomeJogador + " conectado")

                    if (conectados == 2) and (ctrloop == 0):
                        telainicia()

                    # Para poder iniciar o jogo apenas se houver duas sessões ativas
                    # quando o primeiro cliente entra abre um socket que fica aguardando uma resposta
                    # que e enviada pelo servidor apenas quando o segundo cliente tentr
                    # Foi implantado um timeout de 15 s para este socket aberto
                    # Apos este periodo, o cliente fecha conexão e apura apenas o resultado individual

                    else:

                        tFonte = pygame.font.SysFont("Bahnschrift", 20,True)
                        telaespera(jogn)

                        # aguarda proximo jogador
                        sock.settimeout(15)

                        espera = 0
                        try:
                            msgr = recebemsg()
                            espera = msgr
                        # este uso de except nao e ideal mas nao deve causar problemas
                        except:
                            espera = 0

                        sock.settimeout(None)
                        # sock.shutdown

                        # o outro jogador nao finalizou no tempo definido
                        if espera == 0:
                            geralog("Nao houve conexao de um segundo jogador")
                            msgr = ''
                            telapadrao()
                            telarecarga()

                            msg = "V:" + NomeJogador
                            enviamsg(msg)

                            ctrloop = 1
                        else:
                            telainiciapos()

                pygame.mouse.set_pos(0, 0)

            # Clicou em Iniciar para comecar o jogo
            elif (40 <= y < 70) and (480 <= x < 620):

                msg = "I:" + NomeJogador
                enviamsg(msg)

                msgr = recebemsg()
                # se um terceiro jogador tenta conectar
                if msgr == "L":
                    telapadrao()
                    telafull()

                # Jogador 1 ou 2 conectando
                else:
                    list1 = msgr.split(":")
                    msg1 = list1[0]  # carta 1
                    msg2 = list1[1]  # carta 2
                    msg3 = list1[2]  # valor carta 1
                    msg4 = list1[3]  # valor carta 2
                    msg5 = list1[4]  # soma
                    msg6 = list1[5]  # conectados

                    telapadrao()

                    geralog("Iniciou. Recebidas as duas primeiras cartas.")

                    tFonte = pygame.font.SysFont("Courier New", 18)
                    if jogn == 1:
                        con = tFonte.render(NomeJogador, True, white)
                        screen.blit(con, [320, 320])
                    else:
                        con = tFonte.render(NomeJogador, True, white)
                        screen.blit(con, [680, 320])

                    mostracarta(msg1, 1, jogn)
                    mostracarta(msg2, 2, jogn)

                    if jogn == 1:
                        jogm = 2
                    else:
                        jogm = 1

                    mostracarta('verso', 1, jogm)
                    mostracarta('verso', 2, jogm)

                    telacarta()

                    sindex = 2

                pygame.mouse.set_pos(0, 0)

            # Clicou em Outra...
            elif (480 <= y < 510) and (310 <= x < 450):

                if int(msg5) < 21:

                    geralog("Pediu outra carta.")

                    sindex = sindex + 1
                    msg = str(sindex) + ':' + msg5
                    enviamsg(msg)

                    msgr = recebemsg()

                    list1 = msgr.split(":")
                    msg1 = list1[0]  # carta
                    msg3 = list1[1]  # valor da carta
                    msg5 = list1[2]  # soma
                    msg6 = list1[3]  # conectados

                    mostracarta(msg1, sindex, jogn)

                    # Estourou pontuacao
                    if int(msg5) > 21:
                        outra2 = pygame.image.load("outra2.jpg")
                        screen.blit(outra2, (310, 480))
                        x = 700
                        y = 500

                    # Fez os 21 pontos
                    elif int(msg5) == 21:
                        outra2 = pygame.image.load("outra2.jpg")
                        screen.blit(outra2, (310, 480))
                        x = 700
                        y = 500

                    # TODO: tratar 21

                pygame.mouse.set_pos(0, 0)

            # Clicou em Parar ...
            elif (480 <= y < 510) and (650 <= x < 790):

                msg = 'P:'
                enviamsg(msg)

                msgri = recebemsg()

                geralog("Finalizou o jogo.")

                # se os dois jogadores não tiverem finalizado gera um delay aguardando o outro jogador
                # e finaliza com um só caso o segundo não finalize sua escolha em tempo

                if (msgri == '1') and (ctrloop == 0):

                    telapadrao()
                    geralog("Aguardando o proximo jogador finalizar.")

                    tFonte = pygame.font.SysFont("Courier New", 18)
                    con = tFonte.render("Jogador " + str(jogn), True, white)
                    tFonte = pygame.font.SysFont("Courier New", 18)
                    screen.blit(con, [(320 + (jogn - 1) * 460), 320])

                    msg = 'M:' + str(jogn)  # index, jogador
                    enviamsg(msg)

                    msgr = recebemsg()

                    con = tFonte.render("Aguardando o proximo jogador Finalizar ...", True, black)
                    screen.blit(con, [520, 40])

                    list1 = msgr.split(":")
                    ncartas = len(list1)
                    i = 0
                    while (i < ncartas) and (list1[i] != '0'):
                        mostracarta(list1[i], i + 1, jogn)
                        i = i + 1

                    pygame.display.flip()

                    # Para poder exibir na mesma tela de cliente o resultado das duas sessões ativas
                    # cada cliente ao terminar seu jogo abre um socket que fica aguardando uma resposta
                    # que e enviada pelo servidor apenas quando o segundo cliente tambem completa o jogo
                    # e escolhe a opcao PARAR.
                    # Foi implantado um timeout de 20 s para este socket aberto
                    # Apos este periodo, o cliente fecha conexão e apura apenas o resultado individual

                    # aguarda proximo jogador
                    sock.settimeout(20)
                    espera = 0
                    try:
                        msgr = recebemsg()
                        espera = msgr
                    # uso nao ideal de except, mas nao deve causar problemas
                    except:
                        espera = 1

                    sock.settimeout(None)
                    # sock.shutdown

                    # o outro jogador nao finalizou no tempo definido
                    if espera == 1:
                        telapadrao()
                        con = tFonte.render("O outro jogador não finalizou o jogo.", True, black)
                        screen.blit(con, [520, 40])

                        geralog("O outro jogador não finalizou o jogo.")

                        msg = 'M:' + str(jogn)  # index, jogador
                        enviamsg(msg)

                        msgr = recebemsg()
                        list1 = msgr.split(":")
                        ncartas = len(list1)

                        i = 0
                        while (i < ncartas) and (list1[i] != '0'):
                            mostracarta(list1[i], i + 1, jogn)
                            i = i + 1

                        tFonte = pygame.font.SysFont("Courier New", 14)

                        msg = 'T:' + str(jogn)  # index, jogador
                        enviamsg(msg)

                        total1 = recebemsg()
                        msgs = "Total = " + total1

                        con = tFonte.render(msgs, True, white)
                        screen.blit(con, [(320 + (jogn - 1) * 460), 510])

                        sair = pygame.image.load("sair.jpg")
                        screen.blit(sair, (940, 550))

                        pygame.display.flip()

                        ctrloop = 1  # limita a espera do segundo jogador a um loop
                    else:

                        geralog('Os dois jogadores finalizaram')
                        telapadrao()

                        # montar as telas de cartas
                        tFonte = pygame.font.SysFont("Courier New", 18)
                        con = tFonte.render("Jogador 1", True, white)
                        screen.blit(con, [320, 320])
                        con = tFonte.render("Jogador 2", True, white)
                        screen.blit(con, [680, 320])

                        msg = 'M:1'  # index, jogador
                        enviamsg(msg)

                        msgr = recebemsg()
                        list1 = msgr.split(":")
                        ncartas = len(list1)

                        i = 0
                        while (i < ncartas) and (list1[i] != '0'):
                            mostracarta(list1[i], i + 1, 1)
                            i = i + 1

                        msg = 'M:2'  # index
                        enviamsg(msg)

                        msgr = recebemsg()
                        list1 = msgr.split(":")
                        ncartas = len(list1)

                        j = 0
                        while (j < ncartas) and (list1[j] != '0'):
                            mostracarta(list1[j], j + 1, 2)
                            j = j + 1

                        tFonte = pygame.font.SysFont("Courier New", 14)

                        msg = 'T:1'  # index, jogador
                        enviamsg(msg)
                        total1 = recebemsg()
                        msg = "Total = " + total1

                        con = tFonte.render(msg, True, white)
                        screen.blit(con, [320, 510])

                        msg = 'T:2'  # index, jogador
                        enviamsg(msg)
                        total2 = recebemsg()
                        msg = "Total = " + total2

                        con = tFonte.render(msg, True, white)
                        screen.blit(con, [680, 510])

                        # verifica quem foi o vencedor

                        tFonte = pygame.font.SysFont("Courier New", 20)
                        ftxt = apuraresult(total1, total2)
                        con = tFonte.render(ftxt, True, black)
                        screen.blit(con, [520, 40])

                        sair = pygame.image.load("sair.jpg")
                        screen.blit(sair, (940, 550))

                # habilita a sequencia normal quando os dois jogadores tiverem finalizados
                elif msgri == '2':

                    geralog('Os dois jogadores finalizaram')
                    telapadrao()

                    # montar as telas de cartas
                    tFonte = pygame.font.SysFont("Courier New", 18)
                    con = tFonte.render("Jogador 1", True, white)
                    screen.blit(con, [320, 320])
                    con = tFonte.render("Jogador 2", True, white)
                    screen.blit(con, [680, 320])

                    msg = 'M:1'  # index, jogador
                    enviamsg(msg)

                    msgr = recebemsg()
                    list1 = msgr.split(":")
                    ncartas = len(list1)

                    i = 0
                    while (i < ncartas) and (list1[i] != '0'):
                        mostracarta(list1[i], i + 1, 1)
                        i = i + 1

                    msg = 'M:2'  # index
                    enviamsg(msg)

                    msgr = recebemsg()
                    list1 = msgr.split(":")
                    ncartas = len(list1)

                    j = 0
                    while (j < ncartas) and (list1[j] != '0'):
                        mostracarta(list1[j], j + 1, 2)
                        j = j + 1

                    tFonte = pygame.font.SysFont("Courier New", 14)

                    msg = 'T:1'  # index, jogador
                    enviamsg(msg)
                    total1 = recebemsg()
                    msg = "Total = " + total1

                    con = tFonte.render(msg, True, white)
                    screen.blit(con, [320, 510])

                    msg = 'T:2'  # index, jogador
                    enviamsg(msg)
                    total2 = recebemsg()
                    msg = "Total = " + total2

                    con = tFonte.render(msg, True, white)
                    screen.blit(con, [680, 510])

                    # verifica quem foi o vencedor

                    tFonte = pygame.font.SysFont("Courier New", 20)
                    ftxt = apuraresult(total1, total2)
                    con = tFonte.render(ftxt, True, black)
                    screen.blit(con, [520, 40])

                    sair = pygame.image.load("sair.jpg")
                    screen.blit(sair, (940, 550))

                pygame.mouse.set_pos(0, 0)

            # Clicou em Recarregar para voltar a tela inicial    
            elif (40 <= y < 70) and (600 <= x < 740):
                msg = 'R:'  # index
                enviamsg(msg)

                telapadrao()
                telaentra()

                geralog(NomeJogador + " recarregou")
                pygame.mouse.set_pos(0, 0)

                # Clicou em Sair para fechar o programa
            elif (550 <= y < 580) and (940 <= x < 1080):
                msg = 'S:'  # index
                enviamsg(msg)

                geralog(NomeJogador + ' saiu do jogo')

                running = False
            # Zera x e y para que não entre novamente no ultimo elif
            else:
                x = 0
                y = 0

    pygame.display.update()

pygame.quit()

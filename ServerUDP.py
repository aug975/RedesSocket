import socket
import random
import datetime

IP_servidor = "192.168.3.33"  # endereço onde o Server será executado
PORTA_servidor = 4202  # porta aberta pelo Server para conexão

# Criação de socket UDP
# Argumentos, AF_INET que declara a família do protocolo; se fosse um envio via Bluetooth usariamos AF_BLUETOOTH
# SOCK_DGRAM, indica que será UDP.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP e porta que o servidor deve aguardar a conexão
sock.bind((IP_servidor, PORTA_servidor))

# declaramos variaveis
endereco = list(['0', '0'])
jogador = list(['0', '0'])
carta1 = list(['0', '0'])
carta2 = list(['0', '0'])
carta3 = list(['0', '0'])
carta4 = list(['0', '0'])
carta5 = list(['0', '0'])
carta6 = list(['0', '0'])
carta7 = list(['0', '0'])
carta8 = list(['0', '0'])
carta9 = list(['0', '0'])
carta10 = list(['0', '0'])
carta11 = list(['0', '0'])
vcarta1 = list(['0', '0'])
vcarta2 = list(['0', '0'])
vcarta3 = list(['0', '0'])
vcarta4 = list(['0', '0'])
vcarta5 = list(['0', '0'])
vcarta6 = list(['0', '0'])
vcarta7 = list(['0', '0'])
vcarta8 = list(['0', '0'])
vcarta9 = list(['0', '0'])
vcarta10 = list(['0', '0'])
vcarta11 = list(['0', '0'])
soma = list(['0', '0'])

tdcartas = (
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
tcartas = (
    'AP', 'AC', 'AE', 'AO', '2P', '2C', '2E', '2O', '3P', '3C', '2E', '3O', '4P', '4C', '4E', '4O', '5P', '5C', '5E',
    '5O',
    '6P', '6C', '6E', '6O', '7P', '7C', '7E', '7O', '8P', '8C', '8E', '8O', '9P', '9C', '9E', '9O', '10P', '10C', '10E',
    '10O', 'QP', 'QC', 'QE', 'QO', 'JP', 'JC', 'JE', 'JO', 'KP', 'KC', 'KE', 'KO')
tvalorcarta = (
    1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10,
    10,
    10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)

dcartas = list(tdcartas)
cartas = list(tcartas)
valorcarta = list(tvalorcarta)

conectados = 0
cont = 0
apura1 = 0
apura2 = 0
end = ""


# envia mensagem usando socket UDP
def enviamsg(msg, end):
    sock.sendto(msg.encode('UTF-8'), end)


# gera log da acao no servidor
def geralog(logtxt):
    current_time = datetime.datetime.now()
    print('')
    print("[", current_time.hour, ":", current_time.minute, ":", current_time.second, "] - " + logtxt)


# sorteia uma posicao de carta, substitui o valor da lista dcartas por zero naquela posicao para evitar repeticao
def RetiraCarta():
    dcarta = 0
    while dcarta == 0:
        rn = random.randint(0, 51)
        dcarta = dcartas[rn]
    dcartas[rn] = 0
    return rn


# reseta os valores das cartas de um dos jogadores
def LimpaCartas(jog):
    carta1[jog] = '0'
    carta2[jog] = '0'
    carta3[jog] = '0'
    carta4[jog] = '0'
    carta5[jog] = '0'
    carta6[jog] = '0'
    carta7[jog] = '0'
    carta8[jog] = '0'
    carta9[jog] = '0'
    carta10[jog] = '0'
    carta11[jog] = '0'
    vcarta1[jog] = '0'
    vcarta2[jog] = '0'
    vcarta3[jog] = '0'
    vcarta4[jog] = '0'
    vcarta5[jog] = '0'
    vcarta6[jog] = '0'
    vcarta7[jog] = '0'
    vcarta8[jog] = '0'
    vcarta9[jog] = '0'
    vcarta10[jog] = '0'
    vcarta11[jog] = '0'
    soma[jog] = '0'
    return 0


# >>ROTINA PRINCIPAL
geralog("Aberta sessão no endereço: " + str(IP_servidor) + " : " + str(PORTA_servidor))
indexant = ""
endant = ""

while True:

    # Recebe mensagem via socket sock.recvform
    # aloca 1024 bytes
    # separa dados e armazena em data e o endereço de origem e guarda em addr

    data, addr = sock.recvfrom(1024)
    decoded = data.decode('utf-8')
    index, msg = decoded.split(":", 1)

    if (index == indexant) and (end == endant):
        index = ""
        end = ""
    else:
        indexant = index
        endant = addr

    # >>FUNCOES - Para busca de informações armazenadas nas variaveis do servidor

    # Devolve a relacao com a mao das cartas do jogador pra montagem da tela final de resultados
    if index == 'M':
        jogn = int(msg) - 1
        msg = str(carta1[jogn]) + ":" + str(carta2[jogn]) + ":" + str(carta3[jogn]) + ":" + str(
            carta4[jogn]) + ":" + str(carta5[jogn]) + ":" + str(carta6[jogn]) + ":" + str(carta7[jogn]) + ":" + str(
            carta8[jogn]) + ":" + str(carta9[jogn]) + ":" + str(carta10[jogn]) + ":" + str(carta11[jogn])
        enviamsg(msg, addr)

    #  Devolve a soma do valor das cartas do jogador pra montagem da tela final de resultados
    elif index == 'T':
        jogn = int(msg) - 1
        msg = str(int(vcarta1[jogn]) + int(vcarta2[jogn]) + int(vcarta3[jogn]) + int(vcarta4[jogn]) + int(
            vcarta5[jogn]) + int(vcarta6[jogn]) + int(vcarta7[jogn]) + int(vcarta8[jogn]) + int(vcarta9[jogn]) + int(
            vcarta10[jogn]) + int(vcarta11[jogn]))
        enviamsg(msg, addr)

    # >>EVENTOS - A partir de botões acionados pelo jogador na interface Cliente

    #  Jogador conecta, Servidor preenche a posição 'cont' para as listas com seu nome e enderço (IP/Porta)
    elif index == 'E':
        # verifica se ja nao tem 2 jogadores conectados
        if conectados < 2:
            # aponta para uso do registro 0 novamente (Jogador 1) caso este saia e o Jogador 2 permaneca
            # if (conectados == 1):
            #   if (endereco[0] == '0'):
            #       cont = 0

            if endereco[cont] == '0':
                conectados = conectados + 1

            jogador[cont] = msg + " " + str(cont + 1)
            endereco[cont] = addr

            geralog("Jogador " + str(cont + 1) + " conectou")

            msg = msg + ":" + str(cont + 1) + ":" + str(conectados)

            if cont == 0:
                cont = 1
            else:
                cont = 0
            if conectados == 2:
                enviamsg(msg, endereco[0])
                enviamsg(msg, endereco[1])
            else:
                enviamsg(msg, addr)
        else:
            msg = "C"  # nao permite entrada de terceiro jogador
            enviamsg(msg, addr)

    # Jogo é iniciado por algum jogador. Servidor preenche as listas com Valor das 2 primeiras cartas e soma 
    elif index == 'I':

        # verifica se ja nao tem 2 jogadores no jogo
        if conectados <= 2:

            rcont = endereco.index(
                addr)  # encontra a posicao nas listas correspondente a cada jogador a partir do seu endereco

            geralog("Jogador " + str(rcont + 1) + " iniciou o jogo")

            pos = RetiraCarta()
            carta1[rcont] = cartas[pos]
            vcarta1[rcont] = valorcarta[pos]

            pos = RetiraCarta()
            carta2[rcont] = cartas[pos]
            vcarta2[rcont] = valorcarta[pos]

            soma[rcont] = vcarta1[rcont] + vcarta2[rcont]

            msg = str(carta1[rcont]) + ":" + str(carta2[rcont]) + ":" + str(vcarta1[rcont]) + ":" + str(
                vcarta2[rcont]) + ":" + str(soma[rcont]) + ":" + str(int(conectados))

            enviamsg(msg, addr)

        else:
            msg = "L"  # Lotado - nao permite entrada de terceiro jogador
            enviamsg(msg, addr)

    # Jogador pede para não receber mais cartas
    elif index == 'P':
        rcont = endereco.index(
            addr)  # encontra a posicao nas listas correspondente a cada jogador a partir do seu endereco

        geralog("Jogador " + str(rcont + 1) + " parou de pedir cartas")

        if rcont == 0:
            if apura1 == 0:
                apura1 = 1
        else:
            if apura2 == 0:
                apura2 = 1

        msg = str(apura1 + apura2)

        # atualiza tela dos 2 jogadores
        if (apura1 + apura2) == 2:
            enviamsg(msg, endereco[0])
            enviamsg(msg, endereco[1])
        else:
            enviamsg(msg, addr)

        geralog("Tentativa de apuracao do resultado final")

    # Jogador recarrega o jogo
    elif index == 'R':
        # jogador entrou novamente no jogo
        try:
            rcont = endereco.index(
                addr)  # encontra a posicao nas listas correspondente a cada jogador a partir do seu endereco
            # limpar variaveis
            endereco[rcont] = '0'
            jogador[rcont] = '0'
            LimpaCartas(rcont)
            cont = cont - 1
            conectados = conectados - 1
            geralog("Jogador " + str(rcont + 1) + " reiniciou o jogo")

        # Jogador nao iniciou o jogo
        except:
            geralog("Jogador fechou programa antes de iniciar o jogo")

        # index = ""

    # Jogador abandona o jogo
    elif index == 'S':
        # jogador entrou no jogo antes de abandonar
        try:
            rcont = endereco.index(
                addr)  # encontra a posicao nas listas correspondente a cada jogador a partir do seu endereco
            # limpar variaveis
            endereco[rcont] = '0'
            jogador[rcont] = '0'
            LimpaCartas(rcont)
            cont = cont - 1
            conectados = conectados - 1

            geralog("Jogador " + str(rcont + 1) + " saiu do jogo")

        # Jogador nao iniciou o jogo
        except:
            geralog("Jogador fechou o programa antes de iniciar o jogo")

    # Jogador aguardou outro conectar mas nao entrou o segundo jogador
    elif index == 'V':
        rcont = endereco.index(
            addr)  # encontra a posicao nas listas correspondente a cada jogador a partir do seu endereco

        geralog("Jogador " + str(rcont + 1) + " nao encontrou um adversario no servidor")

    # Jogador pede outra carta
    elif index != "":
        rcont = endereco.index(
            addr)  # encontra a posicao nas listas correspondente a cada jogador a partir do seu endereco

        geralog("Jogador " + str(rcont + 1) + " pediu outra carta")

        pos = RetiraCarta()

        if index == '3':
            carta3[rcont] = cartas[pos]
            vcarta3[rcont] = valorcarta[pos]

            soma[rcont] = vcarta1[rcont] + vcarta2[rcont] + vcarta3[rcont]

            msg = str(carta3[rcont]) + ":" + str(vcarta3[rcont]) + ":" + str(soma[rcont]) + ":" + str(conectados)
            enviamsg(msg, addr)

        elif index == '4':
            carta4[rcont] = cartas[pos]
            vcarta4[rcont] = valorcarta[pos]

            soma[rcont] = vcarta1[rcont] + vcarta2[rcont] + vcarta3[rcont] + vcarta4[rcont]

            msg = str(carta4[rcont]) + ":" + str(vcarta4[rcont]) + ":" + str(soma[rcont]) + ":" + str(conectados)
            enviamsg(msg, addr)

        elif index == '5':
            carta5[rcont] = cartas[pos]
            vcarta5[rcont] = valorcarta[pos]

            soma[rcont] = vcarta1[rcont] + vcarta2[rcont] + vcarta3[rcont] + vcarta4[rcont] + vcarta5[rcont]

            msg = str(carta5[rcont]) + ":" + str(vcarta5[rcont]) + ":" + str(soma[rcont]) + ":" + str(conectados)
            enviamsg(msg, addr)

        elif index == '6':
            carta6[rcont] = cartas[pos]
            vcarta6[rcont] = valorcarta[pos]

            soma[rcont] = vcarta1[rcont] + vcarta2[rcont] + vcarta3[rcont] + vcarta4[rcont] + vcarta5[rcont] + vcarta6[
                rcont]

            msg = str(carta6[rcont]) + ":" + str(vcarta6[rcont]) + ":" + str(soma[rcont]) + ":" + conectados
            enviamsg(msg, addr)

        elif index == '7':
            carta7[rcont] = cartas[pos]
            vcarta7[rcont] = valorcarta[pos]

            soma[rcont] = vcarta1[rcont] + vcarta2[rcont] + vcarta3[rcont] + vcarta4[rcont] + vcarta5[rcont] + vcarta6[
                rcont] + vcarta7[rcont]

            msg = str(carta7[rcont]) + ":" + str(vcarta7[rcont]) + ":" + str(soma[rcont]) + ":" + conectados
            enviamsg(msg, addr)

        elif index == '8':
            carta8[rcont] = cartas[pos]
            vcarta8[rcont] = valorcarta[pos]

            soma[rcont] = vcarta1[rcont] + vcarta2[rcont] + vcarta3[rcont] + vcarta4[rcont] + vcarta5[rcont] + vcarta6[
                rcont] + vcarta7[rcont] + vcarta8[rcont]

            msg = str(carta8[rcont]) + ":" + str(vcarta8[rcont]) + ":" + str(soma[rcont]) + ":" + conectados
            enviamsg(msg, addr)

        elif index == '9':
            carta9[rcont] = cartas[pos]
            vcarta9[rcont] = valorcarta[pos]

            soma[rcont] = vcarta1[rcont] + vcarta2[rcont] + vcarta3[rcont] + vcarta4[rcont] + vcarta5[rcont] + vcarta6[
                rcont] + vcarta7[rcont] + vcarta8[rcont] + vcarta9[rcont]

            msg = str(carta9[rcont]) + ":" + str(vcarta9[rcont]) + ":" + str(soma[rcont]) + ":" + conectados
            enviamsg(msg, addr)

        elif index == '10':
            carta10[rcont] = cartas[pos]
            vcarta10[rcont] = valorcarta[pos]

            soma[rcont] = vcarta1[rcont] + vcarta2[rcont] + vcarta3[rcont] + vcarta4[rcont] + vcarta5[rcont] + vcarta6[
                rcont] + vcarta7[rcont] + vcarta8[rcont] + vcarta9[rcont] + vcarta10[rcont]

            msg = str(carta10[rcont]) + ":" + str(vcarta10[rcont]) + ":" + str(soma[rcont]) + ":" + conectados
            enviamsg(msg, addr)

        elif index == '11':
            carta11[rcont] = cartas[pos]
            vcarta11[rcont] = valorcarta[pos]

            soma[rcont] = vcarta1[rcont] + vcarta2[rcont] + vcarta3[rcont] + vcarta4[rcont] + vcarta5[rcont] + vcarta6[
                rcont] + vcarta7[rcont] + vcarta8[rcont] + vcarta9[rcont] + vcarta10[rcont] + vcarta11[rcont]

            msg = str(carta11[rcont]) + ":" + str(vcarta11[rcont]) + ":" + str(soma[rcont]) + ":" + conectados
            enviamsg(msg, addr)

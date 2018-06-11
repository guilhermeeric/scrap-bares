'''
##################################################################
##################################################################
##################################################################
#######GUILHERME ERIC, GUSTAVO SANTOS E LEO VIEIRA################
##################################################################
####EXISTEM MUITOS BARES EM SÃO JOSÉ DOS CAMPOS E REGIÃO E########
####NOSSA CABEÇA FICA CONFUSA NA HORA DE ESCOLHER UM BACA-########
####NA PRA LEVAR A NAMORADA. PENSANDO NISTO, RESOLVEMOS RAS-######
####PAR OS DADOS DOS BARES DE SÃO JOSÉ DOS CAMPOS E REGIÃO########
####INSCRITOS NO FOURSQUARE. NESTE SITE, OS LUGARES SÃO AVA-######
####LIADOS POR NOTA E POSSUEM INFORMAÇÃO DE PREÇO, ONDE:##########
####NOTAS VARIAM DE 0 A 10 E PREÇOS VARIAM DED $ (BARATO)#########
####A $$$ (CARO). ESTE ALGORITMO ENCONTRA O BAR MAIS BARATO#######
####QUANDO COMPARADO COM OUTROS BARES DA MESMA NOTA. ASSIM,#######
####É POSSÍVEL ENCONTRAR O BAR COM MELHOR CUSTO BENEFÍCIO#########
####PARA IR COMER UMA BATATA FRITA COM A RAPAZIADA.###############
##################################################################
'''

import random
import requests
from bs4 import BeautifulSoup

pagina = requests.get("https://pt.foursquare.com/explore?cat=drinks&mode=url&ne=-22.92488%2C-45.87513&sw=-23.264688%2C-45.954094")
sopa = BeautifulSoup(pagina.content, "html.parser")

bares = {}
notas = {}
caro = []
normal = []
barato = []

somatorio = 0;
elementos = 0;

def limpa_listas():

	global caro
	global normal
	global barato

	caro = []
	normal = []
	barato = []

def reseta_variaveis():

	global somatorio
	global elementos

	somatorio = 0
	elementos = 0

def verifica_frequencia(preco):

	somatorio_preco = 0

	for bar in bares:

		if len(bares[bar][2]) == preco:

			somatorio_preco +=1 

	frequencia_relativa = somatorio_preco / len(bares.keys())

	print("{:.0%}".format(frequencia_relativa), "dos bares em São José dos Campos são ", end = "")
	if (preco == 1): print("baratos.")
	if (preco == 2): print("razoáveis.")
	if (preco == 3): print("caros.")


for bar in sopa.findAll("div", class_= "venueBlock"):

	for nome in bar.findAll("h2"):

		for nota in bar.findAll("div", class_= "venueScore positive"):

			notas[float(nota.get_text())] = []

			for endereco in bar.findAll("div", class_= "venueAddress"):

				for preco in bar.findAll("span", class_= "darken"):

					bares[nome.get_text()] = [nota.get_text(), endereco.get_text(), preco.get_text()]

for bar in bares:

	for nota in notas:

		if float(bares[bar][0]) == nota:

			notas[nota].append(bar)

for nota in notas:

	limpa_listas()

	for bar in notas[nota]:

		if len(bares[bar][2]) == 1:

			barato.append(bar)

			somatorio += float(bares[bar][0])
			elementos += 1

	if barato:

		print("Melhor custo benefício em bares com nota %0.1f: %s" %(nota, barato))

print("Média de avaliação de bares com preços baratos: %0.1f" %(somatorio / elementos))

reseta_variaveis()

print("##########################################################################")

for nota in notas:

	limpa_listas()

	for bar in notas[nota]:

		if len(bares[bar][2]) == 2:

			normal.append(bar)

			somatorio += float(bares[bar][0])
			elementos += 1

	if normal:

		print("Preços razoáveis em bares com nota %0.1f: %s" %(nota, normal))

print("Média de avaliação de bares com preços razoáveis: %0.1f" %(somatorio / elementos))

reseta_variaveis()

print("##########################################################################")

for nota in notas:

	limpa_listas()

	for bar in notas[nota]:

		if len(bares[bar][2]) == 3:

			caro.append(bar)

			somatorio += float(bares[bar][0])
			elementos += 1

	if caro:

		print("Preços mais caros em bares com nota %0.1f: %s" %(nota, caro))

print("Média de avaliação de bares com preços caros: %0.1f" %(somatorio / elementos))

reseta_variaveis()

print("##########################################################################")

aleatorio = random.choice(list(bares.items()))

print("Estou com sorte:")
print("Nome do bar: %s \nAvaliação: %s \nEndereço: %s" %(aleatorio[0], aleatorio[1][0], aleatorio[1][1]))
if (len(aleatorio[1][2]) == 1): print("Preço: Barato")
if (len(aleatorio[1][2]) == 2): print("Preço: Razoável")
if (len(aleatorio[1][2]) == 3): print("Preço: Caro")

print("##########################################################################")

verifica_frequencia(1)
verifica_frequencia(2)
verifica_frequencia(3)
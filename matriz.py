import os

caminho ="."

arquivos_txt = [arquivo for arquivo in os.listdir(caminho) if arquivo.endswith(".txt")]

#print(arquivos_txt)

lista_geral = [] #uma lista para armazenar todos os arquivos


#esse loop me formece o nome de cada arquivo e o que tem dentro de cada arquivo em um dicionario
for i in arquivos_txt:
	lista_numeral = []
	with open(i,"r") as file:
		nome = i.split(".")[0] #Eliminando o sufixo .txt
		for linha in file:
			lista_numeral.append(linha.strip())
	lista_geral.append({nome:lista_numeral})


#criando um loop infinito de busca
matriz = input("Digite o numero da matriz: ")
while matriz != "0":
	for dicionario in lista_geral:
		for chave,lista in dicionario.items():
			if matriz in lista:
				print(f"Local: {chave}")		
	matriz = input("Digite o numero da matriz: ")

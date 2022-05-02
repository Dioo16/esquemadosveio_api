from itertools import count


def  transforma_numeros_em_cdn(numero):
    centena_do_numero = numero // 100
    denzena_do_numero = (numero % 100) // 10
    unidade_do_numero = numero % 10
    
    return [centena_do_numero, denzena_do_numero , unidade_do_numero]

def cria_base_matriz(numeros_primeira_lista, numeros_segunda_lista):
    matriz_numeros = [[]]
    primeira_linha = 1
    colunas = 6
    indice_segunda_lista = 0
    for linha in range(primeira_linha):      
        for coluna in range(colunas):
            if coluna < len(numeros_primeira_lista):
                matriz_numeros[linha].append(numeros_primeira_lista[coluna])
            else:
                matriz_numeros[linha].append(numeros_segunda_lista[indice_segunda_lista])
                indice_segunda_lista += 1
     
    return matriz_numeros
    

def cria_base_de_numeros(lista_numeros):
    numero_base = 271 #pq? não sei, mas funciona, entao, fodase
    soma_total_de_numeros = sum(lista_numeros)
    numero_linhas = 10
    numero_colunas = 6
    segunda_linha_da_matriz = 1
    primeira_coluna = 0
    ultima_coluna = 5
    primeira_lista_cdn = transforma_numeros_em_cdn(soma_total_de_numeros)
    segunda_lista_cdn = transforma_numeros_em_cdn(numero_base)
    matriz_com_base = cria_base_matriz(primeira_lista_cdn, segunda_lista_cdn)
    
    for linha in range(segunda_linha_da_matriz,numero_linhas):
        lista_numeros_somados = []
        for coluna in range(numero_colunas):
            linha_anterior = linha - 1
            if coluna < numero_colunas - 1:
                if matriz_com_base[linha_anterior][coluna] + matriz_com_base[linha_anterior][coluna+1] >= 10:
                    numero_reformado_menor_que_dez = (matriz_com_base[linha_anterior][coluna] + matriz_com_base[linha_anterior][coluna+1]) % 10
                    lista_numeros_somados.append(numero_reformado_menor_que_dez)
                else:    
                    lista_numeros_somados.append(matriz_com_base[linha_anterior][coluna] + matriz_com_base[linha_anterior][coluna+1])
            else:
                if matriz_com_base[linha_anterior][primeira_coluna] + matriz_com_base [linha_anterior][ultima_coluna] >= 10:
                    numero_reformado_menor_que_dez = (matriz_com_base[linha_anterior][primeira_coluna] + matriz_com_base [linha_anterior][ultima_coluna]) % 10
                    lista_numeros_somados.append(numero_reformado_menor_que_dez)

                else:     
                     lista_numeros_somados.append(matriz_com_base[linha_anterior][primeira_coluna] + matriz_com_base [linha_anterior][ultima_coluna])
        
        matriz_com_base.append(lista_numeros_somados)
        
    return matriz_com_base

def obtem_numeros_ao_redor(linha, coluna_ao_redor_esquerda, coluna_ao_redor_direita, linhas_abaixo, linhas_acima, matriz, coluna):
    numeros_calculo = [[],[],[]]
    numeros_por_linha = 0
    numeros_por_alinha_acima = 0
    numeros_por_linha_abaixo = 0
   
    if coluna_ao_redor_esquerda != -1 and coluna_ao_redor_direita == -1  and linhas_acima == -1 and linhas_abaixo != -1:
        for index_linha in range(linha, linhas_abaixo + 1 ):
            for index_coluna in range(coluna_ao_redor_esquerda, coluna + 1 ):
                numeros_calculo[numeros_por_linha].append(matriz[index_linha][index_coluna])
                        
            numeros_por_linha += 1
                
    elif coluna_ao_redor_esquerda != -1 and coluna_ao_redor_direita != -1 and linhas_acima == -1 and linhas_abaixo != -1:
            for index_linha in range(linha, linhas_abaixo + 1):
                for index_coluna_esquerda in range(coluna-1, coluna + 2 ):
                    numeros_calculo[numeros_por_linha].append(matriz[index_linha][index_coluna_esquerda])
                    
                    
                numeros_por_linha += 1
            
     
    
            
    elif coluna_ao_redor_esquerda == -1 and coluna_ao_redor_direita != -1  and linhas_acima == -1 and linhas_abaixo != -1:
        for index_linha in range(linha, linhas_abaixo + 1 ):
            for index_coluna in range(coluna, coluna_ao_redor_direita + 1 ):
                numeros_calculo[numeros_por_linha].append(matriz[index_linha][index_coluna])
                    
            numeros_por_linha += 1
    
    elif coluna_ao_redor_esquerda != -1 and coluna_ao_redor_direita == -1  and linhas_acima != -1 and linhas_abaixo == -1:
        for index_linha in range(linhas_acima, linha + 1 ):
            for index_coluna in range(coluna_ao_redor_esquerda, coluna + 1 ):
                numeros_calculo[numeros_por_linha].append(matriz[index_linha][index_coluna])
                        
            numeros_por_linha += 1
                
    elif coluna_ao_redor_esquerda != -1 and coluna_ao_redor_direita != -1 and linhas_acima != -1 and linhas_abaixo == -1:
            for index_linha in range(linhas_acima, linha + 1):
                for index_coluna_esquerda in range(coluna-1, coluna + 2 ):
                    numeros_calculo[numeros_por_linha].append(matriz[index_linha][index_coluna_esquerda])
                    
                    
                numeros_por_linha += 1
            
    elif coluna_ao_redor_esquerda == -1 and coluna_ao_redor_direita != -1  and linhas_acima != -1 and linhas_abaixo == -1:
        for index_linha in range(linhas_acima, linha + 1 ):
            for index_coluna in range(coluna, coluna_ao_redor_direita + 1 ):
                numeros_calculo[numeros_por_linha].append(matriz[index_linha][index_coluna])
                    
            numeros_por_linha += 1
               

    elif coluna_ao_redor_direita == -1 and coluna_ao_redor_esquerda != 1 and linhas_acima != -1 and linhas_abaixo != -1:
        for index_linha in range(linhas_acima, linha + 2 ):
                for index_coluna in range(coluna_ao_redor_esquerda, coluna + 1):
                    numeros_calculo[numeros_por_alinha_acima].append(matriz[index_linha][index_coluna])
                    
                
                    
                numeros_por_alinha_acima += 1
                
        
    else:
            for index_linha in range(linhas_acima, linha + 2 ):
                for index_coluna in range(coluna_ao_redor_esquerda, coluna_ao_redor_direita+1):
                    numeros_calculo[numeros_por_alinha_acima].append(matriz[index_linha][index_coluna])
                    
                
                    
                numeros_por_alinha_acima += 1
                
                
    
    return numeros_calculo        
    

def transforma_numeros_ao_redor(lista_de_numeros):
    numeros_transformados = []
    
    for index_linha in range(len(lista_de_numeros) + 1):
        numero_total_de_numeros_na_lista = 0
        if index_linha < len(lista_de_numeros) - 1:
            for index_coluna in range(len(lista_de_numeros[0])):
                if numero_total_de_numeros_na_lista < len(lista_de_numeros[0]):
                    if index_coluna < len(lista_de_numeros):
                        if index_coluna < len(lista_de_numeros) - 1:
                            numeros_transformados.append(lista_de_numeros[index_linha][index_coluna] * 10 + lista_de_numeros[index_linha][index_coluna + 1])
                            numeros_transformados.append(lista_de_numeros[index_linha][index_coluna + 1] * 10 + lista_de_numeros[index_linha][index_coluna])
                        else:
                            numeros_transformados.append(lista_de_numeros[index_linha][index_coluna] * 10 + lista_de_numeros[index_linha][index_coluna - 1])
                            numeros_transformados.append(lista_de_numeros[index_linha][index_coluna - 1] * 10 + lista_de_numeros[index_linha][index_coluna])
                            
                    if index_linha < len(lista_de_numeros)  and index_coluna < len(lista_de_numeros[0]) :
                        if index_coluna < len(lista_de_numeros[0]) - 1 and index_linha <len(lista_de_numeros)-1:
                            numeros_transformados.append(lista_de_numeros[index_linha][index_coluna] * 10 + lista_de_numeros[index_linha + 1][index_coluna])
                            numeros_transformados.append(lista_de_numeros[index_linha][index_coluna] * 10 + lista_de_numeros[index_linha + 1][index_coluna + 1])

                            numeros_transformados.append(lista_de_numeros[index_linha + 1][index_coluna]  * 10 + lista_de_numeros[index_linha][index_coluna])
                            numeros_transformados.append(lista_de_numeros[index_linha + 1][index_coluna +1]  * 10 + lista_de_numeros[index_linha][index_coluna])
                        else:
                            numeros_transformados.append(lista_de_numeros[index_linha][index_coluna] * 10 + lista_de_numeros[index_linha + 1][index_coluna])
                            numeros_transformados.append(lista_de_numeros[index_linha][index_coluna] * 10 + lista_de_numeros[index_linha + 1][index_coluna - 1])

                            numeros_transformados.append(lista_de_numeros[index_linha + 1][index_coluna]  * 10 + lista_de_numeros[index_linha][index_coluna])
                            numeros_transformados.append(lista_de_numeros[index_linha + 1][index_coluna - 1]  * 10 + lista_de_numeros[index_linha][index_coluna])
                        
                        if  len(lista_de_numeros[0]) // 2 == 1 :
                            if index_coluna == 1 :
                                numeros_transformados.append(lista_de_numeros[index_linha][index_coluna] * 10 + lista_de_numeros[index_linha +1][index_coluna - 1])
                                numeros_transformados.append(lista_de_numeros[index_linha][index_coluna]  + lista_de_numeros[index_linha +1][index_coluna - 1] * 10)
                        else:
                            if index_coluna == 1 or index_coluna == 2:
                                numeros_transformados.append(lista_de_numeros[index_linha][index_coluna] * 10 + lista_de_numeros[index_linha +1][index_coluna - 1])
                                numeros_transformados.append(lista_de_numeros[index_linha][index_coluna]  + lista_de_numeros[index_linha +1][index_coluna - 1] * 10)
                                
                numero_total_de_numeros_na_lista += 1                                   
                               
    
    return numeros_transformados
    

    

def numeros_escolhidos(numeros_concursos_passado):
    possiveis_numeros = []
    esquema_formado = cria_base_de_numeros(numeros_concursos_passado) 
    for linha in range(len(esquema_formado)):
        combinacoes_ao_redor = 0
        for coluna in range(len(esquema_formado[0])):
            
            if esquema_formado[linha][coluna] == 0 or  esquema_formado[linha][coluna]  == 1:
                
                if linha == 0:
                    combinacoes_ao_redor_linha_abaixo = linha + 2
                    combinacoes_ao_redor_linha_acima = -1
                    
                    if coluna == 5:
                        colunas_ao_redor_esquerda = coluna - 2
                        colunas_ao_redor_direita = -1
                        
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                    elif coluna == 4:
                        colunas_ao_redor_esquerda = coluna - 2
                        colunas_ao_redor_direita = coluna 
                
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                    elif coluna == 0:
                        colunas_ao_redor_direita = coluna + 2
                        colunas_ao_redor_esquerda = -1
                        
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                    elif coluna == 1:
                        colunas_ao_redor_esquerda = coluna - 1
                        colunas_ao_redor_direita = coluna + 2
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                    else:
                        colunas_ao_redor_esquerda = coluna - 1
                        colunas_ao_redor_direita = coluna +1
                        
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                        
                    
                    
                elif linha == 1:
                    
                    combinacoes_ao_redor_linha_abaixo = linha + 1
                    combinacoes_ao_redor_linha_acima = linha - 1
                    
                
                    if coluna == 5:
                        colunas_ao_redor_esquerda = coluna - 2
                        colunas_ao_redor_direita = -1
                        
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                                
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                    elif coluna == 4:
                        colunas_ao_redor_esquerda = coluna - 2
                        colunas_ao_redor_direita = coluna 
                
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                    elif coluna == 0:
                        colunas_ao_redor_direita = coluna + 2
                        colunas_ao_redor_esquerda = -1
                        
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                    elif coluna == 1:
                        colunas_ao_redor_esquerda = coluna - 1
                        colunas_ao_redor_direita = coluna + 2
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                        
                    else:
                        colunas_ao_redor_esquerda = coluna - 1
                        colunas_ao_redor_direita = coluna +1
                        
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                elif linha == 8:
                    combinacoes_ao_redor_linha_abaixo = linha + 1
                    combinacoes_ao_redor_linha_acima = linha - 1
                    
                    if coluna == 5:
                        colunas_ao_redor_esquerda = coluna - 2
                        colunas_ao_redor_direita = -1
                        
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                    elif coluna == 4:
                        colunas_ao_redor_esquerda = coluna - 2
                        colunas_ao_redor_direita = coluna 
                
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                    elif coluna == 0:
                        colunas_ao_redor_direita = coluna + 2
                        colunas_ao_redor_esquerda = -1
                        
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                    elif coluna == 1:
                        colunas_ao_redor_esquerda = coluna - 1
                        colunas_ao_redor_direita = coluna + 2
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                    else:
                        colunas_ao_redor_esquerda = coluna - 1
                        colunas_ao_redor_direita = coluna +1
                        
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                elif linha == 9:
                    combinacoes_ao_redor_linha_acima = linha - 2
                    combinacoes_ao_redor_linha_abaixo = -1
                    
                    if coluna == 5:
                        colunas_ao_redor_esquerda = coluna - 2
                        colunas_ao_redor_direita = -1
                        
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                    elif coluna == 4:
                        colunas_ao_redor_esquerda = coluna - 2
                        colunas_ao_redor_direita = coluna 
                
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                    elif coluna == 0:
                        colunas_ao_redor_direita = coluna + 2
                        colunas_ao_redor_esquerda = -1
                        
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                    elif coluna == 1:
                        colunas_ao_redor_esquerda = coluna - 1
                        colunas_ao_redor_direita = coluna + 2
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                    else:
                        colunas_ao_redor_esquerda = coluna - 1
                        colunas_ao_redor_direita = coluna +1
                        
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                        
                
                        
                else:
                    combinacoes_ao_redor_linha_abaixo = linha + 1
                    combinacoes_ao_redor_linha_acima = linha - 1
                    
                    if coluna == 5:
                        colunas_ao_redor_esquerda = coluna - 2
                        colunas_ao_redor_direita = -1
                        
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                    elif coluna == 4:
                        colunas_ao_redor_esquerda = coluna - 2
                        colunas_ao_redor_direita = coluna 
                
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                    elif coluna == 0:
                        colunas_ao_redor_direita = coluna + 2
                        colunas_ao_redor_esquerda = -1
                        
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
                    elif coluna == 1:
                        colunas_ao_redor_esquerda = coluna - 1
                        colunas_ao_redor_direita = coluna + 2
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                    else:
                        colunas_ao_redor_esquerda = coluna - 1
                        colunas_ao_redor_direita = coluna +1
                        
                        numeros_calculo = obtem_numeros_ao_redor(linha, colunas_ao_redor_esquerda, colunas_ao_redor_direita, combinacoes_ao_redor_linha_abaixo, combinacoes_ao_redor_linha_acima, esquema_formado, coluna)
                        possiveis_numeros.append(transforma_numeros_ao_redor(numeros_calculo))
                        
    numeros_sem_romper_máximo_quina = []                  

                    
    possiveis_numeros_totais = []


    for lista in range(len(possiveis_numeros)):
        possiveis_numeros[lista] = list(set(possiveis_numeros[lista]))
        

    for lista in range(len(possiveis_numeros)):
        numeros_sem_romper_máximo_quina.append([x for x in possiveis_numeros[lista] if x < 80])           


    for lista in range(len(numeros_sem_romper_máximo_quina)):
        for numero in range(len(numeros_sem_romper_máximo_quina[lista])):
            possiveis_numeros_totais.append(numeros_sem_romper_máximo_quina[lista][numero])
            
            
    possiveis_numeros_tratados = list(set(possiveis_numeros_totais))

    return possiveis_numeros_tratados


def transforma_em_lista_numeros_get(numeros):
    lista_numeros = list(int(numero) for numero in numeros.split(','))
    return lista_numeros


def tabela_dos_numeros(numeros):
    esquema_formado = cria_base_de_numeros(numeros)
    tabela_numeros = '''''' 
    for lista in esquema_formado:
        cont = 0
        for elemento in lista:
            cont += 1
            tabela_numeros += str(elemento) + ''' '''
            if cont == 6:
                tabela_numeros += '\n'
    
    return tabela_numeros
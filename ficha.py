import random

import utils

nypes = ['♠', '♡', '♢', '♣']
min = 1
max = 6

individualizacao_dados = utils.individualizacao_zero

baralho_inicial = utils.cria_baralho(min, max, nypes)
individ_preenchida = []
need = ['f', 'd', 'i', 's', 'c', 'o']
individ_dict = {'f': 'forca', 'd': 'destreza', 's': 'sabedoria', 'i': 'intelecto', 'c': 'carisma', 'o': 'sobrenatural'}
x = 1


# while need:
#     value = str(input(f"Escolha sua Individualização numero {x}: Força (F), Destreza (D), Intelecto (I), Sabedoria (S), Carisma (C), Sobrenatural (Oculto) (O):\n Ainda faltam:{need}\n")).lower()
#     if value in need:
#         x += 1
#         need.remove(value)
#         individ_preenchida.append(individ_dict[value])

# primeira_indiv = True
# valores_sorteados = []
# for indiv in individ_preenchida:
#     baralho_sorteio = baralho_inicial.copy()
#     for atributo in individualizacao_dados[indiv]:
#         print(f"Sorteio para a individualização {indiv}")
#         carta_sorteada = random.choice(baralho_sorteio)
#         baralho_sorteio.remove(carta_sorteada)
#         print(carta_sorteada)

#         if primeira_indiv:
#             retry = None
#             while retry not in ('s', 'n'):
#                 retry = str(input(f"Tirar carta para substituir? (S/N)")).lower()
#             if retry == 's':
#                 carta_sorteada = random.choice(baralho_sorteio)
#                 baralho_sorteio.remove(carta_sorteada)
#                 print(f"Substituido por {carta_sorteada}")
#         valores_sorteados.append(carta_sorteada[0])

#     for atributo in individualizacao_dados[indiv]:
#         valor = None
#         while valor not in valores_sorteados:
#             valor = int(input(f"O atributo {atributo} usara qual valor sorteado? ({valores_sorteados})")) #TODO Treat errors strings
#         valores_sorteados.remove(valor)
#         individualizacao_dados[indiv][atributo] = valor
#     primeira_indiv = False

### Mock
individ_preenchida = ['forca', 'destreza','carisma', 'sobrenatural', 'sabedoria','intelecto']
individ_preenchida = ['sobrenatural', 'sabedoria','destreza', 'forca', 'intelecto','carisma']
for indiv in individ_preenchida:
    baralho_sorteio = baralho_inicial.copy()
    for atributo in individualizacao_dados[indiv]:
        carta_sorteada = random.choice(baralho_sorteio)
        individualizacao_dados[indiv][atributo] = carta_sorteada[0]
# [4,5,3,4,5],[1,5,6,4,2],[1,2,2,3,5],[2,5,4,3,1],[2,3,1,2,3],[2,5,1,3,2]
### END MOCK

individualizacao_tabela = individualizacao_dados
print(f"DADOS: {individualizacao_dados}")

#### Sum with table
individ_fazer_tab = individ_preenchida.copy()
for indiv in individ_preenchida:
    # print(f"INDIVIDUALIDADE {indiv}")
    for atributo in individualizacao_dados[indiv]:
        # print(f"ATRIBUTO {atributo}")
        valor_individualizacao_dados = individualizacao_dados[indiv][atributo]
        operacoes = utils.tabela_individualizacao[indiv][atributo][str(valor_individualizacao_dados)]
        # print(operacoes)
        if operacoes:
            for operacao in operacoes:
                indiv_a_alterar = utils.obtain_atrb_father(operacao[0])
                # print(f"VAI ALTERAR {indiv_a_alterar} {operacao[0]} em {operacao[1]}")
                # print(f"TA AQUI? {individ_fazer_tab}")
                if indiv_a_alterar in individ_fazer_tab:
                    # print("SIM")
                    # print(individualizacao_tabela[indiv_a_alterar][operacao[0]])
                    individualizacao_tabela[indiv_a_alterar][operacao[0]] = individualizacao_tabela[indiv_a_alterar][operacao[0]] + operacao[1]
                    # print(individualizacao_tabela[indiv_a_alterar][operacao[0]])
                    if individualizacao_tabela[indiv_a_alterar][operacao[0]] < 1:
                        individualizacao_tabela[indiv_a_alterar][operacao[0]] = 1
    individ_fazer_tab.remove(indiv)

print(f"TABELA: {individualizacao_tabela}")


utils.plot_char(individualizacao_dados)
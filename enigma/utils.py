import math
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import random

import numpy as np
import pandas as pd

import tables


nypes = ['♠', '♡', '♢', '♣']


class Ficha:
    indiv = tables.indiv_zero
    atq_insanidade = 0
    indiv_order = []
    disturbs = []


def create_ficha(baralho_inicial, max_value, ficha=None):
    if ficha is None:
        ficha = Ficha()
    if not ficha.indiv_order:
        ficha = define_indiv_order(ficha)
    if ficha.indiv == tables.indiv_zero:
        ficha = sorteio_indiv(ficha, baralho_inicial, max_value)
        plot_ficha(ficha)
    ficha = apply_indiv_table(ficha, max_value)
    # ficha = select_disturbs(ficha, 3) #TODO
    # ficha = apply_disturbs(ficha) #TODO
    # ficha = select_virtude(ficha, 1) #TODO
    # ficha = apply_virtude(ficha) #TODO

    return ficha


def define_indiv_order(ficha):
    indiv_order = []
    need = ['f', 'd', 'i', 's', 'c', 'o']
    indiv_dict = {'f': 'forca', 'd': 'destreza', 's': 'sabedoria', 'i': 'intelecto', 'c': 'carisma', 'o': 'sobrenatural'}
    x = 1
    while need:
        value = str(input(f"Escolha sua Individualização numero {x}: Força (F), Destreza (D), Intelecto (I), Sabedoria (S), Carisma (C), Sobrenatural (Oculto) (O):\n Ainda faltam:{need}\n")).lower()
        if value in need:
            x += 1
            need.remove(value)
            indiv_order.append(indiv_dict[value])
    ficha.indiv_order = indiv_order
    return ficha


def sorteio_indiv(ficha, baralho_inicial, max_value):
    individualizacao_dados = ficha.indiv
    primeira_indiv = True
    valores_sorteados = []
    indiv_order = ficha.indiv_order
    for indiv in indiv_order:
        for atributo in individualizacao_dados[indiv]:
            print(f"### Embaralhou ###")
            baralho_sorteio = baralho_inicial.copy()
            print(f"Sorteio para a individualização {map_names[indiv]}")
            carta_sorteada = random.choice(baralho_sorteio)
            baralho_sorteio.remove(carta_sorteada)
            print(carta_sorteada)

            valor = carta_sorteada[0]
            if primeira_indiv:
                retry = None
                while retry not in ('s', 'n'):
                    retry = str(input(f"Tirar carta para tentar trocar? (S/N)")).lower()
                if retry == 's':
                    sub = None
                    nova_carta_sorteada = random.choice(baralho_sorteio)
                    baralho_sorteio.remove(nova_carta_sorteada)
                    print(f"Nova carta: {nova_carta_sorteada}")
                    while sub not in ('s', 'n'):
                        sub = str(input(f"Substituir o valor anterior? (S/N)")).lower()
                        if sub == 's':
                            valor = nova_carta_sorteada[0]
                        else:
                            valor = carta_sorteada[0]
            valor_limitado = valor if valor <= max_value else max_value
            valores_sorteados.append(valor_limitado)

        #Atribute the values to individualities
        for atributo in individualizacao_dados[indiv]:
            #TODO Show remaining attributes
            #TODO automatically apply last value
            valor = None
            while valor not in valores_sorteados:
                valor = input(f"O atributo {map_names[atributo]} usara qual valor sorteado? ({valores_sorteados})")
                if valor.isnumeric():
                    valor = int(valor)
            valores_sorteados.remove(valor)
            individualizacao_dados[indiv][atributo] = valor
        primeira_indiv = False
    ficha.indiv = individualizacao_dados
    return ficha


def apply_indiv_table(ficha, max_value):
    indiv_pos_tab = ficha.indiv.copy()
    indiv_ficha_immutable = ficha.indiv.copy()
    indivs_that_can_be_changed = ficha.indiv_order
    for indiv in ficha.indiv_order:
        for atributo in indiv_ficha_immutable[indiv]:
            valor_ficha = indiv_ficha_immutable[indiv][atributo]
            operacoes = tables.tabela_individualizacao[indiv][atributo][str(valor_ficha)]
            if operacoes:
                for operacao in operacoes:
                    operation_atr = operacao[0]
                    operation_value = operacao[1]
                    operation_indiv = obtain_atrb_father(operation_atr)
                    if operation_indiv in indivs_that_can_be_changed:
                        indiv_pos_tab[operation_indiv][operation_atr] = indiv_pos_tab[operation_indiv][operation_atr] + operation_value
                        if indiv_pos_tab[operation_indiv][operation_atr] < 1:
                            indiv_pos_tab[operation_indiv][operation_atr] = 1
                        if indiv_pos_tab[operation_indiv][operation_atr] > max_value:
                            indiv_pos_tab[operation_indiv][operation_atr] = max_value
        indivs_that_can_be_changed.remove(indiv)
    ficha.indiv = indiv_pos_tab
    return ficha


def select_disturbs(ficha, n=3):
    disturbs = []

    ficha.disturbs = disturbs
    return ficha


def apply_disturbs(ficha):
    #### DISTURBIOS ####
    gabriel_posficha = [('controleemocional', -2), ('forcmental', 1), ('blefe', 1)]
    posficha = gabriel_posficha
    for operation in posficha:
        valor_atual = individualizacao_tabela[obtain_atrb_father(operation[0])][operation[0]]
        diff = int(valor_atual) + int(operation[1])
        if diff < 1:
            individualizacao_tabela[obtain_atrb_father(operation[0])][operation[0]] = 1
        if diff >= max_value:
            individualizacao_tabela[obtain_atrb_father(operation[0])][operation[0]] = max_value
        else:
            individualizacao_tabela[obtain_atrb_father(operation[0])][operation[0]] = diff
    return ficha



def interval(start, end):
    return range(start, end+1)


def cria_baralho(min, max, nypes=nypes):
    baralho = []
    if not isinstance(nypes, list):
        nypes = [nypes]

    if nypes is None:
        for n in interval(start, end)(min, max):
            baralho.append(n)

    for nype in nypes:
        for n in interval(min, max):
            baralho.append((n, nype))

    return baralho


def obtain_atrb_father(atrb):
    if atrb in ('agressividade', 'luta', 'resistencia', 'vigor', 'brutalidade'):
        return 'forca'
    if atrb in ('agilidade', 'proeficiencia', 'foco', 'equilibrio', 'reflexos'):
        return 'destreza'
    if atrb in ('conhecimentos', 'raclogico', 'controleemocional', 'curiosidade', 'experiencia'):
        return 'intelecto'
    if atrb in ('interpretacao', 'percepcao', 'tino', 'intuicao', 'empatia'):
        return 'sabedoria'
    if atrb in ('aparencia', 'simpatia', 'socializacao', 'blefe', 'ego'):
        return 'carisma'
    if atrb in ('religiao', 'mediunidade', 'conhecocult', 'forcmental', 'clarividencia'):
        return 'sobrenatural'


def pie_heatmap(table, cmap=mpl.cm.tab10, vmin=None, vmax=None,inner_r=0.25, pie_args={}, atrb=None, ax=None):
    n, m = table.shape
    vmin= table.min().min() if vmin is None else vmin
    vmax= table.max().max() if vmax is None else vmax

    centre_circle = plt.Circle((0,0), inner_r, edgecolor='black', facecolor='white', fill=True, linewidth=0.25)
    ax.add_artist(centre_circle)
    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    cmapper = cm.ScalarMappable(norm=norm, cmap=cmap)
    for i, (row_name, row) in enumerate(table.iterrows()):
        labels = None if i > 0 else table.columns
        wedges = ax.pie([1] * m, radius=inner_r+float(n-i)/n, colors=[cmapper.to_rgba(x) for x in row.values],
            labels=labels, startangle=90, counterclock=False, wedgeprops={'linewidth':-1}, **pie_args)
        plt.setp(wedges[0], edgecolor='white',linewidth=1.5)
        plt.setp(wedges[0], edgecolor='white',linewidth=1.5)


def plot_indiv(individualizacao, indiv, ax):
    df = pd.DataFrame()
    atributos = list(individualizacao[indiv].keys())
    avg = 0
    for atributo in atributos:
        array = np.ones(10)
        valor = individualizacao[indiv][atributo]
        avg += int(valor)
        array[0:valor] = 0
        df[map_names[atributo]] = array[::-1].tolist()
    avg = math.floor(avg/len(atributos))
    print(df)

    ax.text(0.5, 0.49, avg, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=40)
    ax.set_title(map_names[indiv], fontweight="bold", size=20)
    pie_heatmap(df, vmin=-1, vmax=1, inner_r=0.2, atrb=indiv, ax=ax)


def plot_ficha(ficha):
    fig, axs = plt.subplots(nrows=2, ncols=3, figsize= (20, 20))
    axs = axs.ravel()
    x = 0
    for indiv in ficha.indiv:
        plot_indiv(ficha.indiv, indiv, axs[x])
        x += 1
    plt.show();


map_names = {
    'forca': 'Força',
    'agressividade': 'Agressividade',
    'luta': 'Luta',
    'resistencia': 'Resistência',
    'vigor': 'Vigor',
    'brutalidade': 'Brutalidade',
    'destreza': 'Destreza',
    'agilidade': 'Agilidade',
    'proeficiencia': 'Proeficiência',
    'equilibrio': 'Equilibrio',
    'foco': 'Foco',
    'reflexos': 'Reflexos',
    'intelecto': 'Intelecto',
    'conhecimentos': 'Conhecimentos',
    'raclogico': 'Raciocinio Lógico',
    'controleemocional': 'Controle Emocional',
    'curiosidade': 'Curiosidade',
    'experiencia': 'Experiência',
    'sabedoria': 'Sabedoria',
    'interpretacao': 'Interpretação',
    'percepcao': 'Percepção',
    'tino': 'Tino',
    'intuicao': 'Intuição',
    'empatia': 'Empatia',
    'carisma': 'Carisma',
    'aparencia': 'Aparência',
    'simpatia': 'Simpatia',
    'socializacao': 'Socialização',
    'blefe': 'Blefe',
    'ego': 'Ego',
    'sobrenatural': 'Sobrenatural',
    'religiao': 'Religião',
    'mediunidade': 'Mediunidade',
    'conhecocult': 'Conhecimento do oculto',
    'forcmental': 'Força Mental',
    'clarividencia': 'Clarividência'
}



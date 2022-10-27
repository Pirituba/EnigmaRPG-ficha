import math
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd


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


def interval(start, end):
    return range(start, end+1)


def cria_baralho(min, max, nypes=None):
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


individualizacao_zero = {
    'forca': {
        'agressividade': 0,
        'luta': 0,
        'resistencia': 0,
        'vigor': 0,
        'brutalidade': 0
    },
    'destreza': {
        'agilidade': 0,
        'proeficiencia': 0,
        'foco': 0,
        'equilibrio': 0,
        'reflexos': 0
    },
    'intelecto': {
        'conhecimentos': 0,
        'raclogico': 0,
        'controleemocional': 0,
        'curiosidade': 0,
        'experiencia': 0
    },
    'sabedoria': {
        'interpretacao': 0,
        'percepcao': 0,
        'tino': 0,
        'intuicao': 0,
        'empatia': 0
    },
    'carisma': {
        'aparencia': 0,
        'simpatia': 0,
        'socializacao': 0,
        'blefe': 0,
        'ego': 0
    },
    'sobrenatural': {
        'religiao': 0,
        'mediunidade': 0,
        'conhecocult': 0,
        'forcmental': 0,
        'clarividencia': 0
    }
}


tabela_individualizacao = {
    'forca': {
        'agressividade': {
            '1': [('brutalidade', -2), ('luta', -2), ('controleemocional', 2)],
            '2': [('brutalidade', -2), ('luta', -2), ('controleemocional', 2)],
            '3': [('brutalidade', -1), ('luta', -1), ('controleemocional', 1)],
            '4': [('brutalidade', -1), ('luta', -1), ('controleemocional', 1)],
            '5': [],
            '6': [('brutalidade', 1), ('luta', 1), ('controleemocional', -1)],
            '7': [('brutalidade', 1), ('luta', 1), ('controleemocional', -1)],
            '8': [('brutalidade', 2), ('luta', 2), ('controleemocional', -2)],
            '9': [('brutalidade', 2), ('luta', 2), ('controleemocional', -2)],
            '10': [('brutalidade', 3), ('luta', 3), ('controleemocional', -3)]
        },
        'luta': {
            '1': [('brutalidade', -2), ('equilibrio', -2)],
            '2': [('brutalidade', -2), ('equilibrio', -2)],
            '3': [('brutalidade', -1), ('equilibrio', -1)],
            '4': [('brutalidade', -1), ('equilibrio', -1)],
            '5': [],
            '6': [('brutalidade', 1), ('equilibrio', 1)],
            '7': [('brutalidade', 1), ('equilibrio', 1)],
            '8': [('brutalidade', 2), ('equilibrio', 2)],
            '9': [('brutalidade', 2), ('equilibrio', 2)],
            '10': [('brutalidade', 3), ('equilibrio', 3)]
        },
        'resistencia': {
            '1': [('brutalidade', -2)], #TODO Dano fisico
            '2': [('brutalidade', -2)], #TODO Dano fisico
            '3': [('brutalidade', -1)], #TODO Dano fisico
            '4': [('brutalidade', -1)], #TODO Dano fisico
            '5': [],
            '6': [('vigor', 1), ('foco', 1)], #TODO Dano fisico
            '7': [('vigor', 1), ('foco', 1)], #TODO Dano fisico
            '8': [('vigor', 2), ('foco', 2)], #TODO Dano fisico
            '9': [('vigor', 2), ('foco', 2)], #TODO Dano fisico
            '10': [('vigor', 3), ('foco', 3)] #TODO Dano fisico
        },
        'vigor': {
            '1':  [('agilidade', -2), ('equilibrio', -2)],
            '2': [('agilidade', -2), ('equilibrio', -2)],
            '3': [('agilidade', -1), ('equilibrio', -1)],
            '4': [('agilidade', -1), ('equilibrio', -1)],
            '5': [],
            '6': [('agilidade', 1), ('equilibrio', 1)],
            '7': [('agilidade', 2), ('equilibrio', 1)],
            '8': [('agilidade', 2), ('equilibrio', 2)],
            '9': [('agilidade', 2), ('equilibrio', 2)],
            '10': [('agilidade', 3), ('equilibrio', 3)],
        },
        'brutalidade': {
            '1': [],
            '2': [],
            '3': [],
            '4': [],
            '5': [],
            '6': [],
            '7': [],
            '8': [],
            '9': [],
            '10': []
        },
    },
    'destreza': {
        'agilidade': {
            '1': [('vigor', -2), ('reflexo', -2)],
            '2': [('vigor', -2), ('reflexo', -2)],
            '3': [('vigor', -1), ('reflexo', -1)],
            '4': [('vigor', -1), ('reflexo', -1)],
            '5': [],
            '6': [('vigor', 1), ('reflexo', 1)],
            '7': [('vigor', 1), ('reflexo', 1)],
            '8': [('vigor', 2), ('reflexo', 2)],
            '9': [('vigor', 2), ('reflexo', 2)],
            '10': [('vigor', 3), ('reflexo', 3)]
        },
        'proeficiencia': {
            '1': [('conhecimentos', -2), ('raclogico', -2)],
            '2': [('conhecimentos', -2), ('raclogico', -2)],
            '3': [('conhecimentos', -1), ('raclogico', -1)],
            '4': [('conhecimentos', -1), ('raclogico', -1)],
            '5': [],
            '6': [('conhecimentos', 1), ('raclogico', 1), ('foco', 1)],
            '7': [('conhecimentos', 1), ('raclogico', 1), ('foco', 1)],
            '8': [('conhecimentos', 2), ('raclogico', 2), ('foco', 2)],
            '9': [('conhecimentos', 2), ('raclogico', 2), ('foco', 2)],
            '10': [('conhecimentos', 3), ('raclogico', 3), ('foco', 3)]
        },
        'foco': {
            '1': [('intuicao', -2), ('interpretacao', -2)],
            '2': [('intuicao', -2), ('interpretacao', -2)],
            '3': [('intuicao', -1), ('interpretacao', -1)],
            '4': [('intuicao', -1), ('interpretacao', -1)],
            '5': [],
            '6': [('intuicao', 1), ('interpretacao', 1)],
            '7': [('intuicao', 1), ('interpretacao', 1)],
            '8': [('intuicao', 2), ('interpretacao', 2)],
            '9': [('intuicao', 2), ('interpretacao', 2)],
            '10': [('intuicao', 3), ('interpretacao', 3)]
        },
        'equilibrio': {
            '1': [('luta', -2), ('vigor', -2)],
            '2': [('luta', -2), ('vigor', -2)],
            '3': [('luta', -1), ('vigor', -1)],
            '4': [('luta', -1), ('vigor', -1)],
            '5': [],
            '6': [('luta', 1), ('vigor', 1)],
            '7': [('luta', 1), ('vigor', 1)],
            '8': [('luta', 2), ('vigor', 2)],
            '9': [('luta', 2), ('vigor', 2)],
            '10': [('luta', 3), ('vigor', 3)],
        },
        'reflexos': {
            '1': [('tino', -2), ('percepcao', -2)],
            '2': [('tino', -2), ('percepcao', -2)],
            '3': [('tino', -1), ('percepcao', -1)],
            '4': [('tino', -1), ('percepcao', -1)],
            '5': [],
            '6': [('tino', 1), ('percepcao', 1)],
            '7': [('tino', 1), ('percepcao', 1)],
            '8': [('tino', 2), ('percepcao', 2)],
            '9': [('tino', 2), ('percepcao', 2)],
            '10': [('tino', 3), ('percepcao', 3)]
        }
    },
    'intelecto': {
        'conhecimentos': {
            '1': [('controleemocional', -2), ('raclogico', -2), ('foco', -2)],
            '2': [('controleemocional', -2), ('raclogico', -2), ('foco', -2)],
            '3': [('controleemocional', -1), ('raclogico', -1), ('foco', -1)],
            '4': [('controleemocional', -1), ('raclogico', -1), ('foco', -1)],
            '5': [],
            '6': [('proeficiencia', 1), ('foco', 1), ('experiencia', 1)],
            '7': [('proeficiencia', 1), ('foco', 1), ('experiencia', 1)],
            '8': [('proeficiencia', 2), ('foco', 2), ('experiencia', 2)],
            '9': [('proeficiencia', 2), ('foco', 2), ('experiencia', 2)],
            '10': [('proeficiencia', 3), ('foco', 3), ('experiencia', 3)]
        },
        'raclogico': {
            '1': [('percepcao', -2), ('interpretacao', -2)],
            '2': [('percepcao', -2), ('interpretacao', -2)],
            '3': [('percepcao', -1), ('interpretacao', -1)],
            '4': [('percepcao', -1), ('interpretacao', -1)],
            '5': [],
            '6': [('percepcao', 1), ('interpretacao', 1)],
            '7': [('percepcao', 1), ('interpretacao', 1)],
            '8': [('percepcao', 2), ('interpretacao', 2)],
            '9': [('percepcao', 2), ('interpretacao', 2)],
            '10': [('percepcao', 3), ('interpretacao', 3)]
        },
        'controleemocional': {
            '1': [('agressividade', -2), ('interpretacao', -2), ('forcmental', -2)],
            '2': [('agressividade', -2), ('interpretacao', -2), ('forcmental', -2)],
            '3': [('agressividade', -1), ('interpretacao', -1), ('forcmental', -1)],
            '4': [('agressividade', -1), ('interpretacao', -1), ('forcmental', -1)],
            '5': [],
            '6': [('agressividade', -1), ('interpretacao', 1), ('forcmental', 1)],
            '7': [('agressividade', -1), ('interpretacao', 1), ('forcmental', 1)],
            '8': [('agressividade', -2), ('interpretacao', 2), ('forcmental', 2)],
            '9': [('agressividade', -2), ('interpretacao', 2), ('forcmental', 2)],
            '10': [('agressividade', -3), ('interpretacao', 3), ('forcmental', 3)],
        },
        'curiosidade': {
            '1': [('intuicao', -2), ('conhecocult', -2)],
            '2': [('intuicao', -2), ('conhecocult', -2)],
            '3': [('intuicao', -1), ('conhecocult', -1)],
            '4': [('intuicao', -1), ('conhecocult', -1)],
            '5': [],
            '6': [('intuicao', 1), ('conhecocult', 1)],
            '7': [('intuicao', 1), ('conhecocult', 1)],
            '8': [('intuicao', 2), ('conhecocult', 2)],
            '9': [('intuicao', 2), ('conhecocult', 2)],
            '10': [('intuicao', 3), ('conhecocult', 3)]
        },
        'experiencia': {
            '1': [],
            '2': [],
            '3': [],
            '4': [],
            '5': [],
            '6': [],
            '7': [],
            '8': [],
            '9': [],
            '10': []
        }
    },
    'sabedoria': {
        'interpretacao': {
            '1': [('experiencia', -2), ('conhecimento', -2), ('percepcao', -2)],
            '2': [('experiencia', -2), ('conhecimento', -2), ('percepcao', -2)],
            '3': [('experiencia', -1), ('conhecimento', -1), ('percepcao', -1)],
            '4': [('experiencia', -1), ('conhecimento', -1), ('percepcao', -1)],
            '5': [],
            '6': [('experiencia', 1), ('conhecimento', 1), ('percepcao', 1)],
            '7': [('experiencia', 1), ('conhecimento', 1), ('percepcao', 1)],
            '8': [('experiencia', 2), ('conhecimento', 2), ('percepcao', 2)],
            '9': [('experiencia', 2), ('conhecimento', 2), ('percepcao', 2)],
            '10': [('experiencia', 3), ('conhecimento', 3), ('percepcao', 3)]
        },
        'percepcao': {
            '1': [('tino', -2), ('reflexo', -2)],
            '2': [('tino', -2), ('reflexo', -2)],
            '3': [('tino', -1), ('reflexo', -1)],
            '4': [('tino', -1), ('reflexo', -1)],
            '5': [],
            '6': [('intuicao', 1), ('reflexo', 1), ('socializacao', 1)],
            '7': [('intuicao', 1), ('reflexo', 1), ('socializacao', 1)],
            '8': [('intuicao', 2), ('reflexo', 2), ('socializacao', 2)],
            '9': [('intuicao', 2), ('reflexo', 2), ('socializacao', 2)],
            '10': [('intuicao', 3), ('reflexo', 3), ('socializacao', 3)]
        },
        'tino': {
            '1': [('religiao', -2), ('mediunidade', -2), ('conhecocult', -2)],
            '2': [('religiao', -2), ('mediunidade', -2), ('conhecocult', -2)],
            '3': [('religiao', -1), ('mediunidade', -1), ('conhecocult', -1)],
            '4': [('religiao', -1), ('mediunidade', -1), ('conhecocult', -1)],
            '5': [],
            '6': [('religiao', 1), ('mediunidade', 1), ('conhecocult', 1)],
            '7': [('religiao', 1), ('mediunidade', 1), ('conhecocult', 1)],
            '8': [('religiao', 2), ('mediunidade', 2), ('conhecocult', 2)],
            '9': [('religiao', 2), ('mediunidade', 2), ('conhecocult', 2)],
            '10': [('religiao', 3), ('mediunidade', 3), ('conhecocult', 3)]
        },
        'intuicao': {
            '1': [('raclogico', -2), ('empatia', -2)],
            '2': [('raclogico', -2), ('empatia', -2)],
            '3': [('raclogico', -1), ('empatia', -1)],
            '4': [('raclogico', -1), ('empatia', -1)],
            '5': [],
            '6': [('reflexo', 1), ('empatia', 1)],
            '7': [('reflexo', 1), ('empatia', 1)],
            '8': [('reflexo', 2), ('empatia', 2)],
            '9': [('reflexo', 2), ('empatia', 2)],
            '10': [('reflexo', 3), ('empatia', 3)],
        },
        'empatia': {
            '1': [('socializacao', -2), ('simpatia', -2)],
            '2': [('socializacao', -2), ('simpatia', -2)],
            '3': [('socializacao', -1), ('simpatia', -1)],
            '4': [('socializacao', -1), ('simpatia', -1)],
            '5': [],
            '6': [('controleemocional', -1), ('simpatia', 1)],
            '7': [('controleemocional', -1), ('simpatia', 1)],
            '8': [('controleemocional', -2), ('simpatia', 2)],
            '9': [('controleemocional', -2), ('simpatia', 2)],
            '10': [('controleemocional', -3), ('simpatia', 3)]
        }
    },
    'carisma': {
        'aparencia': {
            '1': [('socializacao', -2), ('ego', -2)],
            '2': [('socializacao', -2), ('ego', -2)],
            '3': [('socializacao', -1), ('ego', -1)],
            '4': [('socializacao', -1), ('ego', -1)],
            '5': [],
            '6': [('socializacao', 1), ('ego', 1)],
            '7': [('socializacao', 1), ('ego', 1)],
            '8': [('socializacao', 2), ('ego', 2)],
            '9': [('socializacao', 2), ('ego', 2)],
            '10': [('socializacao', 3), ('ego', 3)]
        },
        'simpatia': {
            '1': [('empatia', -2), ('ego', 2)],
            '2': [('empatia', -2), ('ego', 2)],
            '3': [('empatia', -1), ('ego', 1)],
            '4': [('empatia', -1), ('ego', 1)],
            '5': [],
            '6': [('socializacao', 1), ('experiencia', 2)],
            '7': [('socializacao', 1), ('experiencia', 2)],
            '8': [('socializacao', 2), ('experiencia', 2)],
            '9': [('socializacao', 2), ('experiencia', 2)],
            '10': [('socializacao', 3), ('experiencia', 3)]
        },
        'socializacao': {
            '1': [('ego', -2), ('blefe', 2)],
            '2': [('ego', -2), ('blefe', 2)],
            '3': [('ego', -1), ('blefe', 1)],
            '4': [('ego', -1), ('blefe', 1)],
            '5': [],
            '6': [('blefe', 1), ('experiencia', 1)],
            '7': [('blefe', 1), ('experiencia', 1)],
            '8': [('blefe', 2), ('experiencia', 2)],
            '9': [('blefe', 2), ('experiencia', 2)],
            '10': [('blefe', 3), ('experiencia', 3)]
        },
        'blefe': {
            '1': [('controleemoc', -3)],
            '2': [('controleemoc', -2)],
            '3': [('controleemoc', -1)],
            '4': [('controleemoc', -1)],
            '5': [],
            '6': [('experiencia', 1)],
            '7': [('experiencia', 1)],
            '8': [('experiencia', 2)],
            '9': [('experiencia', 2)],
            '10': [('experiencia', 3)]
        },
        'ego': {
            '1': [('vigor', -2)],
            '2': [('vigor', -2)],
            '3': [('vigor', -1)],
            '4': [('vigor', -1)],
            '5': [],
            '6': [('empatia', -1)],
            '7': [('empatia', -1)],
            '8': [('empatia', -2)],
            '9': [('empatia', -2)],
            '10': [('empatia', -3)]
        },
    },
    'sobrenatural': {
        'religiao': {
            '1': [('mediunidade', -2)],
            '2': [('mediunidade', -2)],
            '3': [('mediunidade', -1)],
            '4': [('mediunidade', -1)],
            '5': [],
            '6': [('raclogico', -1), ('intuicao', 1)],
            '7': [('raclogico', -1), ('intuicao', 1)],
            '8': [('raclogico', -2), ('intuicao', 2)],
            '9': [('raclogico', -2), ('intuicao', 2)],
            '10': [('raclogico', -3), ('intuicao', 3)]
        },
        'mediunidade': {
            '1': [('clarividencia', -10)],
            '2': [('clarividencia', -5)],
            '3': [('clarividencia', -4)],
            '4': [('clarividencia', -3)],
            '5': [('clarividencia', -2)],
            '6': [('clarividencia', -1)],
            '7': [],
            '8': [('clarividencia', 1)],
            '9': [('clarividencia', 2)],
            '10': [('clarividencia', 3)]
        },
        'conhecocult': {
            '1': [('forcmental', -2)],
            '2': [('forcmental', -2)],
            '3': [('forcmental', -1)],
            '4': [('forcmental', -1)],
            '5': [],
            '6': [('forcmental', 1)],
            '7': [('forcmental', 1)],
            '8': [('forcmental', 2)],
            '9': [('forcmental', 2)],
            '10': [('forcmental', 3)]
        },
        'forcmental': {
            '1': [('controleemoc', -1)], #TODO ataque insanidade
            '2': [('controleemoc', -1)], #TODO ataque insanidade
            '3': [('controleemoc', -2)], #TODO ataque insanidade
            '4': [('controleemoc', -2)], #TODO ataque insanidade
            '5': [],
            '6': [('controleemoc', 1)], #TODO ataque insanidade
            '7': [('controleemoc', 1)], #TODO ataque insanidade
            '8': [('controleemoc', 2)], #TODO ataque insanidade
            '9': [('controleemoc', 2)], #TODO ataque insanidade
            '10': [('controleemoc', 3)], #TODO ataque insanidade
        },
        'clarividencia': {
            '1': [],
            '2': [],
            '3': [],
            '4': [],
            '5': [],
            '6': [],
            '7': [],
            '8': [],
            '9': [],
            '10': []
        },
    }
}


def pie_heatmap(table, cmap=mpl.cm.tab10, vmin=None, vmax=None,inner_r=0.25, pie_args={}, atrb=None):
    n, m = table.shape
    vmin= table.min().min() if vmin is None else vmin
    vmax= table.max().max() if vmax is None else vmax

    centre_circle = plt.Circle((0,0), inner_r, edgecolor='black', facecolor='white', fill=True, linewidth=0.25)
    plt.gcf().gca().add_artist(centre_circle)
    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    cmapper = cm.ScalarMappable(norm=norm, cmap=cmap)
    for i, (row_name, row) in enumerate(table.iterrows()):
        labels = None if i > 0 else table.columns
        wedges = plt.pie([1] * m,radius=inner_r+float(n-i)/n, colors=[cmapper.to_rgba(x) for x in row.values],
            labels=labels, startangle=90, counterclock=False, wedgeprops={'linewidth':-1}, **pie_args)
        plt.setp(wedges[0], edgecolor='white',linewidth=1.5)
        # wedges = plt.pie([1], radius=inner_r+float(n-i-1)/n, colors=['w'], labels=[row_name], startangle=-90, wedgeprops={'linewidth':0})
        plt.setp(wedges[0], edgecolor='white',linewidth=1.5)
        plt.title(atrb, fontsize=40)


def plot_char(individualizacao):
    # fig, axs = plt.subplots(2, 3)
    # axs = axs.ravel()
    # i=0
    for individ in individualizacao:
        df = pd.DataFrame()
        atributos = list(individualizacao[individ].keys())
        avg = 0
        for atributo in atributos:
            array = np.ones(10)
            valor = individualizacao[individ][atributo]
            avg += int(valor)
            array[0:valor] = 0
            # array += 1
            df[atributo] = array[::-1].tolist()
        avg = math.floor(avg/len(atributos))
        print(df)

    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    ax.text(0.5, 0.5, avg, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=40)

    pie_heatmap(df, vmin=-1,vmax=1,inner_r=0.2, atrb=atributo)

    plt.show();

        # axs[i].pie_heatmap(df, vmin=-1,vmax=1,inner_r=0.2)
        # i += 1
        # print(valor)

import utils

nypes = ['♠']#, '♡', '♢', '♣']
min_card = 1
max_card = 6
max_value = 6

baralho_inicial = utils.cria_baralho(min_card, max_card, nypes)


ficha = utils.create_ficha(baralho_inicial, max_value)
utils.plot_ficha(ficha)

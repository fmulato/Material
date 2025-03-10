
def print_example(*args, **kwargs):
    print(args)
    print(kwargs)

print_example(1,2,3, a=4, b=5)

print_example(9, 9, 1976,nome='Fabricio', idade=25, sexo='M', cidade='São Paulo')

# Explanation
# *args:	Posicionais:	        Tupla ( )
# **kwargs:	Nomeados chave=valor:	Dicionário { }
#
# Parâmetro comum: Obrigatório
# Args (posicionais): (1, 2, 3)
# Kwargs (nomeados): {'nome': 'Alice', 'idade': 25}

# deve obedecer a ordem de parâmetros conforme definido: args, kwargs
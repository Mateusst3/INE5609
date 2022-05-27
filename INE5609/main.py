from ListaOdernada.ListaEncadeada import ListaEncadeada

lista = ListaEncadeada()
for i in range(5):
    lista.insere_no_inicio(i)
print("Lista:", lista)

print("Removendo elementos:")
for i in range(5):
    lista.remove(i)
    print("Removendo o elemento {0}: {1}".format(i, lista))
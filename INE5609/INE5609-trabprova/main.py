class No:
    def __init__(self, d):
        self.dado = d
        self.prox = None
        self.ant = None


class Lista_2mte:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def insereFrente(self, novoDd):
        novoNo = No(novoDd)
        novoNo.prox = self.inicio
        if self.inicio is not None:
            self.inicio.ant = novoNo
            self.inicio = novoNo


class Iterador:
    def __init__(self, lista_2mte):
        self.iterador_inicio = lista_2mte.inicio
        self.iterador_final = lista_2mte.fim
        self.elemento_central = None
        self.num_elementos = 0

    def busca_elemento_central(self):
        if self.iterador_inicio == self.iterador_final:
            self.elemento_central = self.iterador_inicio
            return self.iterador_inicio
        else:
            self.proximo_elemento()

    def proximo_elemento(self):
        if self.iterador_final.ant is not None and self.iterador_inicio.prox is not None:
            self.iterador_final = self.iterador_final.ant
            self.iterador_inicio = self.iterador_inicio.prox
            self.busca_elemento_central()
        else:
            return ('Não há elemento central')

lista_enc = Lista_2mte()
lista_enc.insereFrente(50)
lista_enc.insereFrente(30)
lista_enc.insereFrente(12)
lista_enc.insereFrente(9)
lista_enc.insereFrente(6)
iterator = Iterador(lista_enc)
elemento_central = iterator.busca_elemento_central()

print(elemento_central)
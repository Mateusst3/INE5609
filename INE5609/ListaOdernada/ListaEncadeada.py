from ListaOdernada.Caixinha import Caixinha


class ListaEncadeada:

    def __init__(self):
        self.__cabeca = None

    def __repr__(self):
        return "[" + str(self.__cabeca) + "]"

    def get_cabeca(self):
        return self.__cabeca

    def insere_no_inicio(self, novo_dado):
        # 1) Cria uma Caixinha com o novo dado escolhido
        novo_dado = Caixinha(novo_dado)

        # 2) Transforma o proximo dado da caixinha como o atual
        novo_dado.set_proximo(self.__cabeca)

        # 3) Faz com que a cabeça da lista referencie o novo dado
        self.__cabeca = novo_dado

    def insere_depois(self, dado_anterior, novo_dado):
        assert dado_anterior, 'Dado anterior precisa existir'

        # 1) Cria uma nova caixinha com o dado desejado.
        novo_dado = Caixinha(novo_dado)

        # 2) Seta o proximo do novo ser o anterior
        novo_dado.set_proximo(dado_anterior.get_proximo())

        # 3)
        dado_anterior.set_proximo(novo_dado)

    def busca(self, valor):
        corrente = self.__cabeca
        while corrente and corrente.get_dado() != valor:
            corrente = corrente.get_proximo()
        return corrente

    def remove(self, valor):
        assert self.__cabeca, 'Impossível remover valores de uma lista vazia'
        if self.__cabeca.get_dado() == valor:
            self.__cabeca = self.__cabeca.get_proximo()
        else:
            anterior = None
            corrente = self.__cabeca
            while corrente and corrente.get_dado() != valor:
                anterior = corrente
                corrente = corrente.get_proximo()
            if corrente:
                anterior.set_proximo(corrente.get_proximo())
            else:
                anterior.set_proximo(None)

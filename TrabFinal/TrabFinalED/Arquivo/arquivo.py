class Arquivo:
    def __init__(self):
        self.__lista_arquivo = []
        self.__indice_arquivo = []
        self.__ids_arquivo = []

    def adicionar_ao_arquivo(self, elemento):
        if len(self.__indice_arquivo) == 0:
            self.__lista_arquivo.append(elemento)
            self.__ids_arquivo.append(elemento.id)
        else:
            self.__lista_arquivo[self.__indice_arquivo[0]] = elemento
            self.__ids_arquivo.append(elemento.id)
            del self.__indice_arquivo[0]

    def remover_ao_arquivo(self, elemento):
        for i in range(len(self.__lista_arquivo)):
            if self.__lista_arquivo[i] == elemento:
                self.__lista_arquivo[i] = ' '
                self.__indice_arquivo.append(i)
                for x in self.__ids_arquivo:
                    self.__ids_arquivo.remove(x)

    def buscar_no_arquivo(self, id):
        if len(self.__ids_arquivo) > 0:
            for i in self.__ids_arquivo:
                if i == id:
                    for x in self.__lista_arquivo:
                        if x.id == id:
                            return 'elemento presente na lista'
                else:
                    return 'elemento não presente na lista'

    def adicionar_ao_id(self, id):
        self.__ids_arquivo.append(id)
        self.__ids_arquivo.sort()

    def get_lista(self):
        return self.__lista_arquivo

    def get_indice(self):
        return self.__indice_arquivo

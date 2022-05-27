class Caixinha:

    def __init__(self, dado=0, proximo_elemento=None):
        self.__dado = dado
        self.__proximo = proximo_elemento

    def __repr__(self):
        return '%s -> %s' % (self.__dado, self.__proximo)

    def set_proximo(self, proximo):
        self.__proximo = proximo

    def get_proximo(self):
        return self.__proximo

    def get_dado(self):
        return self.__dado
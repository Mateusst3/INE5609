from Arquivo import arquivo

archive = arquivo.Arquivo()

archive.adicionar_ao_arquivo(3)
archive.adicionar_ao_arquivo(5)
archive.remover_ao_arquivo(3)
archive.adicionar_ao_arquivo(8)

print(archive.get_lista())
print(archive.get_indice())

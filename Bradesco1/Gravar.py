arquivo = open('arqText.txt', 'w')
arquivo.write('Curso Python \n')
arquivo.write('Aula Pratica')
arquivo.close()

leitura = open('arqText.txt', 'r')
print(leitura.read())
leitura.close()
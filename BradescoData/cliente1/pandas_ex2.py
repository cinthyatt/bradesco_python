import pandas as pd

Autor = ['Sun Tzu', 'Fernando Pessoa', 'Thomas Mann', 'João Guimarães Rosa']
Livro = ['A Arte da Guerra', 'Poesias Selecionadas', 'A Montanha Mágica', 'Primeiras Estórias']
Ano = [2000, 2004, 2015, 2017]

dados = {'Autor': Autor, 
         'Livro': Livro, 
         'Ano': Ano}
autores = pd.DataFrame(dados)

autores.to_csv('autores.csv', index=False)
print(autores)

autores_read = pd.read_csv('autores.csv', index_col=0)
print(autores_read)

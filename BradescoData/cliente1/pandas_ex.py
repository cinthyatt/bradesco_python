import pandas as pd

'''disciplinas = {'cursos':['Estatistica', 'Economia', 'Calculo', 'Geometria'], 'créditos': [90, 60, 90, 40], 'requisito': [True, False, True, False]}
data = pd.DataFrame(disciplinas)
print(data)'''

nome_cidade = pd.Series(['Maringa', 'Itabira', 'Uberlandia'])
populacao = pd.Series([403.063, 120.904, 699.097])

data = pd.DataFrame({"Cidade": nome_cidade, "População":populacao})
print(data)
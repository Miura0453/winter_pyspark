import pandas as pd
import matplotlib.pyplot as plt


def ploteo_escuelas(x):
    data = pd.read_csv('../exploracion/escuelas-publicas.csv', index_col='id')
    data['delegacion'] = ''

    for i in range(len(data['domicilio'])):
        try:
            data['delegacion'][i] = data['domicilio'][i].split('DELEGACION ')[1].split(',')[0]
        except:
            data['delegacion'][i] = 'Vacio'

    data[data.nombre.str.contains(x)].groupby('delegacion').count()['nombre'].plot(kind='barh')
    plt.title(x)
    plt.show()

def grados_posibles(lista):
    print('Ingresa una de las siguientes opciones')
    for i in lista:
        print(i)

import transforms as trans
from config import lista_grados as grados

if __name__ == '__main__':
    trans.grados_posibles(grados)
    grado_escolar = str(input('Ingrese el Grado Escolar')).upper()
    trans.ploteo_escuelas(grado_escolar)

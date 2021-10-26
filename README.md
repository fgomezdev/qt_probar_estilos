### Proyecto simple para probar una hoa de estilos qss en PyQt

#### Requerimientos mínimos

- PyQt5
- Python 3.7

Para convertir las interfaces ui en archivos python ejecutar el siguiente comando:

Ejecutar este comando dentro del directorio 'archivos_ui':

`pyuic5 -x ./archivos_ui/frm_prueba_estilo.ui -o ./archivos_ui/frm_prueba_estilo_ui.py`


En main.py importar el archivo asociado al formulario ui que se quiere probar y ponerlo como clase padre de la clase frmModelo

~~~
from archivos_ui.frm_prueba_estilo_ui import Ui_frmPruebaEstilo 

class frmModelo(QDialog, Ui_frmPruebaEstilo):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
~~~
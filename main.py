#!/usr/bin/env python

from PyQt5.QtWidgets import (QApplication, QDialog)

from archivos_ui.frm_prueba_estilo_ui import Ui_frmPruebaEstilo


class frmModelo(QDialog, Ui_frmPruebaEstilo):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    qss="styles.qss"
    with open(qss,"r") as fh:
        app.setStyleSheet(fh.read())
    example = frmModelo()
    example.show()
    sys.exit(app.exec_()) 

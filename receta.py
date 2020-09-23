import sys, os
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QMainWindow
from principal import Ui_Buscardor
from resultado import Ui_Resultado

class Resultado(QMainWindow):
    def __init__(self):
        super(Resultado, self).__init__()
        self.ui = Ui_Resultado()
        self.ui.setupUi(self)
    @Slot()
    def cerrar(self):
        self.close() # cierro la ventana abierta. Este self no es el mismo que esta adentro de la clase Principal

class Principal(QMainWindow):
    def __init__(self):
        super(Principal, self).__init__()
        self.ui = Ui_Buscardor()
        self.ui.setupUi(self)

    @Slot()
    def buscar(self):
        self.nombre = self.ui.lblNombre.text() #leo la caja de texto de la ventanita
        self.user = os.popen("whoami").read() #saco el usuario de mi computadora
        self.user = self.user.rsplit() #saco el salto de carro
        self.ruta = "/home/"+self.user[0] #armo la ruta de donde voy a ejecutar el comando
        os.chdir(self.ruta) #configuro donde se va ejecutar el comando
        self.resultado = os.popen("find -not -path '*/\.*' | grep '" + self.nombre + "'").read() #busco los archivos que coincidan con el
        self.ventanita = Resultado() #estoy creando un objeto que es la ventana nueva
        self.ventanita.ui.txtResultado.setText(self.resultado) #agrego texto a la caja de la segunda ventana
        self.ventanita.show() #le estoy diciendo al objeto creado, mostrate

    @Slot()
    def borrar(self):
        self.ui.lblNombre.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Principal()
    window.show()
    sys.exit(app.exec_())
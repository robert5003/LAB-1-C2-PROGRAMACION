from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QSpinBox, QComboBox, QVBoxLayout, QPushButton, QHBoxLayout, QRadioButton, QButtonGroup

# Clase principal para la interfaz de la aplicación
class VentanaPersona(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Datos Característicos de una Persona")
        self.setGeometry(100, 100, 400, 600)

        # Layout principal
        layout_principal = QVBoxLayout()

        # Crear campos de entrada para cada dato característico
        self.campos_datos = []

        layout_principal.addLayout(self.crear_campo("Nombre"))
        layout_principal.addLayout(self.crear_campo("Apellido"))
        layout_principal.addLayout(self.crear_campo("Cédula"))
        layout_principal.addLayout(self.crear_campo("Dirección"))
        layout_principal.addLayout(self.crear_campo("Teléfono"))
        layout_principal.addLayout(self.crear_spinbox("Edad", 1, 120))
        layout_principal.addLayout(self.crear_combobox("Estado Civil", ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]))
        layout_principal.addLayout(self.crear_radiobuttons("Género", ["Masculino", "Femenino", "Otro"]))
        layout_principal.addLayout(self.crear_campo("Ocupación"))
        layout_principal.addLayout(self.crear_campo("Correo Electrónico"))

        # Botón para mostrar los datos ingresados
        boton_mostrar = QPushButton("Mostrar Datos", self)
        boton_mostrar.clicked.connect(self.mostrar_datos)
        layout_principal.addWidget(boton_mostrar)

        # Etiqueta para mostrar la información
        self.etiqueta_info = QLabel(self)
        layout_principal.addWidget(self.etiqueta_info)

        self.setLayout(layout_principal)

    # Método para crear un campo de texto
    def crear_campo(self, titulo):
        layout = QVBoxLayout()
        label = QLabel(f"{titulo}:", self)
        entrada = QLineEdit(self)
        layout.addWidget(label)
        layout.addWidget(entrada)
        self.campos_datos.append(entrada)
        return layout

    # Método para crear un campo con SpinBox
    def crear_spinbox(self, titulo, minimo, maximo):
        layout = QVBoxLayout()
        label = QLabel(f"{titulo}:", self)
        spinbox = QSpinBox(self)
        spinbox.setRange(minimo, maximo)
        layout.addWidget(label)
        layout.addWidget(spinbox)
        self.campos_datos.append(spinbox)
        return layout

    # Método para crear un campo con ComboBox
    def crear_combobox(self, titulo, opciones):
        layout = QVBoxLayout()
        label = QLabel(f"{titulo}:", self)
        combobox = QComboBox(self)
        combobox.addItems(opciones)
        layout.addWidget(label)
        layout.addWidget(combobox)
        self.campos_datos.append(combobox)
        return layout

    # Método para crear opciones de selección con RadioButtons
    def crear_radiobuttons(self, titulo, opciones):
        layout = QVBoxLayout()
        label = QLabel(f"{titulo}:", self)
        layout.addWidget(label)
        grupo = QButtonGroup(self)
        botones = []
        for opcion in opciones:
            radiobutton = QRadioButton(opcion, self)
            grupo.addButton(radiobutton)
            layout.addWidget(radiobutton)
            botones.append(radiobutton)
        self.campos_datos.append(botones)
        return layout

    # Función para mostrar los datos ingresados
    def mostrar_datos(self):
        datos = []
        for campo in self.campos_datos:
            if isinstance(campo, list):
                # Para los RadioButtons, se selecciona el botón marcado
                for boton in campo:
                    if boton.isChecked():
                        datos.append(boton.text())
                        break
            elif isinstance(campo, (QLineEdit, QComboBox, QSpinBox)):
                datos.append(campo.text() if isinstance(campo, QLineEdit) else str(campo.value() if isinstance(campo, QSpinBox) else campo.currentText()))

        # Mostrar los datos en la etiqueta
        self.etiqueta_info.setText("\n".join(datos))

# Ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPersona()
    ventana.show()
    app.exec_()

#Explicacion del Programa

'''
Este programa, utilizando PyQt5, crea una interfaz gráfica para ingresar y mostrar datos de una persona.
La ventana contiene campos de entrada para cada dato característico, como nombre, apellido, cédula, 
dirección, teléfono, edad, estado civil, género, ocupación y correo electrónico.
Además, se incluye un botón para mostrar los datos ingresados. Al presionar este botón, 
se crea una lista con los valores ingresados y se muestra en una etiqueta.
'''
#Problema que resuelve 

'''
Este programa facilita la recolección y visualización de datos de una persona, 
proporcionando una interfaz amigable y fácil de usar. Permite ingresar y verificar 
fácilmente sus datos, seleccionar el tipo de identificación adecuado y visualizar los datos completos.
'''
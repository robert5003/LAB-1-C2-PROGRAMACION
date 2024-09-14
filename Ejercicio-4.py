import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QSpinBox, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout, QButtonGroup

# Clase principal para la interfaz de la aplicación
class VentanaMascotas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Datos de Mascotas")
        self.setGeometry(100, 100, 400, 500)

        # Layout principal vertical
        layout_principal = QVBoxLayout()

        # Crear los elementos de la mascota 1
        layout_mascota1, entrada_nombre1, entrada_raza1, spinbox_edad1, radiobutton_macho1, radiobutton_hembra1 = self.crear_layout_mascota("Mascota 1")
        layout_principal.addLayout(layout_mascota1)

        # Crear los elementos de la mascota 2
        layout_mascota2, entrada_nombre2, entrada_raza2, spinbox_edad2, radiobutton_macho2, radiobutton_hembra2 = self.crear_layout_mascota("Mascota 2")
        layout_principal.addLayout(layout_mascota2)

        # Crear los elementos de la mascota 3
        layout_mascota3, entrada_nombre3, entrada_raza3, spinbox_edad3, radiobutton_macho3, radiobutton_hembra3 = self.crear_layout_mascota("Mascota 3")
        layout_principal.addLayout(layout_mascota3)

        # Botón para mostrar los datos
        boton_mostrar = QPushButton("Mostrar Datos", self)
        boton_mostrar.clicked.connect(self.mostrar_datos)
        layout_principal.addWidget(boton_mostrar)

        # Etiqueta para mostrar la información
        self.etiqueta_info = QLabel(self)
        layout_principal.addWidget(self.etiqueta_info)

        self.setLayout(layout_principal)

        # Almacenar widgets para acceder a ellos luego
        self.campos_mascotas = [
            (entrada_nombre1, entrada_raza1, spinbox_edad1, radiobutton_macho1, radiobutton_hembra1),
            (entrada_nombre2, entrada_raza2, spinbox_edad2, radiobutton_macho2, radiobutton_hembra2),
            (entrada_nombre3, entrada_raza3, spinbox_edad3, radiobutton_macho3, radiobutton_hembra3)
        ]

    def crear_layout_mascota(self, titulo):
        layout_mascota = QVBoxLayout()

        # Nombre
        label_nombre = QLabel(f"{titulo} - Nombre:", self)
        entrada_nombre = QLineEdit(self)
        layout_mascota.addWidget(label_nombre)
        layout_mascota.addWidget(entrada_nombre)

        # Raza
        label_raza = QLabel(f"{titulo} - Raza:", self)
        entrada_raza = QLineEdit(self)
        layout_mascota.addWidget(label_raza)
        layout_mascota.addWidget(entrada_raza)

        # Edad (SpinBox)
        label_edad = QLabel(f"{titulo} - Edad:", self)
        spinbox_edad = QSpinBox(self)
        spinbox_edad.setRange(1, 20)
        layout_mascota.addWidget(label_edad)
        layout_mascota.addWidget(spinbox_edad)

        # Género (RadioButtons)
        label_genero = QLabel(f"{titulo} - Género:", self)
        layout_mascota.addWidget(label_genero)

        grupo_genero = QButtonGroup(self)
        radiobutton_macho = QRadioButton("Macho", self)
        radiobutton_hembra = QRadioButton("Hembra", self)
        grupo_genero.addButton(radiobutton_macho)
        grupo_genero.addButton(radiobutton_hembra)

        # Crear un layout horizontal para los botones de género
        layout_genero = QHBoxLayout()
        layout_genero.addWidget(radiobutton_macho)
        layout_genero.addWidget(radiobutton_hembra)
        layout_mascota.addLayout(layout_genero)

        return layout_mascota, entrada_nombre, entrada_raza, spinbox_edad, radiobutton_macho, radiobutton_hembra

    # Función para mostrar los datos de las mascotas
    def mostrar_datos(self):
        datos_mascotas = []
        for entrada_nombre, entrada_raza, spinbox_edad, radiobutton_macho, radiobutton_hembra in self.campos_mascotas:
            # Extraer los datos de cada mascota
            nombre = entrada_nombre.text()
            raza = entrada_raza.text()
            edad = spinbox_edad.value()
            genero = "Macho" if radiobutton_macho.isChecked() else "Hembra"
            datos_mascotas.append(f"Nombre: {nombre}, Raza: {raza}, Edad: {edad} años, Género: {genero}")

        # Actualizar la etiqueta con los datos
        self.etiqueta_info.setText("\n".join(datos_mascotas))

# Ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaMascotas()
    ventana.show()
    app.exec_()

#Expliacion del Programa
'''
Este programa en PyQt5 crea una interfaz gráfica para ingresar y mostrar datos de mascotas.
La ventana contiene tres secciones para cada mascota, cada una con los correspondientes widgets de entrada (nombre, raza, edad, género).
Al presionar el botón "Mostrar Datos", se extraen los datos ingresados de cada sección y se muestra en una etiqueta.
'''
#Problema que resuelve

'''
El programa facilita la captura y visualización interactiva de datos de mascotas, 
proporcionando una forma sencilla y amigable de usar.
'''